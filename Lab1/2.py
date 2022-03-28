# capture WebCam/Video sourceq
import cv2 as cv

# VideoCapture(x) where x could be:
#   - number reference to the camera
#   - string path to video relative to terminal
cap = cv.VideoCapture(0)

maxframes = 1000

for i in range(maxframes):
    ret, frame = cap.read()

    cv.imshow("Frame name", frame)

    if cv.waitKey(1) == ord('q') or not ret:
        break

cap.release()