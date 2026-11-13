import cv2
import numpy as np

cap = cv2.VideoCapture("exp13 video.mp4")

while True:
    ret, f = cap.read()
    if not ret:
        break

    r, c = f.shape[:2]
    p1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
    p2 = np.float32([[0,0],[300,0],[100,300],[250,300]])

    M = cv2.getPerspectiveTransform(p1, p2)
    out = cv2.warpPerspective(f, M, (c, r))

    cv2.imshow("Video", out)

    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()