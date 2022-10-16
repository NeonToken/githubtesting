import cv2 as cv
import numpy as np
img = cv.imread("assets/cat.jpg",cv.IMREAD_COLOR)
img2 = cv.imread("assets/dog(1).jpg",cv.IMREAD_COLOR)
print(img,img2)
print(img.size,img2.size)
img = cv.resize(img,(1000,1000))
img2 = cv.resize(img2,(1000,1000))
print(img.dtype)
print(img.size,img2.size)
img3 = cv.add(img,img2)
cv.imshow("abomination",img3)
cv.waitKey(0)
cv.destroyAllWindows()
pixels = np.random.randint(5,size=(1000,1000))
pixels2 = np.random.randint(5,size=(1000,1000))
pixels = pixels.astype(np.uint8)
pixels2 = pixels2.astype(np.uint8)
cv.imshow("coool",pixels)
cv.imshow("coool",pixels2)
cv.waitKey(0)
cv.destroyAllWindows()


