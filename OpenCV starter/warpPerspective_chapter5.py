import cv2
import numpy as np

img = cv2.imread("Resources/cardsImg.jpg")

cv2.imshow("CardsImg",img)

width,height = 250,350
pts1=np.float32([[286,83],[469,218],[75,322],[264,473]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("warpImg",imgOutput)

cv2.waitKey(0)