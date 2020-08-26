import cv2

image = cv2.imread('Desktop/pic.jpg')
output = cv2.putText(image, "hello world",(200,250), cv2.FONT_HERSHEY_DUPLEX, 4,(255, 0, 255), 5)

# 7 arguments in the order (image, text, dimension, font, font_size, rgb, text_size)

cv2.imshow("image", output)
cv2.waitKey(0)