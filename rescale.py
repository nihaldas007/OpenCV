import cv2 as cv

def rescale_frame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimenstions = (width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()