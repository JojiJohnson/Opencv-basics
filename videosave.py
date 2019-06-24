import numpy as np
import cv2

cap = cv2.VideoCapture(0)   # cap is a video capture object.

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputfile.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read() # cap.read() returns boolean value.
    
    if ret==True:                   
        # frame = cv2.flip(frame,0)   

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()



# ret will obtain return value either true or false.
# frame will get the next value from the camera.
