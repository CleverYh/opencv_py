# coding: utf-8
import numpy as np
from cv2 import cv2

# Performance of DFT calculation is better for some array size. It is fastest when array size is power of two. The arrays whose size is a product of 2’s, 3’s, and 5’s are also processed quite efficiently. So if you are worried about the performance of your code, you can modify the size of the array to any optimal size (by padding zeros) before finding DFT. For OpenCV, you have to manually pad zeros. But for Numpy, you specify the new size of FFT calculation, and it will automatically pad zeros for you.

# So how do we find this optimal size ? OpenCV provides a function, cv2.getOptimalDFTSize() for this. It is applicable to both cv2.dft() and np.fft.fft2().

img = cv2.imread(r'pictures\messi5.jpg', 0)
rows, cols = img.shape

print(rows, cols)

nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)
print(nrows, ncols)

# See, the size (342,548) is modified to (360, 576). Now let’s pad it with zeros (for OpenCV) and find their DFT calculation performance. You can do it by creating a new big zero array and copy the data to it, or use cv2.copyMakeBorder().

nimg = np.zeros((nrows, ncols))
nimg[:rows, :cols] = img

# or :
# right = ncols - cols
# bottom = nrows - rows
# bordertype = cv2.BORDER_CONSTANT #just to avoid line breakup in PDF file
# nimg = cv2.copyMakeBorder(img,0,bottom,0,right,bordertype, value = 0)

t_sum = 0
t_best = 100
for i in range(0, 100):
    e1 = cv2.getTickCount()
    fft1 = np.fft.fft2(img)
    e2 = cv2.getTickCount()
    t = (e2 - e1)/cv2.getTickFrequency()
    if (t_best > t):
        t_best = t
    t_sum += t
print('avg process time: ', t_sum/100,
      's ', 'best process time: ', t_best, 's', sep='')

t_sum = 0
t_best = 100
for i in range(0, 100):
    e1 = cv2.getTickCount()
    fft2 = np.fft.fft2(img, [nrows, ncols])
    e2 = cv2.getTickCount()
    t = (e2 - e1)/cv2.getTickFrequency()
    if (t_best > t):
        t_best = t
    t_sum += t
print('avg process time: ', t_sum/100,
      's ', 'best process time: ', t_best, 's', sep='')


t_sum = 0
t_best = 100
for i in range(0, 100):
    e1 = cv2.getTickCount()
    dft1 = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    e2 = cv2.getTickCount()
    t = (e2 - e1)/cv2.getTickFrequency()
    if (t_best > t):
        t_best = t
    t_sum += t
print('avg process time: ', t_sum/100,
      's ', 'best process time: ', t_best, 's', sep='')

t_sum = 0
t_best = 100
for i in range(0, 100):
    e1 = cv2.getTickCount()
    dft2 = cv2.dft(np.float32(nimg), flags=cv2.DFT_COMPLEX_OUTPUT)
    e2 = cv2.getTickCount()
    t = (e2 - e1)/cv2.getTickFrequency()
    if (t_best > t):
        t_best = t
    t_sum += t
print('avg process time: ', t_sum/100,
      's ', 'best process time: ', t_best, 's', sep='')

