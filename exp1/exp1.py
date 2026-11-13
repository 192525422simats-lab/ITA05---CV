import cv2

img = cv2.imread("exp1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)

cv2.imwrite("exp1_out.jpg", gray)
print("Output saved as exp1_out.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()