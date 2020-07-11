# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\imL.png', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
# plt.imshow(res, 'gray')
# plt.show()

# The first histogram equalization we just saw, considers the global contrast of the image. In many cases, it is not a good idea. For example, above shows an input image and its result after global histogram equalization.
# It is true that the background contrast has improved after histogram equalization. But compare the face of statue in both images. We lost most of the information there due to over-brightness. It is because its histogram is not confined to a particular region as we saw in previous cases.
# So to solve this problem, adaptive histogram equalization is used. In this, image is divided into small blocks called “tiles” (tileSize is 8x8 by default in OpenCV). Then each of these blocks are histogram equalized as usual. So in a small area, histogram would confine to a small region (unless there is noise). If noise is there, it will be amplified. To avoid this, contrast limiting is applied. If any histogram bin is above the specified contrast limit (by default 40 in OpenCV), those pixels are clipped and distributed uniformly to other bins before applying histogram equalization. After equalization, to remove artifacts in tile borders, bilinear interpolation is applied.
# Below code snippet shows how to apply CLAHE (Contrast Limited Adaptive Histogram Equalization) in OpenCV

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

res = np.hstack((res, cl1))
plt.imshow(res, 'gray')
plt.show()
# cv2.imwrite('clahe_2.jpg',cl1)
