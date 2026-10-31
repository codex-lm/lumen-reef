from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import random

W, H = 1200, 630
random.seed(27)
image = Image.new("RGB", (W, H))
pixels = image.load()
for y in range(H):
    for x in range(W):
        glow = max(0, 1 - math.hypot((x - 610) / 780, (y - 40) / 760))
        pixels[x, y] = (int(3 + 5 * glow), int(20 + 42 * glow + 13 * (1 - y / H)), int(32 + 51 * glow))

rays = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(rays)
for i in range(7):
    x = 70 + i * 185
    draw.polygon([(x, 0), (x + 70, 0), (x + 300, 540), (x + 160, 540)], fill=(127, 255, 226, 12))
rays = rays.filter(ImageFilter.GaussianBlur(16))
image = Image.alpha_composite(image.convert("RGBA"), rays)

light = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(light)
for radius in range(175, 5, -5):
    alpha = int(1.2 * (175 - radius) / 175 + 1)
    draw.ellipse((635 - radius, 285 - radius, 635 + radius, 285 + radius), fill=(80, 255, 224, alpha))
light = light.filter(ImageFilter.GaussianBlur(22))
image = Image.alpha_composite(image, light)
draw = ImageDraw.Draw(image)

for i in range(70):
    x = random.randrange(W)
    y = random.randrange(H)
    r = random.choice([1, 1, 2, 3])
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(133, 240, 221, random.randrange(45, 150)))

for i in range(16):
    x = i * 82 - 25
    base = H + 10
    height = 60 + (i * 47 % 125)
    color = (5, 48 + i % 3 * 7, 57 + i % 4 * 5, 255)
    draw.line([(x, base), (x + 10, base-height*0.55), (x-5, base-height)], fill=color, width=15)
    draw.line([(x+5, base-height*0.5), (x+35, base-height*0.78)], fill=color, width=10)
    draw.line([(x+6, base-height*0.7), (x-25, base-height*0.88)], fill=color, width=8)
draw.polygon([(0, 570), (140, 545), (270, 580), (420, 552), (590, 585), (780, 550), (960, 575), (1200, 540), (1200, 630), (0, 630)], fill=(3, 24, 34, 255))

manta = Image.new("RGBA", (W, H))
md = ImageDraw.Draw(manta)
md.polygon([(650, 160), (610, 185), (535, 195), (440, 260), (530, 245), (575, 300), (650, 320), (725, 300), (770, 245), (860, 260), (765, 195), (690, 185)], fill=(79, 211, 203, 255))
md.polygon([(650, 173), (615, 210), (650, 290), (685, 210)], fill=(166, 255, 238, 255))
md.line([(650, 300), (655, 360), (670, 415)], fill=(115, 244, 224, 230), width=5)
md.ellipse((625, 205, 637, 217), fill=(3, 35, 46, 255))
md.ellipse((663, 205, 675, 217), fill=(3, 35, 46, 255))
md.ellipse((644, 232, 656, 244), fill=(230, 255, 247, 255))
manta = manta.filter(ImageFilter.GaussianBlur(0.45))
image = Image.alpha_composite(image, manta)
draw = ImageDraw.Draw(image)

for x, y, color in [(405, 330, (255, 141, 120)), (905, 200, (255, 213, 138)), (890, 425, (127, 255, 226))]:
    draw.line([(x-12, y), (x+12, y)], fill=color, width=3)
    draw.line([(x, y-12), (x, y+12)], fill=color, width=3)
    draw.ellipse((x-3, y-3, x+3, y+3), fill=(240, 255, 248))

font_dir = Path("C:/Windows/Fonts")
def font(name, size):
    try:
        return ImageFont.truetype(str(font_dir / name), size)
    except OSError:
        return ImageFont.load_default(size=size)

draw.text((72, 74), "A LITTLE COURAGE GLOWS BRIGHTER", font=font("trebuc.ttf", 20), fill=(127, 255, 226))
draw.text((65, 108), "LUMEN", font=font("trebucbd.ttf", 88), fill=(239, 255, 251))
draw.text((68, 194), "R E E F", font=font("trebucbd.ttf", 72), fill=(127, 255, 226))
draw.text((73, 304), "Skim the shadows. Gather their glow.", font=font("trebuc.ttf", 24), fill=(177, 216, 215))
draw.rounded_rectangle((72, 365, 278, 420), radius=5, fill=(255, 141, 120))
draw.text((96, 380), "DIVE IN", font=font("trebucbd.ttf", 20), fill=(35, 27, 36))
draw.line([(218, 392), (246, 392)], fill=(35, 27, 36), width=3)
draw.line([(236, 382), (246, 392), (236, 402)], fill=(35, 27, 36), width=3)

output = Path(__file__).with_name("cover.png")
image.convert("RGB").save(output, optimize=True)
print(output)
