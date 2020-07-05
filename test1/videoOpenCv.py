import numpy as np 
import cv2

img = cv2.imread("dang.png",1);
cv2.line(img, (0, 0), (400, 300), (255, 200, 10), 25);// (anh, toa_do_ban_dau, toadocuoi, (r,g,b), pixel);
cv2.imwrite('dave.jpg', img);

cv2.destroyAllWindows();