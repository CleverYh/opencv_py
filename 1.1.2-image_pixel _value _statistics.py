# coding : utf-8
from cv2 import cv2
import numpy as np

img = cv2.imread(r'pictures\cat.jpg', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", img)

min, max, minLoc, maxLoc = cv2.minMaxLoc(img)
print("min: %.2f, max: %.2f"% (min, max))
print("min loc: ", minLoc)
print("max loc: ", maxLoc)

means, stddev = cv2.meanStdDev(img) # means:均值, stddev:标准差 
print("mean: %.2f, stddev: %.2f"% (means, stddev))
img[np.where(img < means)] = 0
img[np.where(img > means)] = 255
cv2.imshow("binary", img)   # 图片二值化，大于均值为255，小于均值为0.

cv2.waitKey(0)
cv2.destroyAllWindows()