from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (200, 50), color = (73, 109, 137))

fnt = ImageFont.truetype('preeti.ttf', 20)
d = ImageDraw.Draw(img)
d.text((15,15), "! @ # $ % ^ & * ( ) ", font=fnt, fill=(255, 255, 0))
img.save('pil_text_font.png')