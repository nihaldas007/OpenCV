import cv2 as cv # type: ignore

# img = cv.imread('Images/Logo1.jpg')

# cv.imshow('Logo1', img)

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()