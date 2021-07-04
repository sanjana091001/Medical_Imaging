import cv2
import numpy as np
import time


cv2.destroyAllWindows()
def nothing(x):
    pass
    
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

cv2.namedWindow("trackbars")

cv2.createTrackbar("L - H", "trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "trackbars", 255, 255, nothing)


while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("L - H", "trackbars")
    l_s = cv2.getTrackbarPos("L - S", "trackbars")
    l_v = cv2.getTrackbarPos("L - V", "trackbars")
    u_h = cv2.getTrackbarPos("U - H", "trackbars")
    u_s = cv2.getTrackbarPos("U - S", "trackbars")
    u_v = cv2.getTrackbarPos("U - V", "trackbars")
    
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])
    
    mask = cv2.inRange(hsv,lower_range, upper_range)

    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    stacked = np.hstack((mask_3, frame, res))
    
    cv2.imshow('trackbars', cv2.resize(stacked, None, fx=0.6, fy=0.6))
    
    key = cv2.waitKey(1)
    if key==27:
        break
    if key==ord('s'):
        thearray = [[l_h,l_s,l_v], [u_h, u_s, u_v]]
        print(thearray)
        np.save('penvalue', thearray)
        break
    if key==ord('s'):
        thearray = [[l_h,l_s,l_v], [u_h,u_v,u_s]]
        print(thearray)
        
        np.save('penvalue',thearray)
        break
cap.release()
    
 
