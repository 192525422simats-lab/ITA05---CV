import cv2

img=cv2.imread("exp8.jpg")

big=cv2.resize(img,None,fx=2,fy=2)
small=cv2.resize(img,None,fx=0.5,fy=0.5)

cv2.imshow("Original Image",img)
cv2.imshow("Bigger Image",big)
cv2.imshow("Smaller Image",small)

cv2.imwrite("exp8_out_1.jpg",big)
cv2.imwrite("exp8_out_2.jpg",small)
print("Outputs saved suscessfully.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()