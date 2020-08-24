import cv

image = cv2.imread('Downloads/pic.jpg')
cv2.imshow("ImageWindow",image)
cv2.waitKey(0)
cv2.destroyAllWindows #to destroy all open image windows