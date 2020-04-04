# coding: utf-8
from cv2 import cv2
import matplotlib.pyplot as plt

img_BGR = cv2.imread(r'pictures\cat.jpg')

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)  # matplotlib process in RGB
constant = cv2.copyMakeBorder(
    img_RGB, 40, 40, 40, 40, cv2.BORDER_CONSTANT, value=[0, 0, 255])  # BLUE
reflect = cv2.copyMakeBorder(img_RGB, 40, 40, 40, 40, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(
    img_RGB, 40, 40, 40, 40, cv2.BORDER_REFLECT_101)
replicate = cv2.copyMakeBorder(img_RGB, 40, 40, 40, 40, cv2.BORDER_REPLICATE)
wrap = cv2.copyMakeBorder(img_RGB, 40, 40, 40, 40, cv2.BORDER_WRAP)
titles = ["constant", "reflect", "reflect_101", "replicate", "wrap"]
images = [constant, reflect, reflect_101, replicate, wrap]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# borderType - Flag defining what kind of border to be added. It can be following types:
# cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
# cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
# cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
# cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
# cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg
# value - Color of border if border type is cv2.BORDER_CONSTANT