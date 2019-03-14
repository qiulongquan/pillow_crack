#-*- coding:utf8 -*-
from PIL import Image

im = Image.open("b1tlzh.gif")
im.convert("P")
im2 = Image.new("P",im.size,255)


for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227: # these are the numbers to get
            im2.putpixel((y,x),0)

im2.show()


inletter = False
foundletter=False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))

    inletter=False
print letters

import hashlib
# hashlib 摘要算法又称哈希算法、散列算法。
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
import time

count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    m.update("%s%s"%(time.time(),count))
    print "m={}".format(m.hexdigest())
    im3.save("./%s.gif"%(m.hexdigest()))
    count += 1