import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
img = Image.open("lieldienas.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Aaargh.ttf", 16)
draw.text((100, 10),"Lai Jums priecigas Lieldienas, un specigas olas!",(255,255,255),font=font)
img.save('lieldienas-out.jpg')
