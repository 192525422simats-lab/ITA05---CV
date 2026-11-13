
import cv2

# Read the original image
img = cv2.imread("input.jpg")

# Check whether image is loaded
if img is None:
    print("Image not found")
    exit()

# Display original image
cv2.imshow("Original Image", img)

# Select Region of Interest (ROI)
roi = img[50:200, 50:200]

# Copy the selected region
copy = roi.copy()

# Paste the copied region into another location
img[250:400, 250:400] = copy

# Display cropped image
cv2.imshow("Cropped ROI", roi)

# Display final image
cv2.imshow("Final Image", img)

# Save output image
cv2.imwrite("output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
