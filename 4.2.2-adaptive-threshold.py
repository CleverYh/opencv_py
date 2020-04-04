# coding: utf-8
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\lena.jpg', 0)  # 使用灰度图

ret, thre_1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
adaptive_thre_1 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_thre_2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ["img", "thre_1", "adaptive_thre_1", "adaptive_thre_2"]
imgs = [img, thre_1, adaptive_thre_1, adaptive_thre_2]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(imgs[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Adaptive Method - It decides how thresholding value is calculated.
# cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
# Block Size - It decides the size of neighbourhood area.

# C - It is just a constant which is subtracted from the mean or weighted mean calculated.
