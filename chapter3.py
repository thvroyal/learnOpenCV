import cv2
import numpy as np

img = cv2.imread("Resources/KSH.jpg")
print(img.shape)

imgResize = cv2.resize(img, (540, 360))

imgCropped = img[0:200, 200: 500]

cv2.imshow("Image", img)
cv2.imshow("Resize Img", imgResize)
cv2.imshow("Cropped Img", imgCropped)

cv2.waitKey(0)
