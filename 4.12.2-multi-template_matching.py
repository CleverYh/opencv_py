# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img_rgb = cv2.imread(r'pictures\mario.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(r'pictures\mario_coin.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

# cv2.imwrite('res.png',img_rgb)
plt.subplot(121), plt.imshow(img_gray, cmap='gray')
plt.title('img_gray'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_rgb, cmap='gray')
plt.title('result', ), plt.xticks([]), plt.yticks([])

plt.show()
