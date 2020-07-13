# coding: utf-8
import numpy as np
from cv2 import cv2

print(cv2.useOptimized())

img_1 = cv2.imread(r'pictures\lena.jpg')

e1 = cv2.getTickCount()
for i in range(7, 24, 2):
    img_1 = cv2.medianBlur(img_1, i)
e2 = cv2.getTickCount()

cv2.namedWindow("medianBlur")
cv2.imshow('medianBlur', img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

t = (e2 - e1)/cv2.getTickFrequency()
print('Process time: ',t, 's', sep='')

# Python scalar operations are faster than Numpy scalar operations. So for operations including one or two elements, Python scalar is better than Numpy arrays. Numpy takes advantage when size of array is a little bit bigger.
# Normally, OpenCV functions are faster than Numpy functions. So for same operation, OpenCV functions are preferred. But, there can be exceptions, especially when Numpy works with views instead of copies.

# Avoid using loops in Python as far as possible, especially double/triple loops etc. They are inherently slow.
# Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for vector operations.
# Exploit the cache coherence.
# Never make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.
# Even after doing all these operations, if your code is still slow, or use of large loops are inevitable, use additional libraries like Cython to make it faster.

# More performance optimization will learn in the future.