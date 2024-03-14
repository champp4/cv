import cv2
import numpy as np

# Read the input color image
image = cv2.imread(r"C:\Users\PAVAN KUMAR\OneDrive\Pictures\Saved Pictures\1.jpg")

if image is not None:
    kernel = np.ones((3, 3), np.uint8)

    eroded_image = cv2.erode(image, kernel, iterations=5)
    dilated_image = cv2.dilate(image, kernel, iterations=5)

    scale_factor = 0.1
    resized_original = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
    resized_eroded = cv2.resize(eroded_image, None, fx=scale_factor, fy=scale_factor)
    resized_dilated = cv2.resize(dilated_image, None, fx=scale_factor, fy=scale_factor)

    cv2.imshow("Original Image", resized_original)
    cv2.imshow("Eroded Image", resized_eroded)
    cv2.imshow("Dilated Image", resized_dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")
