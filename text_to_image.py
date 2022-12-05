from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (80, 60), color = (255,0,0))

fnt = ImageFont.truetype('preeti.ttf', 20)
d = ImageDraw.Draw(img)
d.text((15,15), "af $ v \n $%*# ", font=fnt, fill=(255, 255, 255))
img.save('pil_text_font.png')