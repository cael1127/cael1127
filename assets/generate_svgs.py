#!/usr/bin/env python3
"""Generate sage/emerald SMIL SVG assets for cael1127 personal profile."""

from pathlib import Path
from math import sin, pi

OUT = Path(__file__).resolve().parent
FONT_UI = "Georgia, 'Times New Roman', Times, serif"
FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# Sage / emerald — tuned for GitHub light & dark canvases
THEMES = {
    "dark": {
        "bg0": "#0d1117",
        "bg1": "#101612",
        "ink": "#ecf2ec",
        "muted": "#a8b5a8",
        "faint": "#7a8a7a",
        "accent": "#86efac",       # soft emerald
        "accent2": "#a3b18a",      # sage
        "deep": "#14532d",
        "glow": "#1a3d2a",
        "mist": "#243528",
        "leaf": "#4ade80",
        "line": "#2d4a38",
        "soft": "#365314",
    },
    "light": {
        "bg0": "#ffffff",
        "bg1": "#f5f7f3",
        "ink": "#14201a",
        "muted": "#4a5c50",
        "faint": "#6b7c70",
        "accent": "#047857",       # deep emerald
        "accent2": "#52796f",      # sage
        "deep": "#065f46",
        "glow": "#d8e8d8",
        "mist": "#e8efe6",
        "leaf": "#059669",
        "line": "#c5d4c5",
        "soft": "#bbf7d0",
    },
}


def header_svg(theme: str) -> str:
    """Fully static editorial banner — no SMIL animations."""
    t = THEMES[theme]
    # Solid sage panel + typography + CF monogram. Soft blend into GitHub canvas.
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 440" width="1280" height="440" role="img" aria-labelledby="title desc">
  <title id="title">Cael Findley — Software Developer</title>
  <desc id="desc">Static sage/emerald editorial profile banner ({theme})</desc>
  <defs>
    <linearGradient id="wash" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="40%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg0']}"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['deep']}" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="{t['glow']}" stop-opacity="0.15"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="5%" stop-color="white" stop-opacity="1"/>
      <stop offset="90%" stop-color="white" stop-opacity="1"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <mask id="blend" maskUnits="userSpaceOnUse" x="0" y="0" width="1280" height="440">
      <rect width="1280" height="440" fill="url(#edge)"/>
    </mask>
  </defs>

  <g mask="url(#blend)">
    <rect width="1280" height="440" fill="url(#wash)"/>

    <!-- Left brand column -->
    <rect x="0" y="0" width="14" height="440" fill="{t['accent']}"/>
    <rect x="14" y="0" width="220" height="440" fill="url(#panel)"/>

    <!-- Monogram block -->
    <rect x="48" y="150" width="152" height="152" rx="8" fill="{t['accent']}" opacity="0.95"/>
    <text x="124" y="252" text-anchor="middle" fill="{t['bg0']}" font-family="{FONT_UI}" font-size="72" font-weight="700" letter-spacing="-2">CF</text>

    <!-- Primary type -->
    <text x="300" y="150" fill="{t['accent2']}" font-family="{FONT_MONO}" font-size="20" font-weight="600" letter-spacing="5">SOFTWARE DEVELOPER</text>
    <text x="300" y="240" fill="{t['ink']}" font-family="{FONT_UI}" font-size="96" font-weight="400" letter-spacing="-2">Cael Findley</text>
    <rect x="300" y="268" width="280" height="5" rx="2" fill="{t['accent']}"/>
    <text x="300" y="320" fill="{t['muted']}" font-family="{FONT_SANS}" font-size="26">AI systems · full-stack products · systems</text>
    <text x="300" y="368" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="18" letter-spacing="1.5">Texas A&amp;M CS  ·  @cael1127</text>
  </g>
</svg>
'''


def footer_svg(theme: str) -> str:
    t = THEMES[theme]
    dots = []
    for i in range(20):
        x = 100 + i * 54
        delay = i * 0.18
        dots.append(f'''  <circle cx="{x}" cy="52" r="1.5" fill="{t['accent']}" opacity="0.25">
    <animate attributeName="opacity" values="0.15;0.7;0.15" dur="3.4s" begin="{delay}s" repeatCount="indefinite"/>
  </circle>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 96" width="1280" height="96" role="img" aria-labelledby="ft">
  <title id="ft">Cael Findley — footer</title>
  <defs>
    <linearGradient id="fground" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="50%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg0']}"/>
    </linearGradient>
    <linearGradient id="ffade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="35%" stop-color="white" stop-opacity="1"/>
      <stop offset="100%" stop-color="white" stop-opacity="1"/>
    </linearGradient>
    <mask id="ffm" maskUnits="userSpaceOnUse" x="0" y="0" width="1280" height="96">
      <rect width="1280" height="96" fill="url(#ffade)"/>
    </mask>
  </defs>
  <g mask="url(#ffm)">
  <rect width="1280" height="96" fill="url(#fground)"/>
  <line x1="72" y1="26" x2="1208" y2="26" stroke="{t['accent2']}" stroke-width="1" opacity="0.4">
    <animate attributeName="opacity" values="0.25;0.55;0.25" dur="7s" repeatCount="indefinite"/>
  </line>
{chr(10).join(dots)}
  <text x="72" y="58" fill="{t['ink']}" font-family="{FONT_UI}" font-size="15">Cael Findley</text>
  <text x="72" y="78" fill="{t['accent']}" font-family="{FONT_MONO}" font-size="10" letter-spacing="2">BUILD WITH INTENT</text>
  <text x="1208" y="58" text-anchor="end" fill="{t['muted']}" font-family="{FONT_MONO}" font-size="11">@cael1127</text>
  <text x="1208" y="78" text-anchor="end" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="10">findley.netlify.app</text>
  </g>
</svg>
'''


def wave_path(y: int = 28, amp: int = 9, cycles: float = 3.5) -> str:
    pts = []
    for i in range(0, 1281, 8):
        tt = i / 1280 * cycles * 2 * pi
        pts.append(f"{i},{y + amp * sin(tt):.1f}")
    return "M" + " L".join(pts)


def accent_bridge(theme: str) -> str:
    t = THEMES[theme]
    dots = []
    for i in range(12):
        x = 180 + i * 80
        delay = i * 0.3
        dots.append(f'''  <ellipse cx="{x}" cy="24" rx="3" ry="5" fill="{t['leaf']}" opacity="0.2">
    <animate attributeName="cy" values="12;36;12" dur="4.5s" begin="{delay}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.1;0.65;0.1" dur="4.5s" begin="{delay}s" repeatCount="indefinite"/>
  </ellipse>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 48" width="1280" height="48" role="img" aria-hidden="true">
  <path d="M140,24 Q640,6 1140,24" fill="none" stroke="{t['accent2']}" stroke-width="1.1" opacity="0.35">
    <animate attributeName="opacity" values="0.2;0.45;0.2" dur="5s" repeatCount="indefinite"/>
  </path>
{chr(10).join(dots)}
</svg>
'''


def accent_wave(theme: str) -> str:
    t = THEMES[theme]
    d = wave_path(28, 9, 3.5)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
  <path d="{d}" fill="none" stroke="{t['accent']}" stroke-width="1.4" opacity="0.55" stroke-dasharray="7 9">
    <animate attributeName="stroke-dashoffset" from="0" to="-64" dur="6s" repeatCount="indefinite"/>
  </path>
</svg>
'''


def accent_orbit(theme: str) -> str:
    """Emerald gem with soft rings — renamed motif for accents."""
    t = THEMES[theme]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
  <circle cx="640" cy="28" r="16" fill="none" stroke="{t['accent2']}" stroke-width="1" opacity="0.4">
    <animate attributeName="r" values="12;20;12" dur="3.2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.4;0.1;0.4" dur="3.2s" repeatCount="indefinite"/>
  </circle>
  <polygon points="640,14 654,28 640,42 626,28" fill="{t['accent']}" opacity="0.85">
    <animate attributeName="opacity" values="0.6;1;0.6" dur="2.8s" repeatCount="indefinite"/>
  </polygon>
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
  <circle cx="640" cy="28" r="14" fill="none" stroke="{t['leaf']}" stroke-width="1" opacity="0.4">
    <animate attributeName="r" values="10;20;10" dur="2.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.45;0.05;0.45" dur="2.8s" repeatCount="indefinite"/>
  </circle>
</svg>
'''


def accent_constellation(theme: str) -> str:
    t = THEMES[theme]
    hubs = [(520, 22), (580, 38), (640, 16), (700, 36), (760, 20), (620, 40)]
    links = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (2, 5), (3, 5)]
    parts = []
    for i, (a, b) in enumerate(links):
        x1, y1 = hubs[a]
        x2, y2 = hubs[b]
        parts.append(f'''  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t['accent2']}" stroke-width="1" opacity="0.25">
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


def accent_school(theme: str) -> str:
    t = THEMES[theme]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 56" width="1280" height="56" role="img" aria-hidden="true">
  <circle cx="560" cy="28" r="6" fill="{t['accent']}">
    <animate attributeName="cx" values="540;560;540" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="720" cy="28" r="6" fill="#500000" opacity="0.85">
    <animate attributeName="cx" values="740;720;740" dur="5s" repeatCount="indefinite"/>
  </circle>
  <path d="M570,28 Q640,8 710,28" fill="none" stroke="{t['accent2']}" stroke-width="1.3" stroke-dasharray="6 6" opacity="0.6">
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
    for theme in ("dark", "light"):
        (OUT / f"header-{theme}.svg").write_text(header_svg(theme), encoding="utf-8")
        (OUT / f"banner-{theme}.svg").write_text(header_svg(theme), encoding="utf-8")
        (OUT / f"footer-{theme}.svg").write_text(footer_svg(theme), encoding="utf-8")
        (OUT / f"bridge-{theme}.svg").write_text(accent_bridge(theme), encoding="utf-8")
        for name, fn in ACCENTS.items():
            path = accents_dir / f"{name}-{theme}.svg"
            path.write_text(fn(theme), encoding="utf-8")
            print(f"{path.name}: ok")
        print(f"header-{theme}: {len(header_svg(theme))} chars")


if __name__ == "__main__":
    main()
