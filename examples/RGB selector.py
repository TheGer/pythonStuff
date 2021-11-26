# import the necessary packages


import cv2
import numpy as np

def donothing(x):
    pass

img = cv2.imread('lena.jpg')
im_mod = img.copy()

cv2.namedWindow("Color Manipulator1")
#label of trackbar, window title, starting value, ending value, method that is called on change
cv2.createTrackbar('RED', 'Color Manipulator1', 0, 1, donothing)
cv2.createTrackbar('GREEN', 'Color Manipulator1',0, 1, donothing)
cv2.createTrackbar('BLUE', 'Color Manipulator1', 0, 1, donothing)



while True:

    posB = cv2.getTrackbarPos("BLUE", "Color Manipulator1")
    posG = cv2.getTrackbarPos("GREEN", "Color Manipulator1")
    posR = cv2.getTrackbarPos("RED", "Color Manipulator1")
  #  im_mod[:, :, 2] = posR
  #  im_mod[:, :, 1] = posG
  #  im_mod[:, :, 0] = posB

    if posR == 0 :
        im_mod[:, :, 2] = 0
    else : im_mod[:, :, 2] = img[:,:,2]

    if posG == 0:
        im_mod[:, :, 1] = 0
    else:
      im_mod[:, :, 1] = img[:, :, 1]

    if posB == 0 :
        im_mod[:, :, 0] = 0
    else : im_mod[:, :, 0] = img[:,:,0]

    cv2.imshow("Output ", im_mod)


    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        break
