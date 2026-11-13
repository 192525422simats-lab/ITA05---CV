
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg", 0)

# Check whether image is loaded
if img is None:
    print("Image not found")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion operation
erosion = cv2.erode(img, kernel, iterations=1)

# Display original image
cv2.imshow("Original Image", img)

# Display eroded image
cv2.imshow("Erosion Image", erosion)

# Save the output image
cv2.imwrite("erosion.jpg", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
