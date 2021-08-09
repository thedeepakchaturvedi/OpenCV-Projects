import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[200:300,100:300] = 255,0,0

# draw line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# draw rectangles
cv2.rectangle(img,(0,0),(256,352),(0,0,255),2)
cv2.rectangle(img,(0,0),(120,145),(255,0,0),cv2.FILLED)
# draw circles
cv2.circle(img,(400,50),30,(255,255,0),5)
# put texts
cv2.putText(img,"OPENCV ",(300,150),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

cv2.imshow("Img",img)
cv2.waitKey(0)