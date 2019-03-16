#-*- coding:utf8 -*-
from PIL import Image

im = Image.open("2_1.gif")
im.convert("P")
im2 = Image.new("P",im.size,255)


for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 0: # these are the numbers to get
            im2.putpixel((y,x),0)

im2.show()
