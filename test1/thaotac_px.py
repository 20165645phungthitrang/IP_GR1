import cv2;
import numpy as np;

img = cv2.imread("dang.png",1);

px = img[0][0];
print(px);

for i in range(300):
    for j in range(300):
        if img[i,j,0] > 30:
            img[i,j] = 1

cv2.imwrite('dang_thaotac_px.png', img)