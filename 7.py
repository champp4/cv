import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)
triangle = np.array([[250, 50], [50, 450], [450, 450]], dtype=np.int32)
centroid = np.mean(triangle, axis=0, dtype=np.int32)

cv2.polylines(image, [triangle], isClosed=True, color=(0, 255, 0), thickness=2)
cv2.circle(image, tuple(centroid), radius=5, color=(0, 0, 255), thickness=-1)
cv2.imshow("Triangle with Centroid", image)

def change_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.polylines(image, [triangle], isClosed=True, color=np.random.randint(0, 256, size=3).tolist(), thickness=2)
        cv2.circle(image, tuple(centroid), radius=5, color=(0, 0, 255), thickness=-1)
        cv2.imshow("Triangle with Centroid", image)

cv2.setMouseCallback("Triangle with Centroid", change_color)

while cv2.waitKey(1) & 0xFF != ord('q'):
    pass

cv2.destroyAllWindows()
