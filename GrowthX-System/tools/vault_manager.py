#!/usr/bin/env python3
"""
Vault Manager for the GrowthX Content Vault.

Indexes downloaded videos, transcripts, and metadata into a unified
catalog. Provides search, tagging, and status views.

Usage:
    python tools/vault_manager.py status          # overview of vault contents
    python tools/vault_manager.py index           # rebuild the catalog index
    python tools/vault_manager.py list            # list all videos
    python tools/vault_manager.py search QUERY    # full-text search across titles/transcripts
    python tools/vault_manager.py tag VIDEO_ID TAG [TAG ...]
    python tools/vault_manager.py info VIDEO_ID   # show details for one video
    python tools/vault_manager.py export           # export catalog as CSV
"""

import argparse
import csv
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
VAULT_ROOT = PROJECT_ROOT / "content_vault"
VIDEO_DIR = VAULT_ROOT / "videos" / "loom"
TRANSCRIPT_DIR = VAULT_ROOT / "transcripts"
METADATA_DIR = VAULT_ROOT / "metadata"
CATALOG_PATH = VAULT_ROOT / "catalog.json"

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
log = logging.getLogger("vault_manager")


def _human_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if abs(n) < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def _fmt_duration(seconds) -> str:
    if seconds is None:
        return "—"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def load_catalog() -> dict:
    if CATALOG_PATH.exists():
        with open(CATALOG_PATH) as f:
            return json.load(f)
    return {"videos": {}, "updated_at": None}


def save_catalog(catalog: dict):
    catalog["updated_at"] = datetime.now(timezone.utc).isoformat()
    with open(CATALOG_PATH, "w") as f:
        json.dump(catalog, f, indent=2)
    log.info("Catalog saved → %s (%d videos)", CATALOG_PATH, len(catalog["videos"]))


def build_index() -> dict:
    """
    Scan the vault directories and build a unified catalog from
    metadata JSON files + filesystem state.
    """
    catalog = load_catalog()
    existing_tags = {vid: entry.get("tags", []) for vid, entry in catalog.get("videos", {}).items()}

    videos = {}

    for meta_file in sorted(METADATA_DIR.glob("*.json")):
        if meta_file.name.startswith("batch_"):
            continue
        with open(meta_file) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                log.warning("Skipping invalid JSON: %s", meta_file)
                continue

        vid = data.get("video_id")
        if not vid:
            continue

        mp4 = VIDEO_DIR / f"{vid}.mp4"
        transcript = TRANSCRIPT_DIR / f"{vid}.en.vtt"

        entry = {
            "video_id": vid,
            "title": data.get("title", ""),
            "source_url": data.get("source_url", ""),
            "uploader": data.get("uploader", ""),
            "upload_date": data.get("upload_date", ""),
            "duration_seconds": data.get("duration_seconds"),
            "description": data.get("description", ""),
            "downloaded_at": data.get("downloaded_at", ""),
            "has_video": mp4.exists(),
            "video_size_bytes": mp4.stat().st_size if mp4.exists() else 0,
            "has_transcript": transcript.exists(),
            "tags": existing_tags.get(vid, []),
        }
        videos[vid] = entry

    for mp4 in VIDEO_DIR.glob("*.mp4"):
        vid = mp4.stem
        if vid not in videos:
            videos[vid] = {
                "video_id": vid,
                "title": "",
                "source_url": "",
                "has_video": True,
                "video_size_bytes": mp4.stat().st_size,
                "has_transcript": (TRANSCRIPT_DIR / f"{vid}.en.vtt").exists(),
                "tags": existing_tags.get(vid, []),
            }

    catalog["videos"] = videos
    save_catalog(catalog)
    return catalog


def cmd_status(_args):
    catalog = load_catalog()
    videos = catalog.get("videos", {})
    total_videos = sum(1 for v in videos.values() if v.get("has_video"))
    total_transcripts = sum(1 for v in videos.values() if v.get("has_transcript"))
    total_size = sum(v.get("video_size_bytes", 0) for v in videos.values())
    all_tags = set()
    for v in videos.values():
        all_tags.update(v.get("tags", []))

    print()
    print("╔══════════════════════════════════════════╗")
    print("║     GrowthX Content Vault — Status       ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║  Videos downloaded:  {total_videos:<20}║")
    print(f"║  Transcripts:        {total_transcripts:<20}║")
    print(f"║  Total size:         {_human_size(total_size):<20}║")
    print(f"║  Catalog entries:    {len(videos):<20}║")
    print(f"║  Unique tags:        {len(all_tags):<20}║")
    print(f"║  Last indexed:       {(catalog.get('updated_at') or '—')[:19]:<20}║")
    print("╚══════════════════════════════════════════╝")
    print()

    if not videos:
        print("  Vault is empty. Run the Loom downloader to get started:")
        print("    python tools/loom_downloader.py https://www.loom.com/share/YOUR_VIDEO_ID")
        print()


def cmd_index(_args):
    catalog = build_index()
    print(f"Indexed {len(catalog['videos'])} video(s).")


def cmd_list(args):
    catalog = load_catalog()
    videos = catalog.get("videos", {})
    if not videos:
        print("Vault is empty. Run `vault_manager.py index` after downloading videos.")
        return

    entries = sorted(videos.values(), key=lambda v: v.get("downloaded_at", ""), reverse=True)

    if args.tag:
        entries = [e for e in entries if args.tag in e.get("tags", [])]

    for e in entries:
        status = "✓" if e.get("has_video") else "✗"
        transcript = "T" if e.get("has_transcript") else " "
        size = _human_size(e.get("video_size_bytes", 0)) if e.get("has_video") else "—"
        duration = _fmt_duration(e.get("duration_seconds"))
        tags = ", ".join(e.get("tags", []))
        title = e.get("title", "")[:50] or e["video_id"][:12]
        print(f"  {status} [{transcript}] {e['video_id'][:12]}  {duration:>8}  {size:>10}  {title}  {f'[{tags}]' if tags else ''}")

    print(f"\n  {len(entries)} video(s)")


def cmd_search(args):
    query = args.query.lower()
    catalog = load_catalog()
    matches = []

    for vid, entry in catalog.get("videos", {}).items():
        searchable = " ".join([
            entry.get("title", ""),
            entry.get("description", ""),
            entry.get("uploader", ""),
            " ".join(entry.get("tags", [])),
        ]).lower()

        if query in searchable:
            matches.append(entry)
            continue

        transcript_path = TRANSCRIPT_DIR / f"{vid}.en.vtt"
        if transcript_path.exists():
            text = transcript_path.read_text(errors="ignore").lower()
            if query in text:
                matches.append(entry)

    if matches:
        print(f"Found {len(matches)} result(s) for '{args.query}':\n")
        for e in matches:
            title = e.get("title", "") or e["video_id"]
            print(f"  • {e['video_id'][:12]}  {title}")
    else:
        print(f"No results for '{args.query}'.")


def cmd_tag(args):
    catalog = load_catalog()
    videos = catalog.get("videos", {})

    matching = [vid for vid in videos if vid.startswith(args.video_id)]
    if not matching:
        print(f"No video found matching '{args.video_id}'.")
        sys.exit(1)
    if len(matching) > 1:
        print(f"Ambiguous ID '{args.video_id}' matches: {matching}")
        sys.exit(1)

    vid = matching[0]
    existing = set(videos[vid].get("tags", []))
    existing.update(args.tags)
    videos[vid]["tags"] = sorted(existing)
    save_catalog(catalog)
    print(f"Tags for {vid}: {videos[vid]['tags']}")


def cmd_info(args):
    catalog = load_catalog()
    videos = catalog.get("videos", {})

    matching = [vid for vid in videos if vid.startswith(args.video_id)]
    if not matching:
        print(f"No video found matching '{args.video_id}'.")
        sys.exit(1)

    vid = matching[0]
    entry = videos[vid]
    print(json.dumps(entry, indent=2))


def cmd_export(_args):
    catalog = load_catalog()
    videos = catalog.get("videos", {})
    if not videos:
        print("Nothing to export.")
        return

    dest = VAULT_ROOT / "catalog_export.csv"
    fields = [
        "video_id", "title", "source_url", "uploader", "upload_date",
        "duration_seconds", "has_video", "video_size_bytes",
        "has_transcript", "tags", "downloaded_at",
    ]
    with open(dest, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for entry in videos.values():
            row = dict(entry)
            row["tags"] = "; ".join(row.get("tags", []))
            writer.writerow(row)

    print(f"Exported {len(videos)} video(s) → {dest}")


def main():
    parser = argparse.ArgumentParser(
        description="Manage the GrowthX Content Vault."
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Show vault overview")
    sub.add_parser("index", help="Rebuild catalog from metadata + filesystem")

    p_list = sub.add_parser("list", help="List all videos")
    p_list.add_argument("--tag", help="Filter by tag")

    p_search = sub.add_parser("search", help="Search titles, descriptions, and transcripts")
    p_search.add_argument("query", help="Search query")

    p_tag = sub.add_parser("tag", help="Add tags to a video")
    p_tag.add_argument("video_id", help="Video ID (or prefix)")
    p_tag.add_argument("tags", nargs="+", help="Tags to add")

    p_info = sub.add_parser("info", help="Show details for one video")
    p_info.add_argument("video_id", help="Video ID (or prefix)")

    sub.add_parser("export", help="Export catalog as CSV")

    args = parser.parse_args()

    dispatch = {
        "status": cmd_status,
        "index": cmd_index,
        "list": cmd_list,
        "search": cmd_search,
        "tag": cmd_tag,
        "info": cmd_info,
        "export": cmd_export,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
