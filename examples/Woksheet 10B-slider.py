import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np



def onTrackbarChange(max_slider):

    global img
    global output
    global gray

    output = np.copy(img)

    t1 = max_slider

    ret, img_t1 = cv2.threshold(img ,t1, 255,cv2.THRESH_BINARY)
    cv2.imshow("Thresholded", img_t1)


cv2.namedWindow("Thresholded")

# load the image from disk
img = cv2.imread('trees.png',0)
thresh1 = 25 * 255 // 100

cv2.createTrackbar('threshold', "Thresholded", thresh1, 255, onTrackbarChange)
onTrackbarChange(thresh1)

while True:
    key = cv2.waitKey(5)
    if key == 27:
        break

cv2.destroyAllWindows()










