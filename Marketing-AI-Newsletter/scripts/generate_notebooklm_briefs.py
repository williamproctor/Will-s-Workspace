#!/usr/bin/env python3
"""Generate NotebookLM podcast and video producer briefs from an approved edition.

Adapted from the AV newsletter's generator for this newsletter's section
structure and audience. Brand name is read from config.json.

Usage:
  python3 scripts/generate_notebooklm_briefs.py 2026-07-27 \
      --video-title "The Week AI Search Got a Price Tag"
  python3 scripts/generate_notebooklm_briefs.py 2026-07-27 --check

Generated briefs refresh automatically when their edition source changes.
Manually refined briefs (marker removed) are preserved unless --force is passed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
NEWSLETTER_ROOT = SCRIPT_DIR.parent
EDITIONS_DIR = NEWSLETTER_ROOT / "editions"
CONFIG_PATH = NEWSLETTER_ROOT / "config.json"
DEFAULT_OUTPUT_DIR = NEWSLETTER_ROOT / "notebooklm"
GENERATOR_VERSION = "1"
MARKER_RE = re.compile(
    r"<!-- notebooklm-brief-generator:v(?P<version>\d+) "
    r"source-sha256:(?P<digest>[0-9a-f]{64}) -->"
)
MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(https?://[^)]+\)")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(https?://[^)]+\)")
BARE_URL_RE = re.compile(r"https?://\S+")

STORY_SECTION = "This Week in Marketing AI"
WATCH_SECTION = "Platform & Tool Watch"
VOICES_SECTION = "Voices This Week"
THREADS_SECTION = "Common Threads"
ANGLES_SECTION = "Angles for the Week"
TIP_SECTION = "Tip of the Week"


@dataclass
class Subsection:
    title: str
    lines: list[str] = field(default_factory=list)


@dataclass
class Section:
    title: str
    intro: list[str] = field(default_factory=list)
    subsections: list[Subsection] = field(default_factory=list)


@dataclass
class Edition:
    title: str
    lede: list[str]
    sections: list[Section]

    def section(self, name: str) -> Section | None:
        target = name.casefold()
        return next(
            (section for section in self.sections if section.title.casefold() == target),
            None,
        )


def brand_name() -> str:
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8")).get("name", "the newsletter")
    except (OSError, json.JSONDecodeError):
        return "the newsletter"


def source_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_edition(text: str) -> Edition:
    title = ""
    lede: list[str] = []
    sections: list[Section] = []
    current_section: Section | None = None
    current_subsection: Subsection | None = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            continue
        if line.startswith("## "):
            current_section = Section(line[3:].strip())
            sections.append(current_section)
            current_subsection = None
            continue
        if line.startswith("### ") and current_section is not None:
            current_subsection = Subsection(line[4:].strip())
            current_section.subsections.append(current_subsection)
            continue
        if current_section is None:
            if line.startswith(">"):
                lede.append(line.lstrip("> ").strip())
            continue
        if current_subsection is not None:
            current_subsection.lines.append(line)
        else:
            current_section.intro.append(line)

    if not title:
        raise ValueError("Edition is missing its top-level '# ' title.")
    return Edition(title=title, lede=lede, sections=sections)


def clean_lines(lines: list[str]) -> str:
    cleaned: list[str] = []
    skip_source_continuation = False
    for raw in lines:
        stripped = raw.strip()
        if stripped == "---":
            continue
        if stripped.startswith("**Source:**") or stripped.startswith("**Source basis:**"):
            skip_source_continuation = True
            continue
        if skip_source_continuation:
            if not stripped:
                skip_source_continuation = False
            continue
        line = MARKDOWN_IMAGE_RE.sub(r"\1", raw.rstrip())
        line = MARKDOWN_LINK_RE.sub(r"\1", line)
        line = BARE_URL_RE.sub("", line).rstrip()
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def first_paragraph(lines: list[str]) -> str:
    paragraphs = re.split(r"\n\s*\n", clean_lines(lines))
    return next((p.strip() for p in paragraphs if p.strip()), "")


def story_sections(edition: Edition) -> list[Subsection]:
    stories: list[Subsection] = []
    primary = edition.section(STORY_SECTION)
    if primary and primary.subsections:
        stories.extend(primary.subsections)

    if not stories:
        for name in ("The Big Story", "Other Stories"):
            section = edition.section(name)
            if section:
                stories.extend(section.subsections)

    watch = edition.section(WATCH_SECTION)
    if watch:
        watch_body = clean_lines(watch.intro)
        if watch_body:
            stories.append(Subsection(WATCH_SECTION, watch.intro))

    return stories


def through_line(edition: Edition) -> tuple[str, str]:
    common = edition.section(THREADS_SECTION)
    if common and common.subsections:
        first = common.subsections[0]
        return first.title, first_paragraph(first.lines)
    if edition.lede:
        lede = " ".join(edition.lede)
        first_sentence = re.split(r"(?<=[.!?])\s+", lede)[0]
        return "The week's central pattern", first_sentence
    return (
        "The week's central pattern",
        "AI is rewiring how marketing gets discovered, bought, and measured.",
    )


def format_story(subsection: Subsection) -> str:
    body = clean_lines(subsection.lines)
    return f"### {subsection.title}\n\n{body}".strip()


def render_section(section: Section | None) -> str:
    if not section:
        return ""
    blocks: list[str] = []
    intro = clean_lines(section.intro)
    if intro:
        blocks.append(intro)
    blocks.extend(format_story(sub) for sub in section.subsections)
    return "\n\n".join(blocks).strip()


def infer_video_title(edition: Edition) -> str:
    title, _ = through_line(edition)
    return title[:90].rstrip(" .")


def audience_block() -> str:
    return """## Audience and house style

The audience is the GrowthX team: growth marketers, content strategists, and operators who publish publicly and advise clients on AI-era marketing.

- Keep the conversation professional, concrete, and anti-hype. These are practitioners, not beginners.
- Attribute quotations to the named person, not to a publication or show.
- Treat vendor and company performance figures as claims from those organizations. Preserve qualifiers such as "company-reported," "vendor-stated," "panel estimate," "preview," and "planned."
- Use the exact names, dates, prices, percentages, and measurements stated below.
- The angles segment offers starting points for the team's own posts and points of view; present them as raw material grounded in the week's reporting, not as instructions.
- Never mention this brief or its instructions during the episode."""


def render_podcast(edition: Edition, slug: str, display_date: str, digest: str) -> str:
    name = brand_name()
    stories = story_sections(edition)
    if not stories:
        raise ValueError("Edition has no story subsections to place in the brief.")

    through_title, through_body = through_line(edition)
    lead, supporting = stories[0], stories[1:]
    voices = render_section(edition.section(VOICES_SECTION))
    common = render_section(edition.section(THREADS_SECTION))
    angles = render_section(edition.section(ANGLES_SECTION))
    tip = render_section(edition.section(TIP_SECTION))

    supporting_block = "\n\n".join(format_story(story) for story in supporting)
    blocks = [
        f"<!-- notebooklm-brief-generator:v{GENERATOR_VERSION} source-sha256:{digest} -->",
        f"# {name} — Audio Producer Brief — Week of {display_date}",
        (
            f"This is the sole source for this week's {name} audio briefing. "
            "It contains the approved facts in the order the conversation should follow."
        ),
        audience_block(),
        f"""## Episode through-line

The central pattern is **{through_title}**. {through_body}

Establish that pattern near the beginning, connect the supporting stories back to it, and return to it before the closing segments.""",
        f"""## Act One — Lead story

The most important story this week is **{lead.title}**. Give it the most discussion time.

{clean_lines(lead.lines)}""",
    ]

    if supporting_block:
        blocks.append(
            f"""## Act Two — Supporting stories

The following stories broaden the week's pattern. Keep them in this order.

{supporting_block}"""
        )
    if voices:
        blocks.append(f"## Voices and attributed quotations\n\n{voices}")
    if common:
        blocks.append(f"## Common threads to connect\n\n{common}")
    if angles:
        blocks.append(
            f"""## Closing segment one — Angles for the week

Present these as grounded starting points the team can shape into posts and points of view. Keep each angle tied to the facts that support it.

{angles}"""
        )
    if tip:
        blocks.append(
            f"""## Closing segment two — Tip of the week

Give the practical closing tip enough room to be useful, with its concrete steps intact.

{tip}"""
        )
    blocks.append(
        f"""## Accuracy check

- This brief was generated from the approved full edition for {slug}.
- Preserve qualifiers such as "company-reported," "vendor-stated," "panel estimate," "preview," and "planned."
- Do not turn a preview into an available product or a reported claim into an independently measured result.
- Keep all numerical comparisons attached to the organization that reported them."""
    )
    return "\n\n---\n\n".join(blocks).strip() + "\n"


def render_video(
    edition: Edition, slug: str, display_date: str, digest: str, video_title: str
) -> str:
    name = brand_name()
    stories = story_sections(edition)
    if not stories:
        raise ValueError("Edition has no story subsections to place in the brief.")

    through_title, through_body = through_line(edition)
    lead, supporting = stories[0], stories[1:]
    common = render_section(edition.section(THREADS_SECTION))
    angles = render_section(edition.section(ANGLES_SECTION))
    tip = render_section(edition.section(TIP_SECTION))
    supporting_block = "\n\n".join(format_story(story) for story in supporting)

    blocks = [
        f"<!-- notebooklm-brief-generator:v{GENERATOR_VERSION} source-sha256:{digest} -->",
        f"# {name} — Video Producer Brief — Week of {display_date}",
        (
            f"This is the sole source for a five-to-seven-minute {name} video briefing. "
            "It contains approved narration facts and the intended visual sequence."
        ),
        f'**Suggested episode title: "{video_title}."**',
        """## Audience, narration, and visual style

The audience is the GrowthX team: growth marketers, content strategists, and operators who publish publicly and advise clients on AI-era marketing.

- Keep narration professional, observational, concise, and anti-hype.
- Attribute quotations and label company-reported or vendor-stated figures.
- Never mention this brief or its instructions in narration.
- Put important dates, product names, and numerical comparisons on screen.
- Use a clean editorial visual style: warm off-white backgrounds, dark ink typography, one gold accent, flat 2D vector graphics, generous negative space, monospace labels for data.
- Avoid neon, glow effects, three-dimensional renders, and futuristic interface imagery.""",
        f"""## Segment 1 — Cold open and thesis

Open with the week and episode title, then establish this idea:

**{through_title}.**

{through_body}

On screen: "{video_title}" and "Week of {display_date}".""",
        f"""## Segment 2 — Lead story

Give this segment the most time. Show the story title and every important date or numerical comparison exactly as stated.

### {lead.title}

{clean_lines(lead.lines)}""",
    ]
    if supporting_block:
        blocks.append(
            f"""## Segment 3 — Supporting stories

Keep these stories in order. Use one concise visual card per story, with short on-screen labels rather than dense paragraphs.

{supporting_block}"""
        )
    pattern_parts = [part for part in (common, angles) if part]
    if pattern_parts:
        blocks.append(
            "## Segment 4 — Connect the pattern and the angles\n\n" + "\n\n".join(pattern_parts)
        )
    if tip:
        blocks.append(
            f"""## Segment 5 — Tip and close

Present the tip as practical information with its concrete steps.

{tip}

Close by returning to the episode title and the week's central pattern."""
        )
    blocks.append(
        f"""## Accuracy and screen-text check

- This brief was generated from the approved full edition for {slug}.
- Preserve qualifiers such as "company-reported," "vendor-stated," "panel estimate," "preview," and "planned."
- Keep every on-screen number attached to the correct company and task.
- Do not show URLs, source-document instructions, or unsupported claims on screen."""
    )
    return "\n\n---\n\n".join(blocks).strip() + "\n"


def write_managed(path: Path, content: str, digest: str, force: bool) -> str:
    if not path.exists():
        path.write_text(content, encoding="utf-8")
        return "created"

    existing = path.read_text(encoding="utf-8")
    marker = MARKER_RE.search(existing)
    if force or marker:
        if not force and marker and marker.group("digest") == digest:
            return "current"
        path.write_text(content, encoding="utf-8")
        return "refreshed"

    return "preserved manual brief"


def validate_brief(path: Path, source: Path, digest: str, kind: str) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing {path}"]

    text = path.read_text(encoding="utf-8")
    if len(text) < 1_000:
        errors.append(f"{path.name} is unexpectedly short")
    if "GrowthX team" not in text:
        errors.append(f"{path.name} is missing the audience context")
    if kind == "podcast" and "through-line" not in text.casefold():
        errors.append(f"{path.name} is missing a through-line")
    if kind == "video" and "Suggested episode title:" not in text:
        errors.append(f"{path.name} is missing a suggested episode title")
    if "http://" in text or "https://" in text:
        errors.append(f"{path.name} contains URLs that NotebookLM may read aloud")

    marker = MARKER_RE.search(text)
    if marker and marker.group("digest") != digest:
        errors.append(f"{path.name} was generated from an older edition source")
    elif not marker and path.stat().st_mtime < source.stat().st_mtime:
        errors.append(
            f"{path.name} is manually managed but older than {source.name}; review it"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Edition date in YYYY-MM-DD format.")
    parser.add_argument(
        "--video-title",
        help="Suggested video title. Defaults to the first Common Threads heading.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory (defaults to notebooklm/).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite manually refined briefs as well as generated briefs.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate existing briefs without generating them.",
    )
    args = parser.parse_args()

    try:
        parsed_date = datetime.strptime(args.slug, "%Y-%m-%d")
    except ValueError as exc:
        parser.error(str(exc))

    source = EDITIONS_DIR / f"{args.slug}.md"
    if not source.exists():
        parser.error(f"Edition source does not exist: {source}")

    source_text = source.read_text(encoding="utf-8")
    digest = source_digest(source_text)
    edition = parse_edition(source_text)
    display_date = f"{parsed_date.strftime('%B')} {parsed_date.day}, {parsed_date.year}"
    video_title = args.video_title or infer_video_title(edition)
    output_dir = args.output_dir.expanduser().resolve()
    podcast_path = output_dir / f"{args.slug}-podcast.md"
    video_path = output_dir / f"{args.slug}-video.md"

    if not args.check:
        output_dir.mkdir(parents=True, exist_ok=True)
        podcast = render_podcast(edition, args.slug, display_date, digest)
        video = render_video(edition, args.slug, display_date, digest, video_title)
        print(f"{write_managed(podcast_path, podcast, digest, args.force):>24}: {podcast_path}")
        print(f"{write_managed(video_path, video, digest, args.force):>24}: {video_path}")

    errors = [
        *validate_brief(podcast_path, source, digest, "podcast"),
        *validate_brief(video_path, source, digest, "video"),
    ]
    if errors:
        print("NotebookLM brief validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"NotebookLM briefs valid for {args.slug}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
