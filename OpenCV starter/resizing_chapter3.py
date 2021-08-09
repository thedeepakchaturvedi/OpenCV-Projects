import cv2
import numpy as np

img = cv2.imread("Resources/myPic.jpg")
print(img.shape)

imgResize = cv2.resize(img,(260,432)) # (x,y)
print(imgResize.shape)

# cropping of image

imgCropped = img[0:400,100:380]  # (y,x)

cv2.imshow("Image",img)
cv2.imshow("ResisedImg",imgResize)
cv2.imshow("CroppedImg",imgCropped)
cv2.waitKey(0)
