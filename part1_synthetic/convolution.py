import numpy as np
import cv2

def scale_to_0_255(img):
    min_val = np.min(img)
    max_val = np.max(img)
    new_img = (img - min_val) / (max_val - min_val) # 0-1
    new_img *= 255
    return new_img

def convolve_nest_loop(img, kernel):
    scale_img = scale_to_0_255(img)
    img_height = scale_img.shape[0]
    img_width = scale_img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    out = np.zeros((img_height, img_width))

    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            sum = 0
            for k in np.arange(-H, H + 1):
                for l in np.arange(-W, W + 1):
                    a = img[i + k, j + l]
                    w = kernel[H + k, W + l]
                    sum += (w * a)
            out[i, j] = sum
    
    scale_out = scale_to_0_255(out)
    return scale_out

'''in_img = np.array([[1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 1, 1, 0, 1]
                   ])'''
in_img = cv2.imread('cat.png', 0)
kernel = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1]])


out_img = convolve_nest_loop(in_img, kernel)
print(in_img)
print("\n\n\n")
print(out_img)
cv2.imshow("Image",out_img)
cv2.waitKey(0);