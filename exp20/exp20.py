import cv2
import numpy as np

img = cv2.imread("exp20.jpg")

kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])

output = cv2.filter2D(img,-1,kernel)

cv2.imshow("Original",cv2.resize(img,(500,400)))
cv2.imshow("Output",cv2.resize(output,(500,400)))

cv2.imwrite("laplacian_negative.jpg",output)

cv2.waitKey(0)
cv2.destroyAllWindows()