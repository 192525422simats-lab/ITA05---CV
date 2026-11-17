
import cv2

cap = cv2.VideoCapture("video.mp4")

frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

frames.reverse()

if len(frames) > 0:
    height, width = frames[0].shape[:2]
    fps = 20

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(
        "output_reversed.mp4", fourcc, fps, (width, height)
    )

    for frame in frames:
        out.write(frame)

    out.release()

print("Reverse video saved successfully")
