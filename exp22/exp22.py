
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

# Apply closing operation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display original image
cv2.imshow("Original Image", img)

# Display closing image
cv2.imshow("Closing Image", closing)

# Save output image
cv2.imwrite("closing.jpg", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
