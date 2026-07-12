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


def _term_colors(theme: str):
    t = THEMES[theme]
    if theme == "dark":
        return {
            **t,
            "term_bg": "#0c1210",
            "term_border": "#2d4a38",
            "prompt": "#86efac",
            "cmd": "#e8f0e8",
            "out": "#a3b18a",
            "muted": "#6b7c70",
        }
    return {
        **t,
        "term_bg": "#f3f7f2",
        "term_border": "#c5d4c5",
        "prompt": "#047857",
        "cmd": "#14201a",
        "out": "#52796f",
        "muted": "#6b7c70",
    }


def accent_bridge(theme: str) -> str:
    """Boot progress — session coming online."""
    c = _term_colors(theme)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72" role="img" aria-hidden="true">
  <rect x="200" y="10" width="880" height="52" rx="10" fill="{c['term_bg']}" stroke="{c['term_border']}" stroke-width="1"/>
  <text x="224" y="32" fill="{c['prompt']}" font-family="{FONT_MONO}" font-size="13">booting session…</text>
  <rect x="224" y="42" width="700" height="8" rx="4" fill="{c['term_border']}" opacity="0.5"/>
  <rect x="224" y="42" width="0" height="8" rx="4" fill="{c['prompt']}">
    <animate attributeName="width" values="80;420;700;700;80" keyTimes="0;0.35;0.55;0.85;1" dur="4.5s" repeatCount="indefinite"/>
  </rect>
  <text x="940" y="48" text-anchor="end" fill="{c['out']}" font-family="{FONT_MONO}" font-size="12">
    <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite"/>
    ready
  </text>
</svg>
'''


def accent_wave(theme: str) -> str:
    """Focus — paths lighting up one by one like a directory walk."""
    c = _term_colors(theme)
    paths = [("~/ai", 320), ("~/product", 520), ("~/systems", 760)]
    chips = []
    for i, (label, x) in enumerate(paths):
        chips.append(f'''  <g opacity="0.25">
    <rect x="{x}" y="22" width="140" height="28" rx="6" fill="{c['prompt']}" fill-opacity="0.15" stroke="{c['prompt']}" stroke-width="1"/>
    <text x="{x + 70}" y="41" text-anchor="middle" fill="{c['cmd']}" font-family="{FONT_MONO}" font-size="12">{label}</text>
    <animate attributeName="opacity" values="0.25;1;1;0.25" keyTimes="0;0.15;0.55;1" dur="4.2s" begin="{i * 1.2}s" repeatCount="indefinite"/>
  </g>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72" role="img" aria-hidden="true">
  <rect x="160" y="10" width="960" height="52" rx="10" fill="{c['term_bg']}" stroke="{c['term_border']}" stroke-width="1"/>
  <text x="184" y="42" fill="{c['prompt']}" font-family="{FONT_MONO}" font-size="13">$ cd ~/focus</text>
{chr(10).join(chips)}
</svg>
'''


def accent_orbit(theme: str) -> str:
    """Projects — repo chips lighting in sequence."""
    c = _term_colors(theme)
    names = ["boltPlanner", "aquaFarm", "portfolio", "EmulatorRS", "AI_ACF"]
    chips = []
    for i, name in enumerate(names):
        x = 300 + i * 170
        chips.append(f'''  <g>
    <rect x="{x}" y="22" width="150" height="28" rx="6" fill="{c['prompt']}" fill-opacity="0.08" stroke="{c['prompt']}" stroke-opacity="0.35" stroke-width="1"/>
    <text x="{x + 75}" y="41" text-anchor="middle" fill="{c['out']}" font-family="{FONT_MONO}" font-size="12">{name}</text>
    <animate attributeName="opacity" values="0.3;1;1;0.3" keyTimes="0;0.12;0.55;1" dur="5s" begin="{i * 0.55}s" repeatCount="indefinite"/>
  </g>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72" role="img" aria-hidden="true">
  <rect x="120" y="10" width="1040" height="52" rx="10" fill="{c['term_bg']}" stroke="{c['term_border']}" stroke-width="1"/>
  <text x="144" y="42" fill="{c['prompt']}" font-family="{FONT_MONO}" font-size="13">$ ls ~/projects</text>
{chr(10).join(chips)}
</svg>
'''


def accent_constellation(theme: str) -> str:
    """Stack — install meters filling for each toolchain."""
    c = _term_colors(theme)
    tools = [("ts", 280), ("py", 430), ("react", 580), ("torch", 760), ("aws", 940)]
    bars = []
    for i, (label, x) in enumerate(tools):
        bars.append(f'''  <text x="{x}" y="30" fill="{c['muted']}" font-family="{FONT_MONO}" font-size="11">{label}</text>
  <rect x="{x}" y="38" width="100" height="7" rx="3" fill="{c['term_border']}" opacity="0.45"/>
  <rect x="{x}" y="38" width="0" height="7" rx="3" fill="{c['prompt']}">
    <animate attributeName="width" values="0;{60 + (i * 9) % 40};100;100;0" keyTimes="0;0.25;0.45;0.8;1" dur="5s" begin="{i * 0.35}s" repeatCount="indefinite"/>
  </rect>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72" role="img" aria-hidden="true">
  <rect x="140" y="10" width="1000" height="52" rx="10" fill="{c['term_bg']}" stroke="{c['term_border']}" stroke-width="1"/>
  <text x="164" y="42" fill="{c['prompt']}" font-family="{FONT_MONO}" font-size="13">$ which stack</text>
{chr(10).join(bars)}
</svg>
'''


def accent_school(theme: str) -> str:
    """Remotes — packet traveling between origin and school."""
    c = _term_colors(theme)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72" role="img" aria-hidden="true">
  <rect x="180" y="10" width="920" height="52" rx="10" fill="{c['term_bg']}" stroke="{c['term_border']}" stroke-width="1"/>
  <circle cx="360" cy="36" r="8" fill="{c['prompt']}"/>
  <text x="380" y="41" fill="{c['cmd']}" font-family="{FONT_MONO}" font-size="12">origin · @cael1127</text>
  <line x1="560" y1="36" x2="780" y2="36" stroke="{c['term_border']}" stroke-width="2" stroke-dasharray="6 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-24" dur="1.2s" repeatCount="indefinite"/>
  </line>
  <circle cx="560" cy="36" r="4" fill="{c['prompt']}">
    <animate attributeName="cx" values="560;780;560" dur="2.8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="820" cy="36" r="8" fill="#500000"/>
  <text x="840" y="41" fill="{c['cmd']}" font-family="{FONT_MONO}" font-size="12">school · @caelf-hub</text>
</svg>
'''


def accent_pulse(theme: str) -> str:
    """Status — checks lighting green like a passing CI."""
    c = _term_colors(theme)
    checks = [("build", 340), ("tests", 520), ("ship", 700), ("docs", 880)]
    rows = []
    for i, (label, x) in enumerate(checks):
        rows.append(f'''  <g>
    <circle cx="{x}" cy="36" r="9" fill="none" stroke="{c['term_border']}" stroke-width="2"/>
    <path d="M{x - 4},{36} L{x - 1},{39} L{x + 5},{32}" fill="none" stroke="{c['prompt']}" stroke-width="2" stroke-linecap="round" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{0.1 + i * 0.15:.2f};{0.2 + i * 0.15:.2f};0.85;1" dur="5s" repeatCount="indefinite"/>
    </path>
    <text x="{x}" y="58" text-anchor="middle" fill="{c['muted']}" font-family="{FONT_MONO}" font-size="10">{label}</text>
  </g>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72" role="img" aria-hidden="true">
  <rect x="160" y="6" width="960" height="60" rx="10" fill="{c['term_bg']}" stroke="{c['term_border']}" stroke-width="1"/>
  <text x="184" y="40" fill="{c['prompt']}" font-family="{FONT_MONO}" font-size="13">$ git status</text>
{chr(10).join(rows)}
</svg>
'''


def accent_connect(theme: str) -> str:
    """Connect — inbox ping / reply pulse."""
    c = _term_colors(theme)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72" role="img" aria-hidden="true">
  <rect x="220" y="10" width="840" height="52" rx="10" fill="{c['term_bg']}" stroke="{c['term_border']}" stroke-width="1"/>
  <text x="248" y="42" fill="{c['prompt']}" font-family="{FONT_MONO}" font-size="13">$ open contacts</text>
  <g transform="translate(520,20)">
    <rect width="36" height="28" rx="4" fill="none" stroke="{c['prompt']}" stroke-width="1.5"/>
    <path d="M2,4 L18,16 L34,4" fill="none" stroke="{c['prompt']}" stroke-width="1.5"/>
    <circle cx="30" cy="6" r="4" fill="{c['prompt']}">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.4s" repeatCount="indefinite"/>
      <animate attributeName="r" values="3;5;3" dur="1.4s" repeatCount="indefinite"/>
    </circle>
  </g>
  <text x="580" y="42" fill="{c['out']}" font-family="{FONT_MONO}" font-size="13">portfolio · email · school · ig</text>
  <rect x="980" y="26" width="8" height="16" fill="{c['prompt']}">
    <animate attributeName="opacity" values="1;0;1" dur="1.05s" repeatCount="indefinite"/>
  </rect>
</svg>
'''


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
    chrome_dir = OUT / "chrome"
    for d in (accents_dir, ui_dir, chrome_dir):
        d.mkdir(exist_ok=True)
    for theme in ("dark", "light"):
        svg = header_svg(theme)
        (OUT / f"header-{theme}.svg").write_text(svg, encoding="utf-8")
        (OUT / f"banner-{theme}.svg").write_text(svg, encoding="utf-8")
        (OUT / f"session-{theme}.svg").write_text(svg, encoding="utf-8")
        foot = footer_svg(theme)
        (OUT / f"footer-{theme}.svg").write_text(foot, encoding="utf-8")
        (OUT / f"foot-{theme}.svg").write_text(foot, encoding="utf-8")
        (OUT / f"bridge-{theme}.svg").write_text(accent_bridge(theme), encoding="utf-8")
        for name, fn in ACCENTS.items():
            content = fn(theme)
            (accents_dir / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")
            (ui_dir / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")
            (chrome_dir / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")
            print(f"chrome/{name}-{theme}.svg")
        print(f"session-{theme}: {len(svg)} chars")


if __name__ == "__main__":
    main()
