import cv2

image = cv2.imread('Downloads/pic.jpg')
rect = cv2.rectangle(rect, (200,200), (500,500), (255, 0, 0), 5)
cv2.imshow("imagewindow", rect)
cv2.waitKey(0)
cv2.destroyAllWindows