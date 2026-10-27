import cv2

cap=cv2.VideoCapture("exp6 video.mp4")

while True:
    ret,frame=cap.read()

    if not ret:
        break

    cv2.imshow("Video",frame)

    if cv2.waitKey(25)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()