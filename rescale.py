import cv2 as cv # type: ignore

def rescale_frame(frame,scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimenstions = (width, height)

    return cv.resize(frame, dimenstions)

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame, 0.50)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()