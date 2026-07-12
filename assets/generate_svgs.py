#!/usr/bin/env python3
"""Generate distinct SMIL SVG assets for cael1127 — aurora/orbit editorial (not school circuit)."""

from pathlib import Path
from math import cos, sin, pi

OUT = Path(__file__).resolve().parent
FONT_UI = "Georgia, 'Times New Roman', Times, serif"
FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# Aurora editorial — teal + slate (distinct from Aggie maroon and prior steel clone)
THEMES = {
    "dark": {
        "bg0": "#0d1117",
        "bg1": "#0f1419",
        "ink": "#f0f4f8",
        "muted": "#9fb0c0",
        "faint": "#6b7c8c",
        "accent": "#5eead4",
        "accent2": "#67e8f9",
        "glow": "#134e4a",
        "orbit": "#2dd4bf",
        "wave": "#5eead4",
        "star": "#ccfbf1",
        "line": "#1e3a3a",
        "soft": "#164e63",
    },
    "light": {
        "bg0": "#ffffff",
        "bg1": "#f7fafb",
        "ink": "#0f172a",
        "muted": "#475569",
        "faint": "#64748b",
        "accent": "#0f766e",
        "accent2": "#0891b2",
        "glow": "#ccfbf1",
        "orbit": "#0d9488",
        "wave": "#14b8a6",
        "star": "#0f766e",
        "line": "#cfe8e4",
        "soft": "#99f6e4",
    },
}


def aurora_defs(t: dict, w: int = 1280, h: int = 400) -> str:
    return f'''  <defs>
    <linearGradient id="sky" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="50%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg0']}"/>
    </linearGradient>
    <radialGradient id="auroraA" cx="28%" cy="40%" r="42%">
      <stop offset="0%" stop-color="{t['glow']}" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="{t['bg0']}" stop-opacity="0"/>
      <animate attributeName="cx" values="28%;34%;24%;28%" dur="22s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="40%;32%;46%;40%" dur="22s" repeatCount="indefinite"/>
    </radialGradient>
    <radialGradient id="auroraB" cx="72%" cy="55%" r="38%">
      <stop offset="0%" stop-color="{t['soft']}" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="{t['bg0']}" stop-opacity="0"/>
      <animate attributeName="cx" values="72%;66%;78%;72%" dur="26s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="55%;62%;48%;55%" dur="26s" repeatCount="indefinite"/>
    </radialGradient>
    <radialGradient id="auroraC" cx="50%" cy="20%" r="30%">
      <stop offset="0%" stop-color="{t['accent2']}" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="{t['bg0']}" stop-opacity="0"/>
      <animate attributeName="opacity" values="0.5;1;0.5" dur="10s" repeatCount="indefinite"/>
    </radialGradient>
    <linearGradient id="fadeY" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="10%" stop-color="white" stop-opacity="1"/>
      <stop offset="78%" stop-color="white" stop-opacity="1"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <mask id="pageBlend" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}">
      <rect width="{w}" height="{h}" fill="url(#fadeY)"/>
    </mask>
  </defs>
'''


def stars_layer(t: dict, count: int = 48, h: int = 400) -> str:
    lines = [f'  <g fill="{t["star"]}">']
    for i in range(count):
        x = (41 * i * i + 17 * i + 53) % 1240 + 20
        y = (29 * i + 11 * (i % 9) + 7) % (h - 40) + 20
        r = 0.5 + (i % 4) * 0.35
        op = 0.15 + (i % 5) * 0.08
        dur = 3.5 + (i % 7) * 0.55
        delay = (i % 12) * 0.25
        lines.append(f'''    <circle cx="{x}" cy="{y}" r="{r}" opacity="{op:.2f}">
      <animate attributeName="opacity" values="{op:.2f};{min(op + 0.45, 0.95):.2f};{op:.2f}" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>
    </circle>''')
    lines.append("  </g>")
    return "\n".join(lines) + "\n"


def orbits_layer(t: dict) -> str:
    # Right-side orbital system — signature mark, not school circuits
    cx, cy = 980, 200
    parts = [f'  <g fill="none" transform="translate(0,0)">']
    for i, (rx, ry, dur, op) in enumerate(
        [
            (90, 90, 28, 0.35),
            (130, 70, 36, 0.28),
            (170, 110, 44, 0.2),
        ]
    ):
        parts.append(f'''    <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" stroke="{t['orbit']}" stroke-width="1.1" opacity="{op}">
      <animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy}; 360 {cx} {cy}" dur="{dur}s" repeatCount="indefinite"/>
    </ellipse>''')
        # satellite dots
        angle = i * 40
        parts.append(f'''    <circle cx="{cx + rx}" cy="{cy}" r="3" fill="{t['accent']}" opacity="0.85">
      <animateTransform attributeName="transform" type="rotate" values="{angle} {cx} {cy}; {angle + 360} {cx} {cy}" dur="{dur * 0.7:.0f}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.4;1;0.4" dur="3s" begin="{i * 0.4}s" repeatCount="indefinite"/>
    </circle>''')
    parts.append(f'''    <circle cx="{cx}" cy="{cy}" r="8" fill="{t['accent']}" opacity="0.9">
      <animate attributeName="r" values="7;10;7" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="{cx}" cy="{cy}" r="18" fill="none" stroke="{t['accent2']}" stroke-width="1" opacity="0.35">
      <animate attributeName="r" values="16;24;16" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.4;0.08;0.4" dur="4s" repeatCount="indefinite"/>
    </circle>
  </g>''')
    return "\n".join(parts) + "\n"


def wave_path(y: int = 320, amp: int = 14, cycles: int = 3) -> str:
    pts = []
    for i in range(0, 1281, 8):
        t = i / 1280 * cycles * 2 * pi
        pts.append(f"{i},{y + amp * sin(t):.1f}")
    return "M" + " L".join(pts)


def waves_layer(t: dict) -> str:
    w1 = wave_path(310, 12, 2.5)
    w2 = wave_path(330, 8, 3.2)
    return f'''  <g fill="none" stroke-linecap="round">
    <path d="{w1}" stroke="{t['wave']}" stroke-width="1.5" opacity="0.45" stroke-dasharray="6 10">
      <animate attributeName="stroke-dashoffset" from="0" to="-80" dur="8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.25;0.55;0.25" dur="6s" repeatCount="indefinite"/>
    </path>
    <path d="{w2}" stroke="{t['accent2']}" stroke-width="1" opacity="0.3" stroke-dasharray="4 12">
      <animate attributeName="stroke-dashoffset" from="0" to="64" dur="10s" repeatCount="indefinite"/>
    </path>
  </g>
'''


def hero_text(t: dict) -> str:
    return f'''  <g>
    <text x="72" y="88" fill="{t['accent']}" font-family="{FONT_MONO}" font-size="12" font-weight="600" letter-spacing="3.5" opacity="0">
      SOFTWARE DEVELOPER
      <animate attributeName="opacity" from="0" to="1" begin="0.2s" dur="0.6s" fill="freeze"/>
    </text>
    <text x="72" y="168" fill="{t['ink']}" font-family="{FONT_UI}" font-size="64" font-weight="400" letter-spacing="-1.2" opacity="0">
      Cael Findley
      <animate attributeName="opacity" from="0" to="1" begin="0.5s" dur="0.9s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" values="0,16; 0,0" begin="0.5s" dur="0.9s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.22 1 0.36 1"/>
    </text>
    <text x="72" y="214" fill="{t['muted']}" font-family="{FONT_SANS}" font-size="17" opacity="0">
      AI systems · full-stack products · systems programming
      <animate attributeName="opacity" from="0" to="1" begin="1.2s" dur="0.7s" fill="freeze"/>
    </text>
    <text x="72" y="248" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="12" letter-spacing="1.5" opacity="0">
      Texas A&amp;M CS  ·  @cael1127
      <animate attributeName="opacity" from="0" to="1" begin="1.6s" dur="0.6s" fill="freeze"/>
    </text>
    <rect x="72" y="272" width="0" height="2" fill="{t['accent']}" rx="1" opacity="0.9">
      <animate attributeName="width" from="0" to="180" begin="2.0s" dur="1.1s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.4 0 0.2 1"/>
    </rect>
  </g>
'''


def header_svg(theme: str) -> str:
    t = THEMES[theme]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 400" width="1280" height="400" role="img" aria-labelledby="title desc">
  <title id="title">Cael Findley — Software Developer</title>
  <desc id="desc">Aurora and orbit animated banner for personal GitHub profile ({theme})</desc>
{aurora_defs(t, 1280, 400)}  <g mask="url(#pageBlend)">
  <rect width="1280" height="400" fill="url(#sky)"/>
  <rect width="1280" height="400" fill="url(#auroraA)"/>
  <rect width="1280" height="400" fill="url(#auroraB)"/>
  <rect width="1280" height="400" fill="url(#auroraC)"/>
{stars_layer(t, 52, 400)}{orbits_layer(t)}{waves_layer(t)}{hero_text(t)}  </g>
</svg>
'''


def footer_svg(theme: str) -> str:
    t = THEMES[theme]
    stars = []
    for i in range(24):
        x = 80 + i * 48
        delay = i * 0.15
        stars.append(f'''  <circle cx="{x}" cy="56" r="1.4" fill="{t['star']}" opacity="0.25">
    <animate attributeName="opacity" values="0.15;0.7;0.15" dur="3.2s" begin="{delay}s" repeatCount="indefinite"/>
    <animate attributeName="cy" values="48;64;48" dur="4.5s" begin="{delay}s" repeatCount="indefinite"/>
  </circle>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 100" width="1280" height="100" role="img" aria-labelledby="ft">
  <title id="ft">Cael Findley — footer</title>
  <defs>
    <linearGradient id="fsky" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="50%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg0']}"/>
    </linearGradient>
    <linearGradient id="ffade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="35%" stop-color="white" stop-opacity="1"/>
      <stop offset="100%" stop-color="white" stop-opacity="1"/>
    </linearGradient>
    <mask id="ffm" maskUnits="userSpaceOnUse" x="0" y="0" width="1280" height="100">
      <rect width="1280" height="100" fill="url(#ffade)"/>
    </mask>
  </defs>
  <g mask="url(#ffm)">
  <rect width="1280" height="100" fill="url(#fsky)"/>
  <line x1="72" y1="28" x2="1208" y2="28" stroke="{t['accent']}" stroke-width="1" opacity="0.35">
    <animate attributeName="opacity" values="0.2;0.55;0.2" dur="7s" repeatCount="indefinite"/>
  </line>
{chr(10).join(stars)}
  <text x="72" y="62" fill="{t['ink']}" font-family="{FONT_UI}" font-size="16">Cael Findley</text>
  <text x="72" y="82" fill="{t['accent']}" font-family="{FONT_MONO}" font-size="10" letter-spacing="2">BUILD WITH INTENT</text>
  <text x="1208" y="62" text-anchor="end" fill="{t['muted']}" font-family="{FONT_MONO}" font-size="11">@cael1127</text>
  <text x="1208" y="82" text-anchor="end" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="10">findley.netlify.app</text>
  </g>
</svg>
'''


def accent_wave(theme: str) -> str:
    t = THEMES[theme]
    d = wave_path(28, 10, 4)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
  <path d="{d}" fill="none" stroke="{t['wave']}" stroke-width="1.4" opacity="0.55" stroke-dasharray="8 10">
    <animate attributeName="stroke-dashoffset" from="0" to="-72" dur="6s" repeatCount="indefinite"/>
  </path>
</svg>
'''


def accent_orbit(theme: str) -> str:
    t = THEMES[theme]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
  <ellipse cx="640" cy="28" rx="48" ry="16" fill="none" stroke="{t['orbit']}" stroke-width="1.2" opacity="0.55">
    <animateTransform attributeName="transform" type="rotate" values="0 640 28; 360 640 28" dur="14s" repeatCount="indefinite"/>
  </ellipse>
  <ellipse cx="640" cy="28" rx="28" ry="28" fill="none" stroke="{t['accent2']}" stroke-width="1" opacity="0.35">
    <animateTransform attributeName="transform" type="rotate" values="360 640 28; 0 640 28" dur="10s" repeatCount="indefinite"/>
  </ellipse>
  <circle cx="640" cy="28" r="4" fill="{t['accent']}">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="688" cy="28" r="2.5" fill="{t['accent2']}">
    <animateTransform attributeName="transform" type="rotate" values="0 640 28; 360 640 28" dur="14s" repeatCount="indefinite"/>
  </circle>
</svg>
'''


def accent_pulse(theme: str) -> str:
    t = THEMES[theme]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
  <line x1="200" y1="28" x2="560" y2="28" stroke="{t['line']}" stroke-width="1"/>
  <line x1="720" y1="28" x2="1080" y2="28" stroke="{t['line']}" stroke-width="1"/>
  <circle cx="640" cy="28" r="5" fill="{t['accent']}">
    <animate attributeName="r" values="4;7;4" dur="2.8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="640" cy="28" r="14" fill="none" stroke="{t['accent']}" stroke-width="1" opacity="0.4">
    <animate attributeName="r" values="10;20;10" dur="2.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.45;0.05;0.45" dur="2.8s" repeatCount="indefinite"/>
  </circle>
</svg>
'''


def accent_constellation(theme: str) -> str:
    t = THEMES[theme]
    hubs = [(520, 20), (580, 40), (640, 16), (700, 38), (760, 22), (620, 42)]
    links = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (2, 5), (3, 5)]
    parts = []
    for i, (a, b) in enumerate(links):
        x1, y1 = hubs[a]
        x2, y2 = hubs[b]
        parts.append(f'''  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t['orbit']}" stroke-width="1" opacity="0.25">
    <animate attributeName="opacity" values="0.1;0.55;0.1" dur="3.5s" begin="{i * 0.3}s" repeatCount="indefinite"/>
  </line>''')
    for i, (x, y) in enumerate(hubs):
        parts.append(f'''  <circle cx="{x}" cy="{y}" r="2.8" fill="{t['accent']}" opacity="0.6">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2.6s" begin="{i * 0.2}s" repeatCount="indefinite"/>
  </circle>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
{chr(10).join(parts)}
</svg>
'''


def accent_bridge(theme: str) -> str:
    """Soft star rain under hero — not school falling particles on a dashed line."""
    t = THEMES[theme]
    dots = []
    for i in range(14):
        x = 160 + i * 72
        delay = i * 0.28
        dots.append(f'''  <circle cx="{x}" cy="24" r="1.8" fill="{t['accent']}" opacity="0.2">
    <animate attributeName="cy" values="10;38;10" dur="4.2s" begin="{delay}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.1;0.75;0.1" dur="4.2s" begin="{delay}s" repeatCount="indefinite"/>
  </circle>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 48" width="1280" height="48" role="img" aria-hidden="true">
  <path d="M120,24 Q640,8 1160,24" fill="none" stroke="{t['wave']}" stroke-width="1" opacity="0.3">
    <animate attributeName="opacity" values="0.15;0.4;0.15" dur="5s" repeatCount="indefinite"/>
  </path>
{chr(10).join(dots)}
</svg>
'''


def accent_school(theme: str) -> str:
    """Two orbiting hubs — personal ↔ school."""
    t = THEMES[theme]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
  <circle cx="560" cy="28" r="6" fill="{t['accent']}">
    <animate attributeName="cx" values="540;560;540" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="720" cy="28" r="6" fill="#500000" opacity="0.85">
    <animate attributeName="cx" values="740;720;740" dur="5s" repeatCount="indefinite"/>
  </circle>
  <path d="M570,28 Q640,8 710,28" fill="none" stroke="{t['orbit']}" stroke-width="1.3" stroke-dasharray="6 6" opacity="0.6">
    <animate attributeName="stroke-dashoffset" from="0" to="-24" dur="2s" repeatCount="indefinite"/>
  </path>
  <text x="560" y="50" text-anchor="middle" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="8">@cael1127</text>
  <text x="720" y="50" text-anchor="middle" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="8">@caelf-hub</text>
</svg>
'''


ACCENTS = {
    "bridge": accent_bridge,
    "wave": accent_wave,
    "orbit": accent_orbit,
    "pulse": accent_pulse,
    "constellation": accent_constellation,
    "school": accent_school,
}


def main():
    accents_dir = OUT / "accents"
    accents_dir.mkdir(exist_ok=True)
    # remove old school-clone accent names if present
    for old in accents_dir.glob("*.svg"):
        old.unlink()
    for theme in ("dark", "light"):
        (OUT / f"header-{theme}.svg").write_text(header_svg(theme), encoding="utf-8")
        (OUT / f"footer-{theme}.svg").write_text(footer_svg(theme), encoding="utf-8")
        (OUT / f"bridge-{theme}.svg").write_text(accent_bridge(theme), encoding="utf-8")
        for name, fn in ACCENTS.items():
            path = accents_dir / f"{name}-{theme}.svg"
            path.write_text(fn(theme), encoding="utf-8")
            print(f"{path.name}: ok")
        print(f"header-{theme}.svg: {len(header_svg(theme))} chars")


if __name__ == "__main__":
    main()
