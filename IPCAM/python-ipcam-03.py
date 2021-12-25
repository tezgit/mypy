import numpy as np
import cv2

cap = cv2.VideoCapture()
# cap.open("rtsp://USER:PASS@IP:PORT/Streaming/Channels/2")
myStream = "rtsp://admin:Optocam.232323@192.168.0.220/live/av0?user=admin&Optocam.232323"
cap.open(myStream)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # get size of captured image
    height, width, channels = frame.shape

    y = 35
    x = 30
    h = height
    w = width
    crop = frame[y: y + h, x: x + w]

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Salida', crop)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
