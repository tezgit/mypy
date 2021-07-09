import cv2 as cv

# img = cv.imread('/Users/TeZ/Documents/PY/mypy/openCV-tutorial/bigcat.jpg')
# cv.imshow('gatto', img)
# cv.waitKey(0)


# this works for any video/image
def rescaleFrame(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# this only works with live cam
def changeRes(videocapture, width, height):
    videocapture.set(3, width)
    videocapture.set(4, width)


capture = cv.VideoCapture(
    "/Users/TeZ/Documents/PY/mypy/openCV-tutorial/dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        print(frame.shape)
        print(frame_resized.shape)
        height, width = img.shape[:2]
        break

capture.release()
cv.destroyAllWindows()
