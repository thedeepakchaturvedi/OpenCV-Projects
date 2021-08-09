import cv2
print("Package Imported")
# # reading and showing images
#
# img = cv2.imread("Resources/myPic.jpg")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# # reading and showing video

# cap = cv2.VideoCapture("Resources/VID_20200603_145123.mp4")
#
# while True:
#     success, img = cap.read()  # it will save the frame in img and tell successfully or not
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break   # press q to break loop

# # to access webcam

cap = cv2.VideoCapture(0)
cap.set(3,640) # width id =3
cap.set(4,480) # height id=4
cap.set(10,100) # brightness id=10
while True:
    success, img = cap.read()
    cv2.imshow("Cam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break