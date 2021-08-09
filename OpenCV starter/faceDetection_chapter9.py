import cv2
import numpy as np

# cascades in opencv used to detect a lot of things
# all cascades are in D>>My Projects>>OpenCV Projects>>haarcascades

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

path='Resources/myPic.jpg'
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Img",img)
cv2.waitKey(0)