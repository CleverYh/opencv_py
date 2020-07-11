# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\equalization_opencv.jpg',0)

# OpenCV has a function to do histograms equalization, cv2.equalizeHist(). Its input is just grayscale image and output is our histogram equalized image.
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side

plt.imshow(res, 'gray')
plt.show()
# cv2.imwrite('res.png',res)

# Histogram equalization is good when histogram of the image is confined to a particular region. It won’t work good in places where there is large intensity variations where histogram covers a large region, ie both bright and dark pixels are present.
# Check : https://stackoverflow.com/questions/10549245/how-can-i-adjust-contrast-in-opencv-in-c
# Also : https://stackoverflow.com/questions/10561222/how-do-i-equalize-contrast-brightness-of-images-using-opencv