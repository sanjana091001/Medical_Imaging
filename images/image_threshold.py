import cv2

#first convert to grayscale and then to black w white bg
#threshold(img, limiting_pixel, max_pixel, cv2.THRESHOLD_BINARY)
#instead of binary, can be binary_inv, trunc, tozero, to_zer_inv

img = cv2.imread('Downloads/pic.jpg')
out = img.copy()

img_gray = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("image", thresh)
cv2.waitkey(0)
cv2.destroyAllWindows()