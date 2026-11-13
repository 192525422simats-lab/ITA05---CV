
import cv2

# Read image
img = cv2.imread("images.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator
x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine gradients
result = cv2.addWeighted(cv2.convertScaleAbs(x), 0.5,
                         cv2.convertScaleAbs(y), 0.5, 0)

# Display output
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Output", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("sobel_output.jpg", result)
