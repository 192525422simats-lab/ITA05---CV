
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

# Apply dilation operation
dilation = cv2.dilate(img, kernel, iterations=1)

# Display original image
cv2.imshow("Original Image", img)

# Display dilated image
cv2.imshow("Dilated Image", dilation)

# Save output image
cv2.imwrite("dilation.jpg", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
