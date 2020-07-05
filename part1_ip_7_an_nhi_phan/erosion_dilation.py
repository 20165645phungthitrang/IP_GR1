import cv2 
import numpy as np 
from matplotlib import pyplot as plt
  
img = cv2.imread('Input.png', 0) 
  
# mat na nhan chap 5*5 
kernel = np.ones((5,5), np.uint8) 
   
img_erosion = cv2.erode(img, kernel, iterations=1) 
img_dilation = cv2.dilate(img, kernel, iterations=1) 

images = [img, img_erosion, img_dilation]
titles = ['Input','Erosion','Dilation']

for i in range(3):
    plt.subplot(3,1,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow('Input', img) 
cv2.imshow('Erosion', img_erosion) 
cv2.imshow('Dilation', img_dilation) 
  
cv2.waitKey(0) 