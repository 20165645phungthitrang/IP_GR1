import cv2;
import numpy as np;

img = cv2.imread("dang.png", 1);

subimg = img[100:500, 100:1000];
subimg = subimg[:,:,1];
cv2.imshow('image', subimg);

cv2.waitKey(0);