import cv2
import numpy as np

img = cv2.imread("Resources/card.jpg")
width, height = 450, 300
pts1 = np.float32([[256, 141], [884, 270], [306, 540], [964, 650]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image Perspective", imgOutput)
cv2.waitKey(0)
