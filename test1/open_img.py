# import cv2;
# img = cv2.imread('dang.png',0);
# cv2.imshow('image',img);
# cv2.waitKey(0);
# cv2.destroyAllWindows();
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('dang.png',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()