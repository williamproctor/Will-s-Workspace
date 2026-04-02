#!/usr/bin/env python3
"""
Loom Video Downloader for the GrowthX Content Vault.

Downloads Loom videos (MP4), extracts transcripts (VTT/SRT), and
writes structured metadata JSON — all into the content_vault.

Primary engine: yt-dlp (has native Loom extractor since 2024).
Fallback: direct HTTP fetch from Loom's CDN using page-embedded JSON.

Usage:
    # Single video
    python tools/loom_downloader.py https://www.loom.com/share/abc123

    # Batch from file (one URL per line)
    python tools/loom_downloader.py --batch urls.txt

    # Dry run (metadata only, no download)
    python tools/loom_downloader.py --dry-run https://www.loom.com/share/abc123

Environment:
    LOOM_COOKIES    Optional path to a Netscape cookies.txt for private videos
"""

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    requests = None

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
VAULT_ROOT = PROJECT_ROOT / "content_vault"
VIDEO_DIR = VAULT_ROOT / "videos" / "loom"
TRANSCRIPT_DIR = VAULT_ROOT / "transcripts"
METADATA_DIR = VAULT_ROOT / "metadata"

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
log = logging.getLogger("loom_downloader")

LOOM_SHARE_RE = re.compile(
    r"(?:https?://)?(?:www\.)?loom\.com/share/([a-f0-9]+)"
)
LOOM_EMBED_RE = re.compile(
    r"(?:https?://)?(?:www\.)?loom\.com/embed/([a-f0-9]+)"
)


def extract_video_id(url: str) -> str | None:
    """Pull the hex video ID out of a Loom share or embed URL."""
    for pattern in (LOOM_SHARE_RE, LOOM_EMBED_RE):
        m = pattern.search(url)
        if m:
            return m.group(1)
    clean = url.strip().strip("/")
    if re.fullmatch(r"[a-f0-9]{32}", clean):
        return clean
    return None


def _ensure_dirs():
    for d in (VIDEO_DIR, TRANSCRIPT_DIR, METADATA_DIR):
        d.mkdir(parents=True, exist_ok=True)


def _yt_dlp_available() -> bool:
    try:
        subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _fetch_loom_page_json(video_id: str) -> dict | None:
    """
    Hit Loom's share page and pull the embedded Apollo/Next JSON blob
    that contains CDN URLs and metadata. Fallback when yt-dlp is missing.
    """
    if requests is None:
        log.warning("requests library not installed — skipping page-json fallback")
        return None

    share_url = f"https://www.loom.com/share/{video_id}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    try:
        resp = requests.get(share_url, headers=headers, timeout=30)
        resp.raise_for_status()
    except Exception as exc:
        log.warning("Failed to fetch Loom page: %s", exc)
        return None

    patterns = [
        re.compile(r'window\.__NEXT_DATA__\s*=\s*({.*?});?\s*</script>', re.DOTALL),
        re.compile(r'"videoData"\s*:\s*({.*?})\s*[,}]', re.DOTALL),
    ]
    for pat in patterns:
        m = pat.search(resp.text)
        if m:
            try:
                return json.loads(m.group(1))
            except json.JSONDecodeError:
                continue
    return None


def download_with_ytdlp(
    url: str,
    video_id: str,
    *,
    cookies_file: str | None = None,
    write_subs: bool = True,
) -> dict:
    """
    Download video + optional subtitles via yt-dlp.
    Returns a result dict with paths and metadata.
    """
    output_template = str(VIDEO_DIR / f"{video_id}.%(ext)s")

    cmd = [
        "yt-dlp",
        "--no-playlist",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mp4",
        "-o", output_template,
        "--write-info-json",
        "--no-overwrites",
    ]

    if write_subs:
        cmd += ["--write-subs", "--write-auto-subs", "--sub-format", "vtt", "--sub-lang", "en"]

    if cookies_file:
        cmd += ["--cookies", cookies_file]

    cmd.append(url)

    log.info("Running: %s", " ".join(cmd))
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

    if proc.returncode != 0:
        log.error("yt-dlp stderr:\n%s", proc.stderr)
        raise RuntimeError(f"yt-dlp exited {proc.returncode}")

    result = {"video_id": video_id, "source_url": url}

    mp4 = VIDEO_DIR / f"{video_id}.mp4"
    if mp4.exists():
        result["video_path"] = str(mp4)
        result["video_size_bytes"] = mp4.stat().st_size

    info_json = VIDEO_DIR / f"{video_id}.info.json"
    if info_json.exists():
        with open(info_json) as f:
            info = json.load(f)
        result["title"] = info.get("title", "")
        result["duration_seconds"] = info.get("duration")
        result["uploader"] = info.get("uploader", "")
        result["upload_date"] = info.get("upload_date", "")
        result["description"] = info.get("description", "")
        result["thumbnail_url"] = info.get("thumbnail", "")

    sub_path = VIDEO_DIR / f"{video_id}.en.vtt"
    if sub_path.exists():
        dest = TRANSCRIPT_DIR / f"{video_id}.en.vtt"
        sub_path.rename(dest)
        result["transcript_path"] = str(dest)
        log.info("Transcript saved → %s", dest)

    return result


def download_with_fallback(url: str, video_id: str) -> dict:
    """
    Fallback download: scrape the page JSON for a CDN URL, then fetch
    the MP4 directly with requests.
    """
    if requests is None:
        raise RuntimeError(
            "Neither yt-dlp nor the requests library is available. "
            "Install one of them: pip install yt-dlp   OR   pip install requests"
        )

    data = _fetch_loom_page_json(video_id)
    if not data:
        raise RuntimeError(
            f"Could not extract video data from Loom page for {video_id}. "
            "The video may be private or the page structure may have changed."
        )

    cdn_url = None
    title = ""

    def _dig(obj, depth=0):
        nonlocal cdn_url, title
        if depth > 15 or cdn_url:
            return
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("url", "download_url", "raw_url") and isinstance(v, str) and ".mp4" in v:
                    cdn_url = v
                if k == "title" and isinstance(v, str) and not title:
                    title = v
                _dig(v, depth + 1)
        elif isinstance(obj, list):
            for item in obj:
                _dig(item, depth + 1)

    _dig(data)

    if not cdn_url:
        raise RuntimeError("Could not find a CDN download URL in Loom page data")

    mp4_path = VIDEO_DIR / f"{video_id}.mp4"
    log.info("Downloading %s → %s", cdn_url[:80], mp4_path.name)

    with requests.get(cdn_url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(mp4_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 256):
                f.write(chunk)

    return {
        "video_id": video_id,
        "source_url": url,
        "video_path": str(mp4_path),
        "video_size_bytes": mp4_path.stat().st_size,
        "title": title,
    }


def write_metadata(result: dict) -> Path:
    """Persist a JSON sidecar in the metadata directory."""
    video_id = result["video_id"]
    result["downloaded_at"] = datetime.now(timezone.utc).isoformat()
    dest = METADATA_DIR / f"{video_id}.json"
    with open(dest, "w") as f:
        json.dump(result, f, indent=2)
    log.info("Metadata written → %s", dest)
    return dest


def download_one(url: str, *, dry_run: bool = False, cookies_file: str | None = None) -> dict:
    """
    High-level: resolve the video ID, download (or dry-run), write metadata.
    """
    video_id = extract_video_id(url)
    if not video_id:
        raise ValueError(f"Cannot parse Loom video ID from: {url}")

    log.info("Video ID: %s", video_id)

    if dry_run:
        result = {"video_id": video_id, "source_url": url, "dry_run": True}
        data = _fetch_loom_page_json(video_id)
        if data:
            result["page_data_keys"] = list(data.keys())[:20]
        write_metadata(result)
        return result

    existing_mp4 = VIDEO_DIR / f"{video_id}.mp4"
    if existing_mp4.exists():
        log.info("Already downloaded: %s", existing_mp4)
        meta_path = METADATA_DIR / f"{video_id}.json"
        if meta_path.exists():
            with open(meta_path) as f:
                return json.load(f)
        return {"video_id": video_id, "source_url": url, "video_path": str(existing_mp4), "skipped": True}

    use_ytdlp = _yt_dlp_available()
    if use_ytdlp:
        log.info("Using yt-dlp (native Loom extractor)")
        result = download_with_ytdlp(url, video_id, cookies_file=cookies_file)
    else:
        log.info("yt-dlp not found — using HTTP fallback")
        result = download_with_fallback(url, video_id)

    write_metadata(result)
    return result


def download_batch(urls: list[str], *, dry_run: bool = False, cookies_file: str | None = None) -> list[dict]:
    results = []
    total = len(urls)
    for i, url in enumerate(urls, 1):
        log.info("=== [%d/%d] %s ===", i, total, url)
        try:
            r = download_one(url, dry_run=dry_run, cookies_file=cookies_file)
            r["status"] = "ok"
        except Exception as exc:
            log.error("Failed: %s — %s", url, exc)
            r = {"source_url": url, "status": "error", "error": str(exc)}
        results.append(r)
        if i < total:
            time.sleep(1.5)
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Download Loom videos into the GrowthX content vault."
    )
    parser.add_argument(
        "urls",
        nargs="*",
        help="One or more Loom share/embed URLs or bare video IDs",
    )
    parser.add_argument(
        "--batch",
        metavar="FILE",
        help="Path to a text file with one Loom URL per line",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch metadata only — don't download the video file",
    )
    parser.add_argument(
        "--cookies",
        metavar="FILE",
        default=os.environ.get("LOOM_COOKIES"),
        help="Netscape cookies.txt for private videos (or set LOOM_COOKIES env var)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable debug logging",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    urls = list(args.urls or [])

    if args.batch:
        batch_path = Path(args.batch)
        if not batch_path.exists():
            log.error("Batch file not found: %s", batch_path)
            sys.exit(1)
        with open(batch_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    urls.append(line)

    if not urls:
        parser.print_help()
        sys.exit(1)

    _ensure_dirs()

    results = download_batch(urls, dry_run=args.dry_run, cookies_file=args.cookies)

    ok = sum(1 for r in results if r.get("status") == "ok")
    fail = len(results) - ok
    log.info("Done. %d succeeded, %d failed.", ok, fail)

    summary_path = METADATA_DIR / f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(summary_path, "w") as f:
        json.dump(results, f, indent=2)
    log.info("Batch summary → %s", summary_path)

    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
