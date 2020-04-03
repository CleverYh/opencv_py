# coding: utf-8
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\lena.jpg', 0)  # 使用灰度图
e1 = cv2.getTickCount()
ret, thre_1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
adaptive_thre_1 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 2)
adaptive_thre_2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)

titles = ["img", "thre_1", "adaptive_thre_1", "adaptive_thre_2"]
imgs = [img, thre_1, adaptive_thre_1, adaptive_thre_2]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(imgs[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
e2 = cv2.getTickCount()
plt.show()

t = (e2 - e1)/cv2.getTickFrequency()
print('Process time: ', t, 's', sep='')

# cv2.threshold():
# 参数：
#     img:图像对象，必须是灰度图
#     thresh:阈值
#     maxval：最大值
#     type:
#         cv2.THRESH_BINARY:     小于阈值的像素置为0，大于阈值的置为maxval
#         cv2.THRESH_BINARY_INV： 小于阈值的像素置为maxval，大于阈值的置为0
#         cv2.THRESH_TRUNC：      小于阈值的像素不变，大于阈值的置为thresh
#         cv2.THRESH_TOZERO       小于阈值的像素置0，大于阈值的不变
#         cv2.THRESH_TOZERO_INV   小于阈值的不变，大于阈值的像素置0
# 返回两个值
#     ret:阈值
#     img：阈值化处理后的图像

# cv2.adaptiveThreshold() 自适应阈值处理，图像不同部位采用不同的阈值进行处理
# 参数：
#     img: 图像对象，8-bit单通道图
#     maxValue:最大值
#     adaptiveMethod: 自适应方法
#         cv2.ADAPTIVE_THRESH_MEAN_C     ：阈值为周围像素的平均值
#         cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 阈值为周围像素的高斯均值（按权重）
#     threshType:
#         cv2.THRESH_BINARY:     小于阈值的像素置为0，大于阈值的置为maxValuel
#         cv2.THRESH_BINARY_INV:  小于阈值的像素置为maxValue，大于阈值的置为0
#     blocksize: 计算阈值时，自适应的窗口大小,必须为奇数 （如3：表示附近3个像素范围内的像素点，进行计算阈值）
#     C： 常数值，通过自适应方法计算的值，减去该常数值
# (mean value of the blocksize*blocksize neighborhood of (x, y) minus C)
