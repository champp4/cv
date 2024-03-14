import numpy as np
import cv2

# Create a black image
image = np.zeros((400, 400, 3))

# Draw a blue rectangle
cv2.rectangle(image, (50, 50), (150, 150), (255, 0, 0), -1)

# Draw a green circle
cv2.circle(image, (100, 250), 50, (0, 255, 0), -1)

# Draw a red line
# cv2.line(image, (300, 100), (400, 200), (0, 0, 255), 3)

# Display the image
cv2.imshow('2D Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
