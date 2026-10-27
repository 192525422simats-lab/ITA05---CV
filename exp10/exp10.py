import cv2
import numpy as np

img=cv2.imread("exp10.jpg")

rows,cols=img.shape[:2]

M=np.float32([[1,0,100],[0,1,50]])

move=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Original Image",img)
cv2.imshow("Translated Image",move)

cv2.imwrite("exp10_out.jpg",move)
print("Output saved as exp10_out.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()