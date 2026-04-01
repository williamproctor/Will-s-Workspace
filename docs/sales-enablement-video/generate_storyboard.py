#!/usr/bin/env python3
"""
Generate storyboard frames for the GrowthX Sales Enablement Video.

Usage:
    export GEMINI_API_KEY="your-key-here"
    python generate_storyboard.py

    # Regenerate specific shots:
    python generate_storyboard.py --shots 03 04 10

    # Use a reference headshot for character consistency:
    python generate_storyboard.py --headshot matthew-headshot.png
"""

import argparse
import io
import os
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
    from PIL import Image
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install google-genai Pillow")
    sys.exit(1)


STORYBOARD_DIR = Path(__file__).parent / "storyboard"

MATTHEW_CHARACTER = (
    "same man from the reference photo — middle-aged, grey-brown hair, "
    "clean professional appearance, wearing a premium dark crew neck or button-down, "
    "warm and confident expression, the gravitas of someone who ran a major publication"
)

MATTHEW_SET = (
    "modern bright workspace with large windows and natural daylight, "
    "clean minimalist interior, warm tones, shallow depth of field with "
    "soft bright bokeh background, premium brand film lighting"
)

SHOTS = [
    {
        "num": "01",
        "prompt": (
            "Minimalist title card on warm cream background (#faf9f6), "
            "the word 'GrowthX' in bold black sans-serif typography centered in frame, "
            "clean and modern, premium SaaS brand aesthetic, 16:9 aspect ratio, "
            "no other elements, the confidence of a brand that doesn't need to explain itself"
        ),
        "needs_character": False,
    },
    {
        "num": "02",
        "prompt": (
            "Cinematic medium close-up of {CHARACTER} sitting in {SET}, "
            "looking slightly off-camera to the left in conversational posture, "
            "soft natural key light, 85mm equivalent lens, 16:9, "
            "premium brand film aesthetic, confidence and warmth"
        ),
        "needs_character": True,
    },
    {
        "num": "03",
        "prompt": (
            "Clean data visualization on dark background (#1a1a1a), two animated line charts — "
            "one curving upward exponentially labeled 'Content Demand' in cream white, "
            "another growing slowly linearly labeled 'Team Capacity', the gap between them "
            "widening dramatically, minimal modern typography, no grid lines, no clutter, "
            "premium data visualization aesthetic, 16:9, the kind of chart that makes a CMO uncomfortable"
        ),
        "needs_character": False,
    },
    {
        "num": "04",
        "prompt": (
            "Clean horizontal timeline infographic on dark background, showing four milestones "
            "spanning years 1 through 4 of building content operations in-house, each milestone "
            "labeled in cream white sans-serif typography, the timeline stretches impossibly long "
            "across the frame, small annotation at the end reading 'If nothing breaks' in muted grey, "
            "modern minimal design, 16:9, premium brand film graphic"
        ),
        "needs_character": False,
    },
    {
        "num": "05",
        "prompt": (
            "Cinematic medium close-up of {CHARACTER} in {SET}, "
            "the expression has shifted from setting up a problem to sharing something personal — "
            "a quiet conviction, the look of someone who has finally built the thing they always "
            "wanted to build, shallow depth of field, warm and bright, 16:9, premium brand film"
        ),
        "needs_character": True,
    },
    {
        "num": "07",
        "prompt": (
            "Close-up view of a workflow builder interface within a content operations platform, "
            "showing custom-configured nodes with labels like 'Competitor Analysis', "
            "'Audience Signals', 'Content Brief Generation', connected by flowing data lines, "
            "configuration panel open on the right showing parameters being customized, "
            "dark mode UI, modern design system, 16:9, the detail level communicates bespoke engineering"
        ),
        "needs_character": False,
    },
    {
        "num": "08",
        "prompt": (
            "Split-screen composition showing content transformation, left side showing raw data "
            "inputs in a terminal-style dark interface — market data tables, competitor URLs, "
            "search query lists — and right side showing a polished finished blog article with "
            "clean typography and formatting, the contrast between messy inputs and refined output, "
            "dark UI with cream accents, 16:9, premium SaaS product visualization"
        ),
        "needs_character": False,
    },
    {
        "num": "09",
        "prompt": (
            "Slightly tighter cinematic medium close-up of {CHARACTER} in {SET}, "
            "the expression communicating a shift from demonstration to deeper explanation, "
            "leaning slightly forward, engaged and direct, natural daylight, "
            "shallow depth of field, 16:9, the visual intimacy of someone sharing something important"
        ),
        "needs_character": True,
    },
    {
        "num": "10",
        "prompt": (
            "Animated data dashboard montage on dark background showing multiple growth metrics — "
            "organic traffic curve trending sharply upward, search ranking positions chart with "
            "green upward arrows, content output volume bar chart growing month over month, "
            "all rendered in clean modern data visualization style with cream white and green "
            "accent colors, 16:9, premium analytics aesthetic, the data tells a clear story of acceleration"
        ),
        "needs_character": False,
    },
    {
        "num": "11",
        "prompt": (
            "Clean animated flywheel diagram on dark background, four connected nodes in a circle — "
            "'Data', 'Content', 'Results', 'Strategy' — with glowing particles flowing between them "
            "in a continuous loop, each rotation visually faster than the last, minimal modern "
            "typography in cream white, subtle glow effects on the connecting paths, 16:9, "
            "the visual metaphor of a system that compounds, premium motion graphic aesthetic"
        ),
        "needs_character": False,
    },
    {
        "num": "12",
        "prompt": (
            "Cinematic medium close-up of {CHARACTER} in {SET}, "
            "calm and matter-of-fact expression — stating something obvious rather than making "
            "an argument, no dramatic energy, just quiet authority, shallow depth of field, "
            "warm and bright, 16:9, the visual equivalent of someone saying 'you know this already'"
        ),
        "needs_character": True,
    },
    {
        "num": "13",
        "prompt": (
            "Same man in bright workspace, now looking directly into camera for the first time — "
            "a subtle but meaningful shift from off-camera conversational gaze to direct eye contact, "
            "{CHARACTER}, "
            "the expression is warm and inviting, a slight smile forming, "
            "lighting slightly warmer than previous shots, shallow depth of field, 16:9, "
            "the visual moment of transition from explanation to invitation"
        ),
        "needs_character": True,
    },
    {
        "num": "14",
        "prompt": (
            "Cinematic medium close-up, direct eye contact with camera, "
            "{CHARACTER} in {SET}, "
            "the expression carries genuine personal conviction — this is not a rehearsed line "
            "but a belief, warm and confident, slight forward lean, shallow depth of field "
            "with bright bokeh, 16:9, the final frame should feel like an open door, not a closed pitch"
        ),
        "needs_character": True,
    },
    {
        "num": "15",
        "prompt": (
            "Wide view of a sophisticated content operations platform showing an active client "
            "workspace — multiple content pieces in various pipeline stages, activity feeds "
            "showing recent changes, performance metrics sidebar, dark mode interface with "
            "cream accents, 16:9, shown briefly like a glimpse behind a curtain, "
            "premium SaaS product visualization"
        ),
        "needs_character": False,
    },
    {
        "num": "16",
        "prompt": (
            "Minimalist end frame on warm cream background (#faf9f6), the GrowthX logo in bold "
            "black centered in frame, generous whitespace, no tagline no URL no CTA — just the "
            "brand mark, clean and confident, 16:9, "
            "the visual equivalent of a clean handshake before the conversation continues"
        ),
        "needs_character": False,
    },
]


def generate_frame(client, shot, headshot_img=None, reference_img=None):
    """Generate a single storyboard frame."""
    prompt = shot["prompt"]

    if shot["needs_character"]:
        prompt = prompt.replace("{CHARACTER}", MATTHEW_CHARACTER)
        prompt = prompt.replace("{SET}", MATTHEW_SET)

    contents = [prompt]

    if shot["needs_character"] and headshot_img:
        contents.append(headshot_img)
    if reference_img:
        contents.append(reference_img)

    print(f"  Generating shot {shot['num']}...")

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            img = Image.open(io.BytesIO(part.inline_data.data))
            output_path = STORYBOARD_DIR / f"shot-{shot['num']}.png"
            img.save(output_path)
            print(f"  ✓ Saved {output_path.name} ({img.size[0]}x{img.size[1]})")
            return output_path

    print(f"  ✗ No image generated for shot {shot['num']}")
    return None


def main():
    parser = argparse.ArgumentParser(description="Generate storyboard frames")
    parser.add_argument(
        "--shots",
        nargs="+",
        help="Specific shot numbers to generate (e.g., 03 04 10)",
    )
    parser.add_argument(
        "--headshot",
        type=str,
        help="Path to Matthew's headshot for character consistency",
    )
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: Set GEMINI_API_KEY environment variable")
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    STORYBOARD_DIR.mkdir(parents=True, exist_ok=True)

    headshot_img = None
    if args.headshot:
        headshot_path = Path(args.headshot)
        if headshot_path.exists():
            headshot_img = Image.open(headshot_path)
            print(f"Using headshot: {headshot_path}")
        else:
            print(f"Warning: Headshot not found at {headshot_path}")

    shots_to_generate = SHOTS
    if args.shots:
        target_nums = set(args.shots)
        shots_to_generate = [s for s in SHOTS if s["num"] in target_nums]
        if not shots_to_generate:
            print(f"No matching shots found for: {args.shots}")
            sys.exit(1)

    print(f"\nGenerating {len(shots_to_generate)} storyboard frames...")
    print(f"Output: {STORYBOARD_DIR}\n")

    reference_img = None

    for shot in shots_to_generate:
        result = generate_frame(client, shot, headshot_img, reference_img)

        if result and shot["num"] == "02" and shot["needs_character"]:
            reference_img = Image.open(result)
            print(f"  → Using shot 02 as character reference for subsequent shots")

    print(f"\nDone. {len(shots_to_generate)} frames generated in {STORYBOARD_DIR}/")


if __name__ == "__main__":
    main()
