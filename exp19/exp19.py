import cv2

img = cv2.imread("exp19.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sx = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 1, 0))
sy = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 0, 1))

output = cv2.addWeighted(sx, 0.5, sy, 0.5, 0)

cv2.imshow("Original", cv2.resize(img,(500,400)))
cv2.imshow("Output", cv2.resize(output,(500,400)))

cv2.imwrite("sobelxy.jpg", output)

cv2.waitKey(0)
cv2.destroyAllWindows()