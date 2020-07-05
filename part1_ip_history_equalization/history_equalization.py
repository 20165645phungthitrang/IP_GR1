import os, sys
import cv2

if __name__ == "__main__":
    assert len(sys.argv) == 2, '[USAGE] $ python %s img_6.jpg' % (os.path.basename(__file__), INPUT)
    INPUT = sys.argv[1]
    assert os.path.isfile(INPUT), '%s not found' % INPUT
    
    # read color image with grayscale flag: "cv2.IMREAD_GRAYSCALE"
    img = cv2.imread(INPUT, cv2.IMREAD_GRAYSCALE)       # shape: (960, 960)
    # print grayscale image
    cv2.imwrite('grey_%s' % INPUT, img)
    print('Saved grayscale image @ grey_%s' % INPUT)
    
    equalized_img = cv2.equalizeHist(img)
    cv2.imwrite('equalized_%s' % INPUT, equalized_img)
    print('Saved equalized image @ equalized_%s' % INPUT)
    
    print('Done Tut 6: Histogram Equalization. Welcome to minhng.info')