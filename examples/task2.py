# import the necessary packages


import cv2
import numpy as np

def donothing(x):
    pass

img = cv2.imread('lena.jpg')
im_mod = img.copy()

width = img.shape[0]

width = width-20

widthlimit = int(width/2)

print(widthlimit)

height = img.shape[1] 

#height is 399
height = height-20

heightlimit = int (height/2)


print(heightlimit)

cv2.namedWindow("Task 2")
#label of trackbar, window title, starting value, ending value, method that is called on change
cv2.createTrackbar('CropX', 'Task 2', 1, widthlimit, donothing)
cv2.createTrackbar('CropY', 'Task 2', 1, heightlimit, donothing)
cv2.createTrackbar('CropX2','Task 2', 1, widthlimit, donothing)
cv2.createTrackbar('CropY2','Task 2', 1, heightlimit, donothing)





while True:

    cropLeft = cv2.getTrackbarPos("CropX", "Task 2")
    cropUp = cv2.getTrackbarPos("CropY", "Task 2")
    cropRight = cv2.getTrackbarPos("CropX2", "Task 2")
    cropDown = cv2.getTrackbarPos("CropY2", "Task 2")

    if cropLeft <= 1:
        cropLeft = 1
    if cropUp <= 1:
        cropUp = 1
    if cropRight <= 1:
        cropRight = 1
    if cropDown <= 1:
        cropDown = 1
    

    #print(img.shape)
    

    
    #this is the full image

  #  if ( cropUp > 10 and cropDown > 10 and cropLeft > 10 and cropRight> 10):
    #I should not be able to crop to 0



    #if 399 pixels is 100, how can 0 be equivalent to 20? 
    

   # im_mod = img[cropUp:-cropDown,-cropLeft:-cropRight,:]

    #range between 0 and height - 21
    #100 => 378
    

   # print(cropLeft)

    

    im_mod = img[cropUp:-cropDown,cropLeft:-cropRight,:]
    print(im_mod.shape)





  


    

    cv2.imshow("Output ", im_mod)


    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        break
