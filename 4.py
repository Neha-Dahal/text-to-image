from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (30, 30), color = (255,255,255))

fnt = ImageFont.truetype('font2.ttf', 40)
d = ImageDraw.Draw(img)
d.text((2,-2), "$", font=fnt, fill=(255, 0, 0))
img.save('outputs/4/4.png')

img2 = Image.new('RGB', (26, 26), color = (255,255,255))

fnt2 = ImageFont.truetype('font3.ttf', 30)
d2 = ImageDraw.Draw(img2)
d2.text((2,-2), "$", font=fnt2, fill=(255, 0, 0))
img2.save('outputs/4/5.png')

img3 = Image.new('RGB', (30, 30), color = (255,255,255))

fnt3 = ImageFont.truetype('font4.ttf', 40)
d3 = ImageDraw.Draw(img3)
d3.text((2,-2), "$", font=fnt3, fill=(255, 0, 0))
img3.save('outputs/4/6.png')


img4 = Image.new('RGB', (30, 30), color = (255,255,255))

fnt4 = ImageFont.truetype('font5.ttf', 30)
d4 = ImageDraw.Draw(img4)
d4.text((2,-2), "$", font=fnt4, fill=(255, 0, 0))
img4.save('outputs/4/7.png')

img5 = Image.new('RGB', (30, 30), color = (255,255,255))

fnt5 = ImageFont.truetype('font6.ttf', 30)
d5 = ImageDraw.Draw(img5)
d5.text((0,0), "$", font=fnt5, fill=(255, 0, 0))
img5.save('outputs/4/8.png')


img6 = Image.new('RGB', (30, 30), color = (255,255,255))

fnt6 = ImageFont.truetype('font7.otf', 40)
d6 = ImageDraw.Draw(img6)
d6.text((2,-2), "$", font=fnt6, fill=(255, 0, 0))
img6.save('outputs/4/9.png')


img7 = Image.new('RGB', (30, 30), color = (255,255,255))

fnt7 = ImageFont.truetype('font8.ttf', 40)
d7 = ImageDraw.Draw(img7)
d7.text((2,-2), "$", font=fnt7, fill=(255, 0, 0))
img7.save('outputs/4/10.png')


img8 = Image.new('RGB', (30, 30), color = (255,255,255))

fnt8 = ImageFont.truetype('font9.ttf', 40)
d8 = ImageDraw.Draw(img8)
d8.text((2,-2), "$", font=fnt8, fill=(255, 0, 0))
img8.save('outputs/4/11.png')
