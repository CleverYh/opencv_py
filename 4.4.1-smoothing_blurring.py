# Image Blurring (Image Smoothing)
# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\opencv.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Averaging is done by convolving the image with a normalized box filter. It simply takes the average of all the pixels under kernel area and replaces the central element with this average. This is done by the function cv2.blur() or cv2.boxFilter(). Check the docs for more details about the kernel. We should specify the width and height of kernel.

# If you don’t want to use a normalized box filter, use cv2.boxFilter() and pass the argument normalize=False to the function.

avg_blur = cv2.blur(img, (5, 5))    # 平均

# In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used. It is done with the function, cv2.GaussianBlur(). We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective in removing Gaussian noise from the image.

# If you want, you can create a Gaussian kernel with the function, cv2.getGaussianKernel().

g_blur = cv2.GaussianBlur(img, (5, 5), 0)   # 高斯滤波

# Here, the function cv2.medianBlur() computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value. This is highly effective in removing salt-and-pepper noise. One interesting thing to note is that, in the Gaussian and box filters, the filtered value for the central element can be a value which may not exist in the original image. However this is not the case in median filtering, since the central element is always replaced by some pixel value in the image. This reduces the noise effectively. The kernel size must be a positive odd integer.

# In this demo, we add a 50% noise to our original image and use a median filter.

img_m = cv2.imread(r'pictures\median.jpg')
img_m = cv2.cvtColor(img_m, cv2.COLOR_BGR2RGB)

median_filtering = cv2.medianBlur(img_m, 5)   # 中值过滤

# As we noted, the filters we presented earlier tend to blur edges. This is not the case for the bilateral filter, cv2.bilateralFilter(), which was defined for, and is highly effective at noise removal while preserving edges. But the operation is slower compared to other filters. We already saw that a Gaussian filter takes the a neighborhood around the pixel and finds its Gaussian weighted average. This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It does not consider whether pixels have almost the same intensity value and does not consider whether the pixel lies on an edge or not. The resulting effect is that Gaussian filters tend to blur edges, which is undesirable.

# The bilateral filter also uses a Gaussian filter in the space domain, but it also uses one more (multiplicative) Gaussian filter component which is a function of pixel intensity differences. The Gaussian function of space makes sure that only pixels are ‘spatial neighbors’ are considered for filtering, while the Gaussian component applied in the intensity domain (a Gaussian function of intensity differences) ensures that only those pixels with intensities similar to that of the central pixel (‘intensity neighbors’) are included to compute the blurred intensity value. As a result, this method preserves edges, since for pixels lying near edges, neighboring pixels placed on the other side of the edge, and therefore exhibiting large intensity variations when compared to the central pixel, will not be included for blurring.

img_b = cv2.imread(r'pictures\bilateral.png')
img_b = cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB)

bilateral_filtering = cv2.bilateralFilter(img_b, 9, 75, 75)    # 双边过滤

plt.subplot(241), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(245), plt.imshow(avg_blur), plt.title('Avg_Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(246), plt.imshow(g_blur), plt.title('Gaussian_Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(243), plt.imshow(img_m), plt.title('Median_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(247), plt.imshow(median_filtering), plt.title('Median_Filtering')
plt.xticks([]), plt.yticks([])
plt.subplot(244), plt.imshow(img_b), plt.title('Bilateral_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(248), plt.imshow(bilateral_filtering), plt.title('Bilateral_Filtering')
plt.xticks([]), plt.yticks([])
plt.show()


# Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. It actually removes high frequency content (e.g: noise, edges) from the image resulting in edges being blurred when this is filter is applied. (Well, there are blurring techniques which do not blur edges). OpenCV provides mainly four types of blurring techniques.
