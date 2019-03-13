#-*- coding:utf8 -*-
from PIL import Image
import hashlib
import time
import os

im = Image.open("2.gif")
# (将图片转换为8位像素模式)
im.convert("P")

# 打印颜色直方图
print im.histogram()