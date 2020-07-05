import cv2
import numpy as np
import matplotlib.pyplot as plt
#% matplotlib inline


img = cv2.imread('charlie_0r.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))


plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Input image')
plt.xticks([])
plt.yticks([])


plt.subplot(1,2,2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.xticks([])
plt.yticks([])
plt.show()


rows, columns = img.shape
center_rows, center_columns = int(rows/2), int(columns/2)
ranges = 10
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fshift[center_rows-ranges:center_rows+ranges, center_columns-ranges:center_columns+ranges] = 1e-10
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


plt.figure(figsize=(10,5))
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Image')
plt.xticks([])
plt.yticks([])


plt.subplot(2,2,2)
plt.imshow(img_back, cmap='gray')
plt.title('Image back')
plt.xticks([])
plt.yticks([])


plt.subplot(2,2,3)
plt.imshow(img_back,)
plt.title('Image back in JET')
plt.xticks([])
plt.yticks([])


magnitude_spectrum = 20*np.log(np.abs(fshift))


plt.subplot(2,2,4)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.xticks([])
plt.yticks([])
plt.show()


# DFT in opencv
img = cv2.imread('charlie_0r.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)


magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Image input')
plt.xticks([])
plt.yticks([])


plt.subplot(1,2,2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude spectrum')
plt.xticks([])
plt.yticks([])
plt.show()


rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)


dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)


# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1


# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])


magnitude_spectrum = 20*np.log(cv2.magnitude(fshift[:,:,0],fshift[:,:,1])+1e5)


plt.figure(figsize=(10,5))
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image')
plt.xticks([]), plt.yticks([])


plt.subplot(222)
plt.imshow(img_back, cmap = 'gray')
plt.title('Image back')
plt.xticks([]), plt.yticks([])


plt.subplot(223)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum')
plt.xticks([]), plt.yticks([])
plt.show()





















