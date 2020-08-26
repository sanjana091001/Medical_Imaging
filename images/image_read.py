import cv2

image=cv2.imread('Downloads/pic.png')
h,w=image.shape[:2]
print("Height= ",h," width=  ",w)