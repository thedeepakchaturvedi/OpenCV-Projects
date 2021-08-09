import cv2
import numpy as np

img = cv2.imread("Resources/myPic.jpg")
kernel = np.ones((5,5),np.uint8) # value (0,255)

# gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # ksize must be odd - (3,3) (5,5) (7,7)
# using edge detector
imgCanny = cv2.Canny(img,100,100)
# img dialation applied on canny
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #increase iteration for thickness
# opposite of dialation
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("GrayImg",imgGray)
cv2.imshow("BlurImg",imgBlur)
cv2.imshow("CannyImg",imgCanny)
cv2.imshow("DialationImg",imgDialation)
cv2.imshow("ErodedImg",imgEroded)
cv2.waitKey(0)