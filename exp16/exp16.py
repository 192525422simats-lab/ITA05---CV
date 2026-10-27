import cv2

img = cv2.imread("exp16.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray, 100, 200)

cv2.imshow("Canny", edge)
cv2.imwrite("canny.jpg", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()