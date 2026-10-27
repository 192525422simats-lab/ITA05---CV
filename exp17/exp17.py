import cv2

img = cv2.imread("exp17.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)

cv2.imshow("Sobel X", sx)
cv2.imwrite("sobelx.jpg", sx)
cv2.waitKey(0)
cv2.destroyAllWindows()