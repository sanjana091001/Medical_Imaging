import cv2 

#resizing considering ratio

image = cv2.imread('Downloads/pic.jpg')
height, width = image.shape[:2]
print(height, shape) #to print the actual height and shape of image

ratio = 500 / width
h = int(ratio*height)
dim = (500, h) #tuple with new dimensions
res = cv2.resize(image, dim)
newh, neww = res.shape[:2]
print(newh, neww)