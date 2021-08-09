import cv2
import numpy as np
############## code is done with the help of previous 9 chapters ######
cap = cv2.VideoCapture(0)
cap.set(3,640) # width id =3
cap.set(4,480) # height id=4
cap.set(10,150) # brightness id=10

myColors = [[19,189,0,32,255,255], #yellow
            [171,149,0,179,255,255],#red
            [106,64,205,139,146,255]]    #purple


def findColor(img,myColors):

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y= getContours(mask)
    cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
        #cv2.imshow(str(color[0]), mask)

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500: # to ignore dots lines (noise) etc
            cv2.drawContours(imgResult,cnt,-1,(0,0,255),3) # -1 index to draw all shapes
            peri=cv2.arcLength(cnt,True) # true bcz shape is closed
            approx=cv2.approxPolyDP(cnt,0.02*peri,True) # to approx corner points
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img,myColors)
    cv2.imshow("Cam", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


