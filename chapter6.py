import cv2
import numpy as np


def empty(a):
    pass


path = "Resources/lambo.jpg"
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbar", 8, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 58, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 205, 255, empty)
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbar")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("Image", mask)
    cv2.imshow("ImageHSV", imgHSV)
    # imgHor = np.hstack((img, img))
    # imgVer = np.vstack((img, img))
    #
    # cv2.imshow("Horizontal", imgHor)
    # cv2.imshow("Vertical", imgVer)

    cv2.waitKey(1)
