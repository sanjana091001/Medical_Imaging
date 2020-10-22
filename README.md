# opencv_exps
learning opencv

opencv is a cross-platform library used for image processing, video analysis and computer vision.
supports many languages like java, python, c++ etc
.imread() - to read an image

image[pixelsize, pixelsize] - to traverse eg to get bgr value

image[pixel1 : pixel2, pixel3 : pixel4] - to get certain region of interest

.resize(image, (size, size)) - to resize eg cv2.resize(image, (100,100))

.imshow() - to display image

.destroyAllWindows() - destroy all windows lol

.rectange() - takes 5 arguments, draws a rectangle ie:(image, top dim, bottom dim, rgb vals, width )

.putText() - takes 7 arguments writes text on image ie:(image, "text", dimensions, font, font_size, rgb values, size_of_text)

.cvtColor() - convert to grayscale eg cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

.threshold() - 4 arguments  (img, limit_pixel, max_pixel, type_of_thresholding)

.imwrite() - save the file eg cv2.imwrite('Desktop/new.jpg', newimage)

.VideoCapture(0) - to start capturing video

# Concepts related to Air-Canvas project



