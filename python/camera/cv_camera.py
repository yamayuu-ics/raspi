
import cv2
import numpy as np
print(cv2.__version__)
print(np.__version__)


cap = cv2.VideoCapture(0)


while(True):
    ret,frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





