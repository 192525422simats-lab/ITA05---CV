import cv2

img = cv2.imread("exp2.jpg")

blur = cv2.GaussianBlur(img,(15,15),0)

cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)

cv2.imwrite("exp2_out.jpg", blur)
print("Output saved as exp2_out.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()