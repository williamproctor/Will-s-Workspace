"""
Build with Intent — Full Storyboard Regeneration
=================================================
Spatial Geography (locked for every interior shot):

    PLAN VIEW — looking down from ceiling

    ┌─────────────────────────────────────────────────────┐
    │                  GLASS PARTITION WALL                │
    │  ┌──────────────┐  AISLE  ┌──────────────┐         │
    │  │  DESIGNER     │ ~~~~~~~ │  DEVELOPER    │         │
    │  │  (SCREEN L)   │ 3 ft   │  (SCREEN R)   │         │
    │  │  BLACK        │ cubicle │  GRAY HOODIE  │         │
    │  │  TURTLENECK   │  wall   │  GRAPHIC TEE  │         │
    │  │  minimal desk │         │  chaotic desk │         │
    │  │  one monitor  │         │  three monitors│        │
    │  │  succulent    │         │  energy drinks │         │
    │  └──────────────┘         └──────────────┘         │
    │                    AISLE                             │
    │                  (PM enters from far end)            │
    │  ┌─────────────────────────────────────────────┐    │
    │  │  LARGE WINDOWS — city skyline beyond         │    │
    │  │  (golden light enters here in Act II/III)    │    │
    │  └─────────────────────────────────────────────┘    │
    └─────────────────────────────────────────────────────┘

    Designer sits FACING LEFT (his monitor is in front of him, we see
    the back of the cubicle wall behind his monitor).
    Developer sits FACING RIGHT (his monitors are in front of him,
    back of the cubicle wall behind his monitors).
    They are BACK-TO-BACK — their chairs almost touch across the
    low cubicle divider.

Camera Positions (named for consistency):
    CAM-A: Front of Designer — we see Designer face-on, his minimal
           desk, monitor, succulent. Cubicle wall visible behind him.
           Developer's desk/monitors might peek over the cubicle wall
           in the deep background, but blurred.
    CAM-B: Front of Developer — mirror of CAM-A. We see Developer
           face-on, his chaotic desk, three monitors, energy drinks.
           Cubicle wall behind him; Designer's setup barely visible
           over the wall in deep BG, blurred.
    CAM-C: Side angle — perpendicular to the cubicle wall. Shows
           both desks in profile. Cubicle wall is a vertical divider
           in the center of frame. Designer on left, Developer on right.
    CAM-D: Aisle POV — PM's walk-up. Looking down the aisle between
           rows of desks. Designer visible on one side, Developer on
           the other.
    CAM-E: OTS Designer — over Designer's right shoulder, looking at
           his screen. We see his turtleneck collar and the edge of
           his head. Shallow DOF, screen sharp.
    CAM-F: OTS Developer — over Developer's left shoulder, looking at
           his screens. We see his hoodie and curly hair. Shallow DOF,
           screens sharp.
    CAM-G: The Reveal Wide — pulled back to show both desks, the
           cubicle wall between them, and PM standing in the aisle.
           The spatial punchline.
"""

import os
import sys
import time
from io import BytesIO
from google import genai
from google.genai import types
from PIL import Image

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyClKp6-HYJ-uVuzufm30dAMh3_OaApPJiA")
MODEL = "gemini-3.1-flash-image-preview"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "storyboard")
PM_HEADSHOT = os.path.join(SCRIPT_DIR, "pm-headshot.png")

# ── CHARACTER LOCKS ──────────────────────────────────────────

DESIGNER = (
    "A caucasian male, early 30s, lean build, sharp angular jawline. "
    "Short dark brown hair neatly styled and swept to the left. Clean-shaven with at most "
    "very faint stubble. Wearing a FITTED BLACK TURTLENECK — this is his signature. "
    "No jewelry. Expression: dry deadpan confidence, Jemaine Clement energy. "
    "He is the EXACT same person in every single shot."
)

DEVELOPER = (
    "A caucasian male, late 20s, slightly stocky build. Curly/wavy LIGHT BROWN hair, "
    "noticeably longer and messier than the Designer's. Reddish-brown short beard or "
    "heavy stubble. Wearing a DARK CHARCOAL ZIP-UP HOODIE over a FADED VINTAGE GRAPHIC "
    "TEE (the tee's print is partially visible at the neckline). "
    "Expression: kinetic, fast-talking confidence. Martin Starr in Silicon Valley energy. "
    "He is the EXACT same person in every single shot."
)

PM = (
    "A caucasian male, mid-to-late 40s, lean angular face, prominent cheekbones, short "
    "cropped brownish hair with some gray, stubble. Wearing a GRAY BLAZER over a BLUE "
    "BUTTON-DOWN SHIRT, open collar. Holds a white ceramic coffee mug that prominently "
    "reads 'PRODUCT GUY' in large black sans-serif text. Warm, practical dad-energy. "
    "He is the EXACT same person in every single shot."
)

# ── SET LOCKS ────────────────────────────────────────────────

SET_CORE = (
    "LOCKED SET: A modern open-plan corporate office. Key architectural features that "
    "MUST appear in every interior shot: (1) Rectangular FLUORESCENT PANEL LIGHTS in a "
    "white drop-tile ceiling. (2) GLASS PARTITION WALLS with thin BLACK METAL FRAMES "
    "visible in the mid-ground or background. (3) LOW GRAY FABRIC-COVERED CUBICLE "
    "DIVIDERS (approximately waist-height when standing) separating adjacent desks. "
    "(4) WHITE LAMINATE DESKS with silver/chrome legs. (5) Polished CONCRETE FLOOR "
    "with a slight sheen. (6) A city skyline visible through large windows in the "
    "background. The overall space is clean, corporate, open — NOT a co-working loft, "
    "NOT a home office, NOT a space with exposed brick or wood."
)

SET_COOL = (
    SET_CORE + " COLOR GRADE: Cool, slightly desaturated. The fluorescent lights cast "
    "blue-gray tones. Think David Fincher corporate — sterile, precise, controlled. "
    "No warm light sources. The environment feels efficient but soulless."
)

SET_WARM = (
    SET_CORE + " COLOR GRADE: Same office but now WARM late-afternoon golden light "
    "streams through the large windows, mixing with the overhead fluorescents. The "
    "color temperature has shifted — warmer, more saturated, more human. The same "
    "sterile space now feels inviting. The architectural features are IDENTICAL to "
    "the cool version — same ceiling, same glass walls, same cubicles, same desks."
)

SET_EXTERIOR = (
    "LOCKED EXTERIOR SET: The courtyard/entrance area of the same office building. "
    "A BRICK PAVER WALKWAY leads from GLASS DOUBLE DOORS to a landscaped area with "
    "TRIMMED HEDGES and MATURE TREES. The glass facade of the building is visible "
    "behind them, with the fluorescent office interior visible through the glass. "
    "GOLDEN HOUR: The sun is low, casting long warm shadows and rich amber light. "
    "Lens flare is welcome. The world outside feels alive compared to the office."
)

# ── SPATIAL GEOGRAPHY (included in every interior prompt) ────

SPATIAL_DESIGNER_SIDE = (
    "SPATIAL LOCK: The Designer's desk is on the LEFT side of a low cubicle wall. "
    "His setup: one large monitor centered on a white desk, a small succulent plant "
    "to the right of the monitor, one pen aligned parallel to the keyboard, nothing "
    "else. The desk surface is aggressively minimal. Behind him (on the OTHER side of "
    "the cubicle wall, partially visible over the top) is the Developer's chaotic setup "
    "— the tops of multiple monitors and stacked energy drink cans may peek over the "
    "low wall, BLURRED in the background."
)

SPATIAL_DEVELOPER_SIDE = (
    "SPATIAL LOCK: The Developer's desk is on the RIGHT side of the same low cubicle "
    "wall. His setup: THREE monitors (one laptop, two external displays) on a white desk "
    "COVERED in clutter — stacked energy drink cans (Monster, Red Bull), a rubber duck "
    "perched on the center monitor, Funko pops, sticker-covered laptop, tangled cables, "
    "a coffee mug. The desk is beautiful organized chaos. Behind him (on the OTHER side "
    "of the cubicle wall, partially visible over the top) is the Designer's minimal "
    "setup — the top of his single monitor and succulent may peek over the low wall, "
    "BLURRED in the background."
)

SPATIAL_BOTH = (
    "SPATIAL LOCK: Two adjacent desks separated by a LOW GRAY CUBICLE DIVIDER (waist "
    "height). LEFT desk: Designer's minimal setup — one monitor, one succulent, one pen. "
    "RIGHT desk: Developer's chaotic setup — three monitors, energy drinks stacked, "
    "rubber duck, stickers, cables. The cubicle wall runs horizontally through the "
    "CENTER of the frame. The two desks face AWAY from each other (back-to-back), "
    "so from this side angle the Designer faces LEFT and the Developer faces RIGHT."
)


# ── SHOT DEFINITIONS ─────────────────────────────────────────

SHOTS = [
    # ═══════════════════════════════════════════════════════
    # ACT I — THE PROBLEM (Cool grade, comedy)
    # ═══════════════════════════════════════════════════════
    {
        "num": "01",
        "name": "Designer — Establishing Wide",
        "refs": [],
        "prompt": (
            "CAMERA POSITION CAM-A: Locked-off, symmetrical WIDE SHOT facing the Designer "
            "head-on. " + DESIGNER + " He sits at his desk centered in frame, speaking "
            "directly to camera with deadpan confidence. "
            + SPATIAL_DESIGNER_SIDE + " " + SET_COOL +
            " Wes Anderson symmetry — the desk, monitor, and succulent form a perfectly "
            "balanced composition. Shallow depth of field: Designer sharp, the cubicle wall "
            "and anything beyond it (Developer's monitors peeking over) are softly blurred. "
            "16:9 aspect ratio. Subtle film grain. The stillness is deliberate."
        ),
    },
    {
        "num": "02",
        "name": "Designer's Screen — The Gorgeous Page",
        "refs": [],
        "prompt": (
            "CAMERA POSITION: MACRO INSERT — push-in past the Designer's shoulder to his "
            "monitor. The monitor fills 85% of the frame. We are looking at a gorgeous "
            "landing page: lush purple-blue gradient hero section, perfect sans-serif "
            "typography hierarchy, smooth layout with a prominent glowing CTA button that "
            "reads 'Get Started'. A HAND enters from the lower-left — it belongs to the "
            "Designer (we see the edge of his BLACK TURTLENECK sleeve). His INDEX FINGER "
            "extends toward the CTA button with theatrical deliberation. "
            "Shallow depth of field: screen sharp, everything else melted. "
            "The edge of the succulent plant is barely visible on the desk, "
            "confirming this is the Designer's station. "
            + SET_COOL +
            " 16:9, film grain. The confidence of the click is the comedy."
        ),
    },
    {
        "num": "04",
        "name": "Designer — The Pinky (Dr. Evil)",
        "refs": ["01"],
        "prompt": (
            "CAMERA POSITION CAM-A PUSHED IN: EXTREME CLOSE-UP of the Designer's face, "
            "filling the frame from chin to forehead. " + DESIGNER +
            " Same face as the reference image — IDENTICAL features, hair, stubble level. "
            "He slowly raises his PINKY FINGER to the corner of his lip in a subtle "
            "Dr. Evil gesture. Completely deadpan expression. No smile. Total commitment. "
            "BACKGROUND (out of focus): His monitor showing a white error page "
            "(localhost:3000 connection refused). The fluorescent panel lights on the "
            "ceiling are visible as soft bokeh rectangles above his head. "
            "16:9, film grain. The stillness IS the joke."
        ),
    },
    {
        "num": "05",
        "name": "Developer — Establishing Wide",
        "refs": [],
        "prompt": (
            "CAMERA POSITION CAM-B: Locked-off, symmetrical WIDE SHOT facing the Developer "
            "head-on — this is the EXACT MIRROR of the Designer's establishing shot. Same "
            "distance, same height, same lens, same symmetry. " + DEVELOPER +
            " He sits at his desk centered in frame, speaking to camera with kinetic "
            "confidence. " + SPATIAL_DEVELOPER_SIDE + " " + SET_COOL +
            " The energy drink towers, rubber duck, and sticker-covered laptop create "
            "organized chaos that contrasts the Designer's minimal desk — but the framing "
            "is IDENTICAL. The cubicle wall behind him has the Designer's minimal setup "
            "peeking over the top, blurred. 16:9, film grain."
        ),
    },
    {
        "num": "07",
        "name": "Developer — The Warning Toast",
        "refs": ["05"],
        "prompt": (
            "CAMERA POSITION CAM-B PUSHED IN: MEDIUM CLOSE-UP of the Developer at his "
            "chaotic desk. " + DEVELOPER + " Same face as the reference image — IDENTICAL "
            "features, curly hair, beard. His three monitors are visible: the center one "
            "shows a dense configuration UI (toggles, dropdowns, JSON panels), and a "
            "small orange WARNING TOAST notification has appeared in the upper-right "
            "corner of the screen. His expression: calm and completely unbothered. "
            "He either doesn't see it or has made peace with the chaos. "
            "Energy drink cans and rubber duck visible on the desk. "
            + SET_COOL +
            " 16:9, film grain. The quiet horror of someone at peace."
        ),
    },
    {
        "num": "08",
        "name": "PM Walks In — Aisle POV",
        "refs": ["pm", "01", "05"],
        "prompt": (
            "CAMERA POSITION CAM-D: WIDE SHOT from BEHIND the Product Manager as he walks "
            "down the CENTER AISLE of the office. We see his BACK and SHOULDERS in the "
            "lower-center foreground — he wears a GRAY BLAZER over a BLUE SHIRT, and holds "
            "a white 'PRODUCT GUY' coffee mug in his right hand at hip level. "
            "CRITICAL SPATIAL LAYOUT visible ahead of him: On the LEFT side of the aisle, "
            "we see the BACK of the Designer's head and the back of his monitor — he is "
            "in his BLACK TURTLENECK at his minimal desk with the succulent visible. "
            "On the RIGHT side of the aisle, we see the BACK of the Developer's head "
            "(curly hair) and the backs of his three monitors — energy drinks and clutter "
            "visible on his desk. The low CUBICLE WALL runs between them. They are "
            "BACK-TO-BACK, separated by the cubicle wall — but from this angle we see "
            "only their backs, so the proximity is not yet obvious. "
            "Slight HANDHELD CAMERA BOB for documentary feel. "
            + SET_COOL +
            " 16:9, film grain. The PM is about to discover the spatial punchline."
        ),
    },
    {
        "num": "09",
        "name": "The Reveal — Three Feet Apart",
        "refs": ["01", "05", "pm"],
        "prompt": (
            "CAMERA POSITION CAM-G: WIDE REVEAL SHOT — the camera has PULLED BACK and "
            "ROTATED to show the SIDE VIEW (CAM-C position). This is the SPATIAL PUNCHLINE. "
            "We now see the full geography: the Designer (LEFT, " + DESIGNER + ") and "
            "the Developer (RIGHT, " + DEVELOPER + ") are sitting at desks on OPPOSITE "
            "SIDES of the SAME low cubicle wall. They are literally THREE FEET APART. "
            "They have stood up from their chairs and now FACE EACH OTHER over the low "
            "cubicle divider, looking surprised. Between them, standing in the aisle, "
            "is the PM (" + PM + ") with his PRODUCT GUY mug, looking mildly amused. "
            "SPATIAL DETAILS: Designer's minimal desk (one monitor, succulent) on the "
            "left. Developer's chaotic desk (three monitors, energy drinks, rubber duck) "
            "on the right. The low gray cubicle wall in the exact center of the frame. "
            "Both men have RAISED EYEBROWS — synchronized dawning realization. "
            + SET_COOL +
            " SYMMETRICAL framing — the cubicle wall is the axis of symmetry. "
            "16:9, film grain. The comedy is in the spatial reveal."
        ),
    },

    # ═══════════════════════════════════════════════════════
    # ACT II — THE COLLABORATION (Warming grade, montage)
    # ═══════════════════════════════════════════════════════
    {
        "num": "10",
        "name": "Montage: Design System (OTS Designer)",
        "refs": ["01"],
        "prompt": (
            "CAMERA POSITION CAM-E: OVER-THE-SHOULDER from behind the Designer, looking "
            "at his screen. MACRO/INSERT feel — shallow depth of field, f/1.4. "
            "We see the back-right of his head (short dark hair) and his RIGHT SHOULDER "
            "(the collar and shoulder seam of his BLACK TURTLENECK are sharply visible in "
            "the foreground). His hands rest on a clean keyboard and trackpad. "
            "THE SCREEN (sharp, fills upper 2/3 of frame): A beautiful design system — "
            "type scale cascading down the left column (Heading 1 at 48px, Heading 2 at "
            "36px, Body at 16px), color token swatches in a grid with CSS variable names "
            "underneath, and a spacing scale with pixel increments. Clean, systematic, white "
            "background interface. "
            "BACKGROUND (soft bokeh): Over the low cubicle wall behind the monitor, we can "
            "barely make out the BLURRED shapes of the Developer's setup — the tops of "
            "his stacked energy drink cans and the edge of his monitors. This subtle detail "
            "confirms the spatial geography without drawing attention. "
            + SET_WARM +
            " 16:9, film grain. The screen is the star. Creative flow state."
        ),
    },
    {
        "num": "11",
        "name": "Montage: Project Scaffold (OTS Developer)",
        "refs": ["05"],
        "prompt": (
            "CAMERA POSITION CAM-F: OVER-THE-SHOULDER from behind the Developer, looking "
            "at his screens. MACRO/INSERT feel — shallow depth of field, f/1.4. "
            "We see the back-left of his head (curly/wavy LIGHT BROWN hair) and his LEFT "
            "SHOULDER (the hood and shoulder of his CHARCOAL HOODIE visible in the "
            "foreground). His hands move FAST on a MECHANICAL KEYBOARD. "
            "THE CENTER SCREEN (sharp): A terminal with green-on-black text — a project "
            "directory tree scaffolding in real-time: folders expanding, config files "
            "generating, 'Installing dependencies...' text scrolling. "
            "LEFT SCREEN: Syntax-highlighted code (dark theme, blue/orange/green tokens). "
            "RIGHT SCREEN: API documentation page. "
            "DESK: Energy drink cans (Monster green, Red Bull blue/silver) visible next "
            "to the keyboard. Rubber duck perched on the center monitor's top bezel. "
            "BACKGROUND (soft bokeh): Over the low cubicle wall behind the monitors, the "
            "BLURRED shape of the Designer's single monitor and the tiny succulent are "
            "barely perceptible — maintaining spatial geography. "
            + SET_WARM +
            " 16:9, film grain. The energy of creation."
        ),
    },
    {
        "num": "13",
        "name": "Montage: The Nudge (Tight OTS Designer)",
        "refs": ["01"],
        "prompt": (
            "CAMERA POSITION CAM-E TIGHTER: Very TIGHT over-the-shoulder — almost a "
            "MACRO shot. The Designer's head (back/right side, short dark hair) and the "
            "collar of his BLACK TURTLENECK fill the left 30% of the frame, softly out "
            "of focus. The SCREEN fills the remaining 70%, SHARP. "
            "ON SCREEN: A bezier easing curve editor on a dark interface. A smooth "
            "S-curve with draggable control points. Numeric values in a panel to the "
            "right: cubic-bezier(0.4, 0.0, 0.2, 1.0). The faint REFLECTION of the "
            "Designer's face is visible in the glossy monitor surface — contemplative, "
            "precise, fine-tuning. "
            "His RIGHT HAND is on a trackpad, making a micro-adjustment. "
            + SET_WARM +
            " Extremely shallow DOF — the monitor reflection and the curve are the story. "
            "16:9, film grain. The precision of someone who cares about the last 5%."
        ),
    },
    {
        "num": "14",
        "name": "Montage: Design→Code Convergence (Side Angle)",
        "refs": ["01", "05"],
        "prompt": (
            "CAMERA POSITION CAM-C: SIDE ANGLE — the camera is PERPENDICULAR to the "
            "cubicle wall, shooting across both desks. The LOW CUBICLE DIVIDER runs "
            "vertically through the CENTER of the frame. "
            "LEFT SIDE: The Designer's monitor shows a DESIGN INTERFACE — a hero section "
            "mockup with a bold headline, subtitle text, and a gradient CTA button on a "
            "white canvas. The Designer (" + DESIGNER + ") is visible at the far left "
            "edge of frame, in profile, looking at his screen. His BLACK TURTLENECK is "
            "unmistakable. The succulent sits on his desk. "
            "RIGHT SIDE: The Developer's center monitor shows a CODE EDITOR — dark "
            "background with syntax-highlighted JSX/React code that corresponds to the "
            "same hero section visible on the Designer's screen. The Developer "
            "(" + DEVELOPER + ") is visible at the far right edge of frame, in profile, "
            "looking at his screen. His HOODIE and curly hair are unmistakable. Energy "
            "drink cans are on his desk. "
            "The TWO SCREENS are the heroes of this frame — showing the same product "
            "from design and code perspectives, separated only by the cubicle wall. "
            "The CUBICLE WALL that once divided them now CONNECTS them visually. "
            + SET_WARM +
            " 16:9, film grain. Shallow DOF on the screens, characters soft."
        ),
    },
    {
        "num": "15",
        "name": "Montage: Musical Peak (Wide Convergence)",
        "refs": ["01", "05"],
        "prompt": (
            "CAMERA POSITION CAM-C WIDE: WIDE SHOT from the same side angle as shot 14, "
            "but PULLED BACK to include more of both setups. The cubicle wall divides "
            "the frame vertically at center. "
            "LEFT: The Designer (" + DESIGNER + ") sits at his minimal desk. His monitor "
            "shows a polished, complete product page — beautiful typography, hero image, "
            "feature cards, gradient CTA button. The succulent and single pen are visible. "
            "RIGHT: The Developer (" + DEVELOPER + ") sits at his chaotic desk. His "
            "center monitor shows code that mirrors the design. His energy drinks, rubber "
            "duck, and sticker-covered laptop are all visible. "
            "BOTH are leaning slightly forward — in the flow. The two screens almost "
            "MIRROR each other across the cubicle wall. Design and code showing the same "
            "product. The lighting is the WARMEST it has been — rich golden afternoon "
            "light through the windows filling the space. "
            + SET_WARM +
            " 16:9, film grain. This is the visual and musical peak of the collaboration."
        ),
    },
    {
        "num": "16",
        "name": "The Ship — Leaning Back",
        "refs": ["01", "05"],
        "prompt": (
            "CAMERA POSITION CAM-C: SAME SIDE ANGLE as shots 14 and 15 — maintaining "
            "the exact same camera position and framing. The cubicle wall divides the "
            "frame vertically at center. "
            "LEFT: The Designer (" + DESIGNER + ") has LEANED BACK in his chair, arms "
            "relaxed, a subtle satisfied half-smile. His eyes are half-closed. Done. "
            "His minimal desk with the succulent is visible. "
            "RIGHT: The Developer (" + DEVELOPER + ") has ALSO LEANED BACK in his chair, "
            "hands behind his head, a matching satisfied expression. Done. His chaotic "
            "desk with energy drinks is visible. "
            "They are MIRROR IMAGES of relaxation, separated by the cubicle wall that now "
            "feels like a bridge rather than a barrier. The quiet confidence of people who "
            "know they shipped something good. No high-five. Just an exhale. "
            + SET_WARM +
            " The lighting is warm and golden. 16:9, film grain. Stillness after momentum."
        ),
    },

    # ═══════════════════════════════════════════════════════
    # ACT III — THE RESOLUTION (Golden hour, warmth)
    # ═══════════════════════════════════════════════════════
    {
        "num": "17",
        "name": "The Walk-Off (Exterior Wide)",
        "refs": ["01", "05"],
        "prompt": (
            "CAMERA POSITION: EXTERIOR WIDE, slightly behind and to the right. "
            "TRACKING SHOT feel. The Designer (" + DESIGNER + ") and Developer "
            "(" + DEVELOPER + ") walk together along a brick paver walkway, having "
            "just exited through glass double doors. They are mid-conversation and "
            "genuinely LAUGHING — body language is easy, friendly. They look like "
            "friends, not coworkers. No laptops in sight. "
            "The Designer (LEFT) wears his black turtleneck. The Developer (RIGHT) "
            "wears his charcoal hoodie over a graphic tee. Their contrasting wardrobes "
            "remain consistent even outdoors. "
            + SET_EXTERIOR +
            " Rich lens flare from the low sun. 16:9, film grain. The warmth is earned."
        ),
    },
    {
        "num": "18",
        "name": "PM at the Window — FOMO",
        "refs": ["pm"],
        "prompt": (
            "CAMERA POSITION: INTERIOR looking OUT through the office's large window. "
            "The PM (" + PM + ") is in the RIGHT THIRD of frame, shot from a three-quarter "
            "angle. He stands inside the office looking out through the glass at the "
            "courtyard where the Designer and Developer are walking away (visible as small "
            "SILHOUETTES through the window glass — one in dark clothing, one in lighter). "
            "His 'PRODUCT GUY' mug is PROMINENT in frame — held at chest height. "
            "A flash of FOMO crosses his face — mouth slightly open, eyebrows up. "
            "INTERIOR: Cool fluorescent office light on the PM. "
            "EXTERIOR (through glass): Warm golden hour light on the courtyard. "
            "The contrast between interior coolness and exterior warmth is the visual joke. "
            "16:9, film grain. Physical comedy setup."
        ),
    },
    {
        "num": "19",
        "name": "They Don't Stop (Exterior, backs to camera)",
        "refs": ["01", "05"],
        "prompt": (
            "CAMERA POSITION: EXTERIOR, BEHIND the Designer and Developer as they walk "
            "AWAY from camera. Their backs fill the lower half of the frame. "
            "Designer (LEFT) — the back of his BLACK TURTLENECK and dark hair visible. "
            "Developer (RIGHT) — the back of his CHARCOAL HOODIE and curly hair visible. "
            "They are mid-stride, relaxed, not stopping for anyone. The brick walkway "
            "leads toward trees and the setting sun. "
            + SET_EXTERIOR +
            " They fill the frame confidently. They heard someone call them. They don't "
            "care. 16:9, film grain. Quiet confidence."
        ),
    },
    {
        "num": "20",
        "name": "PM Running After",
        "refs": ["pm"],
        "prompt": (
            "CAMERA POSITION: EXTERIOR MEDIUM SHOT. The PM (" + PM + ") has burst through "
            "the glass double doors and is JOGGING along the brick walkway, slightly out "
            "of breath. He holds his 'PRODUCT GUY' mug in his right hand while jogging — "
            "coffee threatening to spill. His gray blazer flaps as he moves. "
            "In the BACKGROUND: The Designer and Developer are small figures further "
            "down the walkway, still not stopping, walking into the golden sunset. "
            "One wears dark clothing (Designer), the other lighter (Developer). "
            + SET_EXTERIOR +
            " 16:9, film grain. Physical comedy — chasing people who aren't waiting."
        ),
    },
    {
        "num": "22",
        "name": "End Card — Static",
        "refs": [],
        "prompt": (
            "Minimalist black background. Centered clean white text in a modern sans-serif "
            "font reading 'Build with Intent.' — the word 'Intent' is in a distinctive "
            "green color (#3ecf8e / mint green). Below in smaller muted gray text with wide "
            "letter-spacing: 'intent.augmentcode.com'. Clean cinematic end card. 16:9 "
            "aspect ratio. Subtle film grain. Premium, restrained."
        ),
    },
]


def load_img(path):
    full = os.path.join(SCRIPT_DIR, path) if not os.path.isabs(path) else path
    if not os.path.exists(full):
        full = os.path.join(OUTPUT_DIR, path)
    if os.path.exists(full):
        return Image.open(full)
    return None


def ref_label(path):
    if "pm-headshot" in path:
        return "PM headshot — match this face exactly."
    if "shot-01" in path:
        return "Designer reference — match this man's face, hair, turtleneck, and lean build exactly."
    if "shot-05" in path:
        return "Developer reference — match this man's curly hair, beard, hoodie, and stocky build exactly."
    return "Visual consistency reference."


def generate_shot(shot, client, attempt=1, max_attempts=3):
    num = shot["num"]
    out = os.path.join(OUTPUT_DIR, f"shot-{num}.png")

    if os.path.exists(out) and attempt == 1:
        print(f"  [SKIP] shot-{num}.png exists")
        return True

    print(f"  [{attempt}/{max_attempts}] shot-{num}: {shot['name']}...")

    contents = []
    labels = []

    for ref in shot.get("refs", []):
        if ref == "pm":
            img = load_img(PM_HEADSHOT)
        else:
            img = load_img(f"shot-{ref}.png")

        if img:
            path_str = PM_HEADSHOT if ref == "pm" else f"shot-{ref}.png"
            labels.append(ref_label(path_str))
            contents.append(img)
        else:
            print(f"    [WARN] Reference '{ref}' not found")

    preamble = ""
    if labels:
        preamble = "REFERENCE IMAGES: " + " ".join(
            f"Image {i+1}: {l}" for i, l in enumerate(labels)
        ) + " "

    contents.insert(0, preamble + shot["prompt"])

    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=types.GenerateContentConfig(response_modalities=["IMAGE", "TEXT"]),
        )
        for part in resp.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                img = Image.open(BytesIO(part.inline_data.data))
                img.save(out)
                print(f"  [OK] shot-{num}.png ({img.size[0]}x{img.size[1]})")
                return True

        print(f"  [WARN] No image returned for shot-{num}")
    except Exception as e:
        print(f"  [ERR] shot-{num}: {e}")

    if attempt < max_attempts:
        wait = 5 * attempt
        print(f"  Retrying in {wait}s...")
        time.sleep(wait)
        return generate_shot(shot, client, attempt + 1, max_attempts)

    return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = genai.Client(api_key=API_KEY)

    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    if only:
        print(f"Generating only: {', '.join(sorted(only))}")

    ok, fail = 0, []
    for shot in SHOTS:
        if only and shot["num"] not in only:
            continue
        if generate_shot(shot, client):
            ok += 1
        else:
            fail.append(shot["num"])
        time.sleep(3)

    print(f"\n{'='*40}")
    print(f"Generated {ok}/{ok + len(fail)} shots")
    if fail:
        print(f"Failed: {', '.join(fail)}")


if __name__ == "__main__":
    main()
