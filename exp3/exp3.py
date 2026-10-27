import cv2

img = cv2.imread("exp3.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,100,200)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge", edge)

cv2.imwrite("exp3_out.jpg", edge)
print("Output saved as exp3_out.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()