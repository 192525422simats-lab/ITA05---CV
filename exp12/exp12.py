import cv2
import numpy as np

img = cv2.imread("exp12.jpg")
r, c = img.shape[:2]

p1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
p2 = np.float32([[0,0],[300,0],[100,300],[250,300]])

M = cv2.getPerspectiveTransform(p1, p2)
out = cv2.warpPerspective(img, M, (c, r))

cv2.imshow("Perspective", out)
cv2.imwrite("perspective.jpg", out)
cv2.waitKey(0)
cv2.destroyAllWindows()