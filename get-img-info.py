# coding: utf-8
from cv2 import cv2
import numpy as np

img = cv2.imread(r'pictures\a.jpg')

print(img.shape, img.size, img.dtype)  # (2368, 4096, 3) 29097984 uint8


