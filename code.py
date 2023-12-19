# Import necessary libraries
import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # Import cv2_imsh
# Read the image
image = cv2.imread('/content/objects-png-format.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and help contour detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the edged image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Measure the size of the object
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)
    print(f"Object area: {area}")

# Display the image with contours using cv2_imshow
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2_imshow(image)
