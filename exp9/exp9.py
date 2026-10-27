import cv2

img = cv2.imread("exp9.jpg")

cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
ccw = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("Clockwise", cw)
cv2.imshow("Counter Clockwise", ccw)

cv2.imwrite("exp9_clockwise.jpg", cw)
cv2.imwrite("exp9_counter.jpg", ccw)

cv2.waitKey(0)
cv2.destroyAllWindows()