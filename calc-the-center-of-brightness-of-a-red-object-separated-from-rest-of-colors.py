import numpy as np
import cv2
import time
cap = cv2.VideoCapture(1)   

while(True):
    
    __,frame = cap.read()

    red = np.matrix(frame[:,:,2])
    green = np.matrix(frame[:,:,1])
    blue = np.matrix(frame[:,:,0])

    red_only = np.int16(red)-np.int16(green)-np.int16(blue)

    red_only[red_only<0]=0
    red_only[red_only>255]=255
    red_only=np.uint8(red_only)

    #calc center of brightness of the red object
    coulmn_sums = np.matrix(np.sum(red_only,0))
    coulmn_numbers = np.matrix(np.arange(640))
    coulmn_mult = np.multiply(coulmn_sums,coulmn_numbers)
    total = np.sum(coulmn_mult)
    total_total = np.sum(np.sum(red_only))
    coulmn_location = total/total_total
    type(coulmn_location)

    print(coulmn_location)
                            

    cv2.imshow('red_only',red_only)
    cv2.imshow('rgb',frame)
    
    if np.isnan (coulmn_location)  :
        print("green")
    else:
        print("rred")
        
    

    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()
