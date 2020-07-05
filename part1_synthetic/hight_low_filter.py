import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.png',0)
f = np.fft.fft2(img) # bien đổi tần số thành mảng phức tạp 
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow,ccol = rows/2 , cols/2
(fshift[int(crow-30):int(crow+30),int(ccol-30):int(ccol+30)]) = 0 # lọc thông thấp thông cao tùy thuộc vào việc thay đổi 
f_ishift = np.fft.ifftshift(fshift)                                # giá trị cao gần tâm =0 , thấp xa tâm =0
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
#plt.subplot(133),plt.imshow(img_back)
#plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()




