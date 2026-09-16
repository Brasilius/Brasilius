"""Rebuild the original, dependency-free SVG artwork: python3 scripts/render-profile.py."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets"
BG, PANEL, LINE, GREEN, CREAM, MUTED = (
    "#141d18", "#1d2b22", "#3a5140", "#aac986", "#e0e8ce", "#8fa58c"
)
FONT = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "I": ["111", "010", "010", "010", "010", "010", "111"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
}


def rect(x, y, w, h, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>'


def text(x, y, label, size=14, color=MUTED):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="monospace" font-size="{size}">{escape(label)}</text>'


def pixel_text(label, x, y, scale):
    result = []
    for letter in label:
        rows = FONT[letter]
        for dy, row in enumerate(rows):
            for dx, bit in enumerate(row):
                if bit == "1":
                    result.append(rect(x + dx * scale, y + dy * scale, scale, scale, GREEN))
        x += (len(rows[0]) + 1) * scale
    return "".join(result)


def svg(name, height, title, description, body):
    document = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<style>
  .float {{ animation: float 5s steps(5, end) infinite; }}
  .spark {{ animation: sparkle 4s steps(2, end) infinite; }}
  .steam {{ animation: float 3s steps(4, end) infinite; }}
  @keyframes float {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-8px); }} }}
  @keyframes sparkle {{ 0%,100% {{ opacity: .35; }} 50% {{ opacity: 1; }} }}
  @media (prefers-reduced-motion: reduce) {{ .float,.spark,.steam {{ animation: none; }} }}
</style>
{rect(0, 0, 960, height, BG)}
{rect(1, 1, 958, height-2, 'none', f'stroke="{LINE}"')}
{body}
</svg>
'''
    (ROOT / name).write_text(document)


body = rect(1, 1, 958, 38, PANEL)
body += text(24, 25, "BRASI / PERSONAL TERMINAL", 12, GREEN)
body += text(701, 25, "LOS ANGELES  /  EARTH", 12)
for i in range(3):
    body += rect(917 + i * 10, 17, 4, 4, GREEN if i == 0 else LINE)
body += text(40, 86, "HELLO, WORLD. I'M LEO.", 13, CREAM)
body += pixel_text("BRASILIUS", 40, 112, 10)
body += text(40, 218, "AEROSPACE ENGINEER / SOFTWARE DEVELOPER", 17, CREAM)
body += text(40, 247, "Open source. Linux. Rockets. Drones.", 15)
body += rect(40, 274, 286, 30, PANEL)
body += rect(53, 286, 6, 6, GREEN, 'class="spark"')
body += text(70, 294, "MATCHA FUELED / FLIGHT MINDED", 12, GREEN)
# A stepped moon, stars, mountain range and a tiny hovering rocket.
body += '<g shape-rendering="crispEdges">'
for x, y, s in [(678, 83, 4), (899, 106, 4), (723, 182, 3), (884, 215, 3), (666, 250, 3)]:
    body += rect(x, y, s, s, GREEN, 'class="spark"')
body += '<path d="M830 65h32v8h8v32h-8v8h-32v-8h-8V73h8z" fill="#3a5140"/>'
body += '<path d="M640 306h32v-16h24v-20h24v-20h24v20h24v20h24v16h32v-32h24v-20h24v-24h24v24h24v20h24v32h16v24H640z" fill="#26382b"/>'
body += '<g class="float"><path d="M790 125h8v8h8v16h8v64h-8v16h-24v-16h-8v-64h8v-16h8z" fill="#e0e8ce"/>'
body += rect(782, 157, 24, 24, LINE) + rect(790, 165, 8, 8, GREEN)
body += '<path d="M774 189h-8v16h-8v24h16z M814 189h8v16h8v24h-16z" fill="#789763"/>'
body += '<path class="spark" d="M782 237h24v16h-8v16h-8v-16h-8z" fill="#aac986"/></g></g>'
body += rect(24, 330, 912, 1, LINE)
body += text(40, 357, "01 / ENGINEER", 12) + text(345, 357, "02 / TINKERER", 12) + text(650, 357, "03 / EXPLORER", 12)
svg("matcha-terminal.svg", 380, "Brasilius — Leo's personal terminal", "Matcha pixel lettering, a hovering rocket, twinkling stars and a mountain horizon. Aerospace engineer and software developer in Los Angeles.", body)

body = '<g shape-rendering="crispEdges">'
body += rect(40, 43, 48, 28, GREEN) + rect(46, 71, 36, 6, GREEN)
body += rect(88, 47, 12, 18, GREEN) + rect(88, 51, 8, 10, BG)
body += rect(36, 81, 64, 4, LINE)
body += '<g class="steam">' + rect(50, 24, 4, 12, MUTED) + rect(66, 20, 4, 12, MUTED) + '</g></g>'
body += text(126, 48, "SMALL COMMITS. BIG TRAJECTORIES.", 20, CREAM)
body += text(126, 77, "Built with matcha and the occasional jet fuel.", 14)
for i, color in enumerate([LINE, MUTED, GREEN, CREAM]):
    body += rect(842 + i * 20, 47, 12, 12, color)
svg("matcha-footer.svg", 108, "Small commits. Big trajectories.", "A pixel matcha cup with gently rising steam. Built with matcha and the occasional jet fuel.", body)

for filename, number, title, subtitle in [
    ("portfolio", "01", "PORTFOLIO", "nielslarsen.dev"),
    ("projects", "02", "PROJECTS", "Explore repositories"),
    ("activity", "03", "ACTIVITY", "Recent public work"),
    ("monkeytype", "04", "MONKEYTYPE", "Meet me at the keyboard"),
]:
    # Native SVG cards stay sharp at every display density.
    card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="460" height="112" viewBox="0 0 460 112" role="img" aria-label="{title}: {subtitle}">
{rect(1, 1, 458, 110, PANEL, f'stroke="{LINE}"')}
{text(22, 33, number + ' / OPEN', 12, MUTED)}
{text(22, 61, title, 20, CREAM)}
{text(22, 87, subtitle, 13, MUTED)}
<path d="M404 44h20v20m-24 4 24-24" fill="none" stroke="{GREEN}" stroke-width="4"/>
</svg>'''
    (ROOT / f"{filename}.svg").write_text(card)
