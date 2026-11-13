
import cv2

# Read the original image
img = cv2.imread("exp17input.jpg")

# Check whether image is loaded
if img is None:
    print("Image not found")
    exit()

# Add watermark text
watermark = "WATERMARK"

# Insert watermark into image
cv2.putText(img, watermark, (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            2, (0, 0, 255), 3)

# Save watermarked image
cv2.imwrite("watermarked.jpg", img)

# Display the image
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
