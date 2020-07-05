import numpy as np

def max(img):
    img_height = img.shape[0]
    img_width = img.shape[1]

    max = img[0, 0]

    for j in np.arange(0,img_width-1):
        for i in np.arange(0,img_height-1):
            if img[i, j] > max :
                max = img[i, j]
    return max



def glcm(img, distance):
    img_height = img.shape[0]
    img_width = img.shape[1]

    out = np.zeros((max(img)+1, max(img)+1))

    for i in np.arange(0, img_height):
        for j in np.arange(0, img_width - distance):
            x = img[i, j]
            y = img[i, j+distance]
            out[x, y] += 1
    return out

in_img = np.array([[0, 3, 3, 2],
                [3, 1, 2, 1],
                [0, 1, 0, 3],
                [0, 1, 1, 2]])

out_img1 = glcm(in_img,1)
print("Matrix for distance=1 and direction=0°")
print(out_img1)
