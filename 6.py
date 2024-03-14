import cv2

# Read the input color image
image_bgr = cv2.imread(r"C:\Users\PAVAN KUMAR\OneDrive\Pictures\Saved Pictures\1.jpg")

if image_bgr is not None:
    # Convert BGR to Grayscale
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    # Resize images for better visibility
    scale_factor = 0.1
    resized_original = cv2.resize(image_bgr, None, fx=scale_factor, fy=scale_factor)
    resized_gray = cv2.resize(image_gray, None, fx=scale_factor, fy=scale_factor)

    # Display the original and grayscale images
    cv2.imshow("Original Image", resized_original)
    cv2.imshow("Grayscale Image", resized_gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")
