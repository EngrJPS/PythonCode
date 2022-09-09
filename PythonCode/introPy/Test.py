import cv2

print("Package Delivered")

img = cv2.imread("Downloads/Cat.jpeg")

cv2.imshow("Output", img)
cv2.waitKey(0)