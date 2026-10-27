import cv2
import numpy as np

img = cv2.imread("input.jpg")
r, c = img.shape[:2]

src = np.float32([[50,50],[300,50],[50,300],[300,300]])
dst = np.float32([[0,0],[250,0],[50,300],[300,300]])

H, _ = cv2.findHomography(src, dst)
out = cv2.warpPerspective(img, H, (c, r))

cv2.imshow("Homography", out)
cv2.imwrite("homography.jpg", out)
cv2.waitKey(0)
cv2.destroyAllWindows()