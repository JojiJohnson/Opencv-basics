import numpy as np
import cv2

print ("Press 'Q' to quit")

cap = cv2.VideoCapture(0) #capture video from laptop cam. Hence cam index = 0 or -1.

while(True):
    
    ret, frame = cap.read()  # Capture frame-by-frame
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting to grayscale.

    cv2.imshow('frame',frame)  # Display the resulting frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()  # When everything done, release the capture.
cv2.destroyAllWindows() # Close all windows.
