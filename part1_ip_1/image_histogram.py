import cv2 
from matplotlib import pyplot as plt 
img = cv2.imread('flower.png',0) 
plt.title('Histogram for gray scale picture')
# alternative way to find histogram of an image 
plt.hist(img.ravel(),256,[0,256]) 
plt.show() 
