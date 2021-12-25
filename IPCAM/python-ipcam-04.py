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

    # define the screen resulation
    screen_res = 1280, 720
    scale_width = screen_res[0] / crop.shape[1]
    scale_height = screen_res[1] / crop.shape[0]
    scale = min(scale_width, scale_height)
    # resized window width and height
    window_width = int(crop.shape[1] * scale)
    window_height = int(crop.shape[0] * scale)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # cv2.WINDOW_NORMAL makes the output window resizealbe
    # cv2.namedWindow('MetCam', cv2.WINDOW_NORMAL)
    # # resize the window according to the screen resolution
    # cv2.resizeWindow('MetCam', window_width, window_height)

    cv2.namedWindow("MetCam", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        "MetCam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Display the resulting frame
    cv2.imshow("MetCam", crop)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
