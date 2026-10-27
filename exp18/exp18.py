import cv2

img = cv2.imread("exp18.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
output = cv2.convertScaleAbs(sobel)

cv2.imshow("Original", cv2.resize(img, (500,400)))
cv2.imshow("Output", cv2.resize(output, (500,400)))

cv2.imwrite("sobely.jpg", output)

cv2.waitKey(0)
cv2.destroyAllWindows()