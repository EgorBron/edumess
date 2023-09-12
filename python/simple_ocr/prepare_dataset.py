from PIL import Image, ImageDraw, ImageFont
import string
import os

output_dir = "./dataset/"
os.makedirs(output_dir, exist_ok=True)

font = ImageFont.truetype("times.ttf", 60)
image_size = (50, 100)

for glyph in string.ascii_letters:
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    _,_, text_width, text_height = draw.textbbox((0,0), glyph, font=font)
    text_x = (image_size[0] - text_width) / 2
    text_y = (image_size[1] - text_height) / 2

    draw.text((text_x, text_y), glyph, fill="black", font=font)

    image_filename = os.path.join(output_dir, f"{glyph.capitalize()} {font.getname()[0]}.png")
    image.save(image_filename)

print("generated")
