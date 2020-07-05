import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift
import cv2
import math

def scaleSpectrum(A):
   return numpy.real(numpy.log10(numpy.absolute(A) + numpy.ones(A.shape)))


# sample values from a spherical gaussian function from the center of the image
# sigma is variance 
def makeGaussianFilter(numRows, numCols, sigma, highPass=True):
   centerI = 0
   centerJ = 0

   def gaussian(i,j):
      coefficient = math.exp(-1.0 * ((i - centerI)**2 + (j - centerJ)**2) / (2 * sigma**2)) 
      return 1 - coefficient if highPass else coefficient

   return numpy.array([[gaussian(i,j) for j in range(numCols)] for i in range(numRows)])


def filterDFT(imageMatrix, filterMatrix):
   shiftedDFT = fftshift(fft2(imageMatrix))
   cv2.imwrite("dft.jpg", scaleSpectrum(shiftedDFT))

   filteredDFT = shiftedDFT * filterMatrix
   cv2.imwrite("filtered-dft.jpg", scaleSpectrum(filteredDFT))
   return ifft2(ifftshift(filteredDFT))


def lowPass(imageMatrix, sigma):
   n,m = imageMatrix.shape
   return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=False))


def highPass(imageMatrix, sigma):
   n,m = imageMatrix.shape
   return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=True))


def hybridImage(highFreqImg, lowFreqImg, sigmaHigh, sigmaLow):
   highPassed = highPass(highFreqImg, sigmaHigh)
   lowPassed = lowPass(lowFreqImg, sigmaLow)

   return highPassed + lowPassed


def playWithFiltering():
   cat = cv2.imread("cat.jpg", 0)

   highPassedCat = highPass(cat, 20)
   lowPassedCat = lowPass(cat, 20)

   cv2.imwrite("low-passed-cat.jpg", numpy.real(lowPassedCat))
   cv2.imwrite("high-passed-cat.jpg", numpy.real(highPassedCat))
   cv2.imwrite("sum-of-cats.jpg", numpy.real((highPassedCat + lowPassedCat)/2.0))

if __name__ == "__main__":
   dog = cv2.imread("dog.jpg", 0)
   cat = cv2.imread("cat.jpg", 0)

   hybrid = hybridImage(dog, cat, 25, 10)
   cv2.imwrite("dog-cat.jpg", numpy.real(hybrid))