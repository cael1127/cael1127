#!/usr/bin/env python3
"""Generate sage/emerald SMIL SVG assets for cael1127 personal profile."""

from pathlib import Path

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
    """
    Theme: a live build session.
    Left = identity (always readable). Right = terminal that types a short session log.
    Story: open shell → whoami → focus → location → ready prompt.
    """
    t = THEMES[theme]
    if theme == "dark":
        term_bg, term_chrome, term_border = "#0c1210", "#152019", "#2d4a38"
        prompt, cmd, out, muted = "#86efac", "#e8f0e8", "#a3b18a", "#6b7c70"
    else:
        term_bg, term_chrome, term_border = "#f3f7f2", "#e5ede3", "#94a894"
        prompt, cmd, out, muted = "#047857", "#14201a", "#52796f", "#6b7c70"

    clips = []
    lines = []
    # (clip_id, y, begin, dur, width, text, fill)
    script = [
        ("c1", 150, "0.5s", "0.75s", 200, "$ whoami", prompt),
        ("c2", 180, "1.4s", "0.85s", 260, "Cael Findley", out),
        ("c3", 220, "2.5s", "0.9s", 290, "$ cat ~/focus.md", prompt),
        ("c4", 250, "3.6s", "1.1s", 400, "AI systems · full-stack · systems", out),
        ("c5", 290, "5.0s", "0.65s", 140, "$ pwd", prompt),
        ("c6", 320, "5.8s", "0.95s", 320, "~/texas-am/computer-science", out),
        ("c7", 360, "7.0s", "0.4s", 40, "$", prompt),
    ]
    for cid, y, begin, dur, width, text, fill in script:
        clips.append(f'''    <clipPath id="{cid}">
      <rect x="742" y="{y - 20}" width="0" height="26">
        <animate attributeName="width" from="0" to="{width}" begin="{begin}" dur="{dur}" fill="freeze"/>
      </rect>
    </clipPath>''')
        safe = text.replace("&", "&amp;")
        lines.append(f'''    <text x="754" y="{y}" fill="{fill}" font-family="{FONT_MONO}" font-size="15" clip-path="url(#{cid})">{safe}</text>''')

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 460" width="1280" height="460" role="img" aria-labelledby="title desc">
  <title id="title">Cael Findley — Software Developer</title>
  <desc id="desc">Build-session banner: identity plus a terminal that types whoami, focus, and location ({theme})</desc>
  <defs>
    <linearGradient id="wash" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="50%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg0']}"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="4%" stop-color="white" stop-opacity="1"/>
      <stop offset="92%" stop-color="white" stop-opacity="1"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <mask id="blend" maskUnits="userSpaceOnUse" x="0" y="0" width="1280" height="460">
      <rect width="1280" height="460" fill="url(#edge)"/>
    </mask>
{chr(10).join(clips)}
  </defs>

  <g mask="url(#blend)">
    <rect width="1280" height="460" fill="url(#wash)"/>

    <!-- Identity -->
    <rect x="0" y="0" width="10" height="460" fill="{t['accent']}"/>
    <text x="56" y="128" fill="{t['accent']}" font-family="{FONT_MONO}" font-size="16" font-weight="600" letter-spacing="4">SOFTWARE DEVELOPER</text>
    <text x="56" y="220" fill="{t['ink']}" font-family="{FONT_UI}" font-size="78" font-weight="400" letter-spacing="-1.5">Cael Findley</text>
    <rect x="56" y="246" width="200" height="4" rx="2" fill="{t['accent']}"/>
    <text x="56" y="296" fill="{t['muted']}" font-family="{FONT_SANS}" font-size="22">Building AI systems and full-stack products</text>
    <text x="56" y="336" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="15" letter-spacing="1.2">Texas A&amp;M CS  ·  @cael1127</text>

    <g transform="translate(56,372)">
      <rect width="168" height="32" rx="16" fill="{t['glow']}" stroke="{t['accent2']}" stroke-width="1"/>
      <circle cx="18" cy="16" r="5" fill="{t['accent']}">
        <animate attributeName="opacity" values="1;0.35;1" dur="1.8s" repeatCount="indefinite"/>
      </circle>
      <text x="34" y="21" fill="{t['ink']}" font-family="{FONT_MONO}" font-size="12" font-weight="600">build session</text>
    </g>

    <!-- Terminal -->
    <rect x="720" y="72" width="500" height="320" rx="12" fill="{term_bg}" stroke="{term_border}" stroke-width="1.5"/>
    <path d="M720,84 a12,12 0 0 1 12,-12 h476 a12,12 0 0 1 12,12 v20 H720 Z" fill="{term_chrome}"/>
    <circle cx="744" cy="92" r="5" fill="#ef4444" opacity="0.8"/>
    <circle cx="762" cy="92" r="5" fill="#eab308" opacity="0.8"/>
    <circle cx="780" cy="92" r="5" fill="#22c55e" opacity="0.8"/>
    <text x="970" y="97" text-anchor="middle" fill="{muted}" font-family="{FONT_MONO}" font-size="12">cael@findley — zsh</text>

{chr(10).join(lines)}

    <!-- Caret after final $ -->
    <rect x="772" y="346" width="9" height="17" fill="{prompt}" opacity="0">
      <animate attributeName="opacity" values="0;0;1" keyTimes="0;0.95;1" dur="7.5s" fill="freeze"/>
      <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.48;0.5;1" dur="1.05s" begin="7.5s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
'''


def footer_svg(theme: str) -> str:
    """Session footer — status bar, not floating dots."""
    t = THEMES[theme]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 88" width="1280" height="88" role="img" aria-labelledby="ft">
  <title id="ft">Cael Findley — session footer</title>
  <defs>
    <linearGradient id="fground" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="50%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg0']}"/>
    </linearGradient>
    <linearGradient id="ffade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="30%" stop-color="white" stop-opacity="1"/>
      <stop offset="100%" stop-color="white" stop-opacity="1"/>
    </linearGradient>
    <mask id="ffm" maskUnits="userSpaceOnUse" x="0" y="0" width="1280" height="88">
      <rect width="1280" height="88" fill="url(#ffade)"/>
    </mask>
  </defs>
  <g mask="url(#ffm)">
    <rect width="1280" height="88" fill="url(#fground)"/>
    <rect x="64" y="22" width="1152" height="44" rx="8" fill="{t['glow']}" stroke="{t['line']}" stroke-width="1"/>
    <circle cx="92" cy="44" r="5" fill="{t['accent']}">
      <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="112" y="50" fill="{t['ink']}" font-family="{FONT_MONO}" font-size="14">session complete</text>
    <text x="640" y="50" text-anchor="middle" fill="{t['faint']}" font-family="{FONT_MONO}" font-size="13">cael@findley · build with intent</text>
    <text x="1196" y="50" text-anchor="end" fill="{t['accent']}" font-family="{FONT_MONO}" font-size="13">exit 0</text>
  </g>
</svg>
'''


def _prompt_bar(theme: str, command: str, height: int = 52) -> str:
    """Shared CLI prompt strip used as section chrome."""
    t = THEMES[theme]
    if theme == "dark":
        bg, border, prompt, text = "#0c1210", "#2d4a38", "#86efac", "#d8e8d8"
    else:
        bg, border, prompt, text = "#f3f7f2", "#c5d4c5", "#047857", "#14201a"
    safe = command.replace("&", "&amp;")
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 {height}" width="1280" height="{height}" role="img" aria-hidden="true">
  <rect x="240" y="8" width="800" height="36" rx="8" fill="{bg}" stroke="{border}" stroke-width="1"/>
  <text x="264" y="32" font-family="{FONT_MONO}" font-size="14">
    <tspan fill="{prompt}">$</tspan><tspan fill="{text}"> {safe}</tspan>
  </text>
  <rect x="{(264 + 18 + len(command) * 8.4):.0f}" y="18" width="8" height="16" fill="{prompt}">
    <animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>
</svg>
'''


def accent_bridge(theme: str) -> str:
    return _prompt_bar(theme, "ready")


def accent_wave(theme: str) -> str:
    return _prompt_bar(theme, "cd ~/focus")


def accent_orbit(theme: str) -> str:
    return _prompt_bar(theme, "ls ~/projects")


def accent_constellation(theme: str) -> str:
    return _prompt_bar(theme, "which stack")


def accent_school(theme: str) -> str:
    return _prompt_bar(theme, "git remote -v")


def accent_pulse(theme: str) -> str:
    return _prompt_bar(theme, "git status --short")


def accent_connect(theme: str) -> str:
    return _prompt_bar(theme, "open mailto:caelfindley@gmail.com")


ACCENTS = {
    "bridge": accent_bridge,
    "focus": accent_wave,
    "work": accent_orbit,
    "stack": accent_constellation,
    "remote": accent_school,
    "status": accent_pulse,
    "connect": accent_connect,
}


def main():
    accents_dir = OUT / "accents"
    ui_dir = OUT / "ui"
    accents_dir.mkdir(exist_ok=True)
    ui_dir.mkdir(exist_ok=True)
    for theme in ("dark", "light"):
        svg = header_svg(theme)
        (OUT / f"header-{theme}.svg").write_text(svg, encoding="utf-8")
        (OUT / f"banner-{theme}.svg").write_text(svg, encoding="utf-8")
        (OUT / f"session-{theme}.svg").write_text(svg, encoding="utf-8")
        (OUT / f"footer-{theme}.svg").write_text(footer_svg(theme), encoding="utf-8")
        (OUT / f"foot-{theme}.svg").write_text(footer_svg(theme), encoding="utf-8")
        (OUT / f"bridge-{theme}.svg").write_text(accent_bridge(theme), encoding="utf-8")
        for name, fn in ACCENTS.items():
            content = fn(theme)
            (accents_dir / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")
            (ui_dir / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")
            print(f"ui/{name}-{theme}.svg")
        print(f"session-{theme}: {len(svg)} chars")


if __name__ == "__main__":
    main()
