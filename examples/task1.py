# import the necessary packages


import cv2
import numpy as np

def donothing(x):
    pass

img = cv2.imread('lena.jpg')
im_mod = img.copy()

cv2.namedWindow("Task 1")
#label of trackbar, window title, starting value, ending value, method that is called on change
cv2.createTrackbar('Crop', 'Task 1', 0, 50, donothing)



while True:

    cropLeft = cv2.getTrackbarPos("Crop", "Task 1")
    
    #this is the full image

   

    if cropLeft>0: 
        im_mod = img[:,cropLeft:,:]

        

    cv2.imshow("Output ", im_mod)


    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        break
