#blur the part of image using OpenCV
import cv2 as cv
import numpy as np

image=cv.imread("E://openCV_images/amber.jpg")
cv.imshow("original_image",image)

new_image=image[200:250,0:500]
#blur this part
gaussian=cv.GaussianBlur(new_image,(7,7),0)

image[200:250,0:500]=gaussian

cv.imshow("new_image",image)
cv.waitKey(0)
cv.destroyAllWindows()
