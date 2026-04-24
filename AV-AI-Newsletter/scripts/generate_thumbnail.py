#!/usr/bin/env python3
"""
Generate a video thumbnail (or any static image) via OpenAI's gpt-image-2 API.

Reads OPENAI_API_KEY from the workspace-root .env (same file the rest of the
workspace uses — never commit it). Writes a PNG to the path you pass in.

Usage:
  # The Dispatch default: save a thumbnail for an edition.
  python scripts/generate_thumbnail.py \
      --slug 2026-04-24 \
      --prompt "$(cat prompts/2026-04-24-thumb.txt)"

  # Arbitrary output path, explicit size/quality.
  python scripts/generate_thumbnail.py \
      --out /tmp/cover.png \
      --prompt "..." \
      --size 1536x1024 \
      --quality high

Defaults are tuned for the Dispatch video-thumbnail use case:
  model   = gpt-image-2
  size    = 1536x1024  (closest supported 3:2 — plays cleanly as a 16:9 poster)
  quality = high
  out     = site/video/thumbs/<slug>.png  (when --slug is given)
"""
from __future__ import annotations

import argparse
import base64
import os
import sys
from pathlib import Path

# ── Locate workspace root and load .env ────────────────────────────────────────
# scripts/generate_thumbnail.py → AV-AI-Newsletter/ → workspace root
SCRIPT_DIR = Path(__file__).resolve().parent
NEWSLETTER_ROOT = SCRIPT_DIR.parent
WORKSPACE_ROOT = NEWSLETTER_ROOT.parent
ENV_PATH = WORKSPACE_ROOT / ".env"


def load_env(path: Path) -> None:
    """Very small .env loader — no external dependency on python-dotenv."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


load_env(ENV_PATH)

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover
    sys.exit(
        "openai SDK not installed. Run:\n"
        f"  {sys.executable} -m pip install openai"
    )


def resolve_output_path(args: argparse.Namespace) -> Path:
    if args.out:
        return Path(args.out).expanduser().resolve()
    if args.slug:
        return (
            NEWSLETTER_ROOT / "site" / "video" / "thumbs" / f"{args.slug}.png"
        ).resolve()
    raise SystemExit("Pass either --out <path> or --slug <YYYY-MM-DD>.")


def generate(prompt: str, *, model: str, size: str, quality: str) -> bytes:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit(
            f"OPENAI_API_KEY not set. Add it to {ENV_PATH} (see .env.example)."
        )
    client = OpenAI(api_key=api_key)
    resp = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )
    datum = resp.data[0]
    if getattr(datum, "b64_json", None):
        return base64.b64decode(datum.b64_json)
    # Fallback to URL download if the API ever returns a URL-mode response.
    url = getattr(datum, "url", None)
    if url:
        import urllib.request
        with urllib.request.urlopen(url) as r:  # noqa: S310
            return r.read()
    raise RuntimeError("OpenAI response contained neither b64_json nor url.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", help="Edition slug, e.g. 2026-04-24. Resolves to site/video/thumbs/<slug>.png.")
    ap.add_argument("--out", help="Explicit output path (overrides --slug).")
    ap.add_argument("--prompt", help="Inline prompt text.")
    ap.add_argument("--prompt-file", help="Read the prompt from a file.")
    ap.add_argument("--model", default="gpt-image-2")
    ap.add_argument("--size", default="1536x1024",
                    help="Any gpt-image-2-supported size. 1536x1024 = 3:2 (poster-friendly).")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    args = ap.parse_args()

    if args.prompt and args.prompt_file:
        ap.error("Pass either --prompt or --prompt-file, not both.")
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    else:
        prompt = args.prompt or ""
    if not prompt.strip():
        ap.error("Prompt is empty. Pass --prompt or --prompt-file.")

    out_path = resolve_output_path(args)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"→ model={args.model}  size={args.size}  quality={args.quality}")
    print(f"→ out:    {out_path}")
    print(f"→ prompt: {prompt[:140]}{'…' if len(prompt) > 140 else ''}")

    png_bytes = generate(prompt, model=args.model, size=args.size, quality=args.quality)
    out_path.write_bytes(png_bytes)

    size_kb = len(png_bytes) / 1024
    print(f"✓ wrote {out_path}  ({size_kb:,.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
