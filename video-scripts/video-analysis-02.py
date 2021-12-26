import numpy as np
import cv2


def list_ports():
    """
Test the ports and returns a tuple with the available ports and the ones that are working.
"""
    is_working = True
    dev_port = 0
    working_ports = []
    available_ports = []
    while is_working:
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            is_working = False
            print("Port %s is not working." % dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %
                      (dev_port, h, w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." % (
                    dev_port, h, w))
                available_ports.append(dev_port)
        dev_port += 1
    return available_ports, working_ports


ports = list_ports()

cap = cv2.VideoCapture(0)


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(0)  # waits until a key is pressed


cap.release()
cv2.destroyAllWindows()
