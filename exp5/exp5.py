import cv2
import numpy as np

img=cv2.imread("exp5.jpg")

kernel=np.ones((5,5),np.uint8)

erode=cv2.erode(img,kernel,iterations=1)

cv2.imshow("Original Image",img)
cv2.imshow("Eroded Image",erode)

cv2.imwrite("exp5_out.jpg",erode)
print("Output saved as exp5_out.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()