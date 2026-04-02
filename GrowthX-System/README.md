# GrowthX System — Content Vault

Download, organize, and search Loom videos for the GrowthX content pipeline.

## Directory Structure

```
GrowthX-System/
├── content_vault/
│   ├── videos/loom/      ← downloaded MP4s (git-ignored)
│   ├── transcripts/       ← VTT/SRT subtitle files (git-ignored)
│   └── metadata/          ← per-video JSON sidecars
├── tools/
│   ├── loom_downloader.py ← download engine (yt-dlp + HTTP fallback)
│   └── vault_manager.py   ← catalog, search, tagging, export
├── requirements.txt
├── config.example.env
└── urls.example.txt       ← template for batch downloads
```

## Quick Start

```bash
cd GrowthX-System

# Install dependencies
pip install -r requirements.txt

# Download a single Loom video
python tools/loom_downloader.py https://www.loom.com/share/VIDEO_ID

# Batch download from a URL list
cp urls.example.txt urls.txt
# (paste your Loom URLs into urls.txt)
python tools/loom_downloader.py --batch urls.txt

# Check vault status
python tools/vault_manager.py status

# Rebuild the index after downloading
python tools/vault_manager.py index

# List all videos
python tools/vault_manager.py list

# Search across titles, descriptions, and transcripts
python tools/vault_manager.py search "sales enablement"
```

## Loom Downloader

The downloader uses **yt-dlp** (which has a native Loom extractor) as its primary engine. If yt-dlp is not installed, it falls back to scraping the Loom page for a CDN link and downloading with `requests`.

**What gets saved per video:**

| Artifact | Location | Committed to git? |
|---|---|---|
| MP4 video | `content_vault/videos/loom/{id}.mp4` | No (git-ignored) |
| VTT transcript | `content_vault/transcripts/{id}.en.vtt` | No |
| Metadata JSON | `content_vault/metadata/{id}.json` | **Yes** |

### Options

```
python tools/loom_downloader.py [OPTIONS] URL [URL ...]

  --batch FILE    Read URLs from a text file (one per line)
  --dry-run       Fetch metadata only, skip the video download
  --cookies FILE  Netscape cookies.txt for private videos
  -v, --verbose   Debug logging
```

### Private Videos

For Loom videos that require authentication, export your browser cookies as a Netscape `cookies.txt` file and pass them in:

```bash
python tools/loom_downloader.py --cookies cookies.txt https://www.loom.com/share/PRIVATE_ID
```

Or set the `LOOM_COOKIES` environment variable.

## Vault Manager

The vault manager indexes everything in the content vault into a single `catalog.json` and provides CLI commands for browsing and organizing.

### Commands

| Command | Description |
|---|---|
| `status` | Overview of vault contents (counts, total size, tags) |
| `index` | Rebuild `catalog.json` from metadata files + filesystem |
| `list [--tag TAG]` | List all videos, optionally filtered by tag |
| `search QUERY` | Full-text search across titles, descriptions, transcripts |
| `tag VIDEO_ID TAG [...]` | Add tags to a video |
| `info VIDEO_ID` | Print full metadata JSON for one video |
| `export` | Export the catalog as `catalog_export.csv` |

### Tagging

Tag videos to organize them by topic, project, or pipeline stage:

```bash
python tools/vault_manager.py tag abc123 sales-enablement matthew-panzarino
python tools/vault_manager.py list --tag sales-enablement
```

## Resuming Work

The downloader is **idempotent** — running it again with the same URL will skip already-downloaded videos. To pick up where you left off:

1. Add any new Loom URLs to `urls.txt`
2. Run `python tools/loom_downloader.py --batch urls.txt`
3. Run `python tools/vault_manager.py index` to update the catalog
