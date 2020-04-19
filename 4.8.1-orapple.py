# coding: utf-8
import numpy as np
import sys
from cv2 import cv2
import matplotlib.pyplot as plt

A = cv2.imread(r'pictures\apple.jpg')
A = cv2.cvtColor(A, cv2.COLOR_BGR2RGB)
B = cv2.imread(r'pictures\orange.jpg')
B = cv2.cvtColor(B, cv2.COLOR_BGR2RGB)

# Find the Gaussian Pyramids for apple and orange, number of levels is 6
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]  # list
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    # because the GE's size isn't match gpA[i-1]
    width, height, dpt = gpA[i-1].shape
    GE = cv2.resize(GE, (width, height))
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    width, height, dpt = gpB[i-1].shape
    GE = cv2.resize(GE, (width, height))
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)

# Now join the left half of apple and right half of orange in each levels of Laplacian Pyramids
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols//2], lb[:, cols//2:]))
    LS.append(ls)

# Now reconstruct the original image
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    width, height, dpt = LS[i].shape
    ls_ = cv2.resize(ls_, (width, height))
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
# TypeError: slice indices must be integers or None or have an __index__ method because / devide to float, so change to //.
real = np.hstack((A[:, :cols//2], B[:, cols//2:]))

# cv2.imwrite('Pyramid_blending2.jpg', ls_)
# cv2.imwrite('Direct_blending.jpg', real)

plt.subplot(2, 2, 1), plt.imshow(A, cmap='gray')
plt.title('Apple'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(B, cmap='gray')
plt.title('Orange'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(real, cmap='gray')
plt.title('Direct_blending'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(ls_, cmap='gray')
plt.title('Pyramid_blending'), plt.xticks([]), plt.yticks([])

plt.show()

# For sake of simplicity, each step is done separately which may take more memory. You can optimize it if you want so.