# coding: utf-8
from cv2 import cv2
import matplotlib.pyplot as plt

img_BGR = cv2.imread('cat.jpg')

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)  # matplotlib process in RGB
constant = cv2.copyMakeBorder(
    img_RGB, 40, 40, 40, 40, cv2.BORDER_CONSTANT, value=[0, 0, 255])  # BLUE
reflect = cv2.copyMakeBorder(img_RGB, 40, 40, 40, 40, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(
    img_RGB, 40, 40, 40, 40, cv2.BORDER_REFLECT_101)
replicate = cv2.copyMakeBorder(img_RGB, 40, 40, 40, 40, cv2.BORDER_REPLICATE)
wrap = cv2.copyMakeBorder(img_RGB, 40, 40, 40, 40, cv2.BORDER_WRAP)
titles = ["constant", "reflect", "reflect_101", "replicate", "wrap"]
images = [constant, reflect, reflect_101, replicate, wrap]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
