#-*- coding:utf8 -*-
from PIL import Image
import hashlib
import time
import os

im = Image.open("2_1.gif")
# (将图片转换为8位像素模式)
im.convert("P")

# 打印颜色直方图
print im.histogram()

his = im.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
    print j,k
