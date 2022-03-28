# capture WebCam/Video sourceq
import cv2 as cv

# VideoCapture(x) where x could be:
#   - number reference to the camera
#   - string path to video relative to terminal
cap = cv.VideoCapture("material/Video.mp4")

frames = []

maxframes = 1000

DIFFERENCE = 3

THRESH = 30
MAXVAL = 255

if THRESH < DIFFERENCE:
    print("'THRESH' value shoud be higher than 'DIFFERENCE'")
    exit(0)

for i in range(maxframes):
    ret, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

    frames.append(frame_gray)

    if len(frames) > DIFFERENCE+1:
        frames.pop(0)
    if len(frames) < DIFFERENCE:
        continue
    
    diff = cv.absdiff(frames[-1], frames[-DIFFERENCE])
    ret, threshold_frame = cv.threshold(diff, THRESH, MAXVAL, cv.THRESH_BINARY)

    cv.imshow("Frame differencing", diff)
    cv.imshow("Frame with threshold", threshold_frame)

    if cv.waitKey(1) == ord('q') or not ret:
        break

cap.release()