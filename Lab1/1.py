import cv2

print("Hello")
print(f"OpenCV version : {cv2.__version__}")

image =  cv2.imread("material/OpenCV.png")
cv2.imshow("LoL", image)
cv2.waitKey(0)