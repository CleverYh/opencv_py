# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, Gradient etc also comes into play.

img = cv2.imread(r'pictures\j.png')

kernel = np.ones((5, 5), np.uint8)

# The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). So what does it do? The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
# So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel. So the thickness or size of the foreground object decreases or simply white region decreases in the image. It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.

erosion = cv2.erode(img, kernel, iterations=1)

# Dilation is just opposite of erosion. Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases. It is also useful in joining broken parts of an object.

dilation = cv2.dilate(img, kernel, iterations=1)

# Opening is just another name of erosion followed by dilation. It is useful in removing noise, as we explained above. Here we use the function, cv2.morphologyEx()

img_o = cv2.imread(r'pictures\opening.png')
opening = cv2.morphologyEx(img_o, cv2.MORPH_OPEN, kernel)

# Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.

img_c = cv2.imread(r'pictures\closing.png')
closing = cv2.morphologyEx(img_c, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient is the difference between dilation and erosion of an image. The result will look like the outline of the object.

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 9x9 kernel

kernel = np.ones((9, 9), np.uint8)

# Top Hat is the difference between input image and Opening of the image. Below example is done for a 9x9 kernel.

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Black Hat is the difference between the closing of the input image and input image.

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


plt.subplot(2, 5, 1), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 2), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 3), plt.imshow(dilation), plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 4), plt.imshow(img_o), plt.title('Opening Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 5), plt.imshow(img_c), plt.title('Closing Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 9), plt.imshow(opening), plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 10), plt.imshow(closing), plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 6), plt.imshow(gradient), plt.title('Morphological Gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 7), plt.imshow(tophat), plt.title('Top Hat')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 8), plt.imshow(blackhat), plt.title('Black Hat')
plt.xticks([]), plt.yticks([])
plt.show()
