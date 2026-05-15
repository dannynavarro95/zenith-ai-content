from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import textwrap
import json

WIDTH = 1080
HEIGHT = 1350

template = Image.open(
    "../assets/plantilla instagram.png"
).convert("RGBA")

generated = Image.open(
    "../output/generated-image.png"
).convert("RGBA")

generated = generated.resize(
    (760, 760)
)

canvas = template.copy()

generated = generated.rotate(
    -6,
    expand=True
)

canvas.paste(
    generated,
    (360, 260),
    generated
)

draw = ImageDraw.Draw(canvas)

with open(
    "../output/campaign.json",
    "r",
    encoding="utf-8"
) as f:

    campaign = json.load(f)

title = campaign["title"]

subtitle = campaign["subtitle"]

title_font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    92
)

subtitle_font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    32
)

title_lines = textwrap.wrap(
    title,
    width=14
)

y = 260

for line in title_lines:

    draw.text(
        (70, y),
        line,
        font=title_font,
        fill=(255,255,255)
    )

    y += 92

subtitle_lines = textwrap.wrap(
    subtitle,
    width=28
)

y += 30

for line in subtitle_lines:

    draw.text(
        (75, y),
        line,
        font=subtitle_font,
        fill=(210,215,225)
    )

    y += 48

canvas.save(
    "../output/final-post.png"
)

print("\n")
print("FINAL POST GENERATED")
print("\n")
print("../output/final-post.png")
print("\n")
