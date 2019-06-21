# Video stream from webcam of laptop.
# Converts the video stream to grayscale.

import numpy as np
import cv2

cap = cv2.VideoCapture(0) #capture video from laptop cam. Hence cam index = 0 or -1.

print ("Press 'Q' to quit")
while(True):
    
    ret, frame = cap.read()  # Capture frame-by-frame
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting to grayscale.
    
    cv2.imshow('farme',frame) # Displays the original frame.
    cv2.imshow('frame',gray)  # Display the grayscale frame.
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()  # When everything done, release the capture.
cv2.destroyAllWindows() # Close all windows.


# cv2.waitKey() returns a 32 Bit integer value (might be dependent on the platform). The key input is in ASCII which is an 8 Bit integer value. So you only care about these 8 bits and want all other bits to be 0.

# ord('q') returns the ascii value of 'q'.
