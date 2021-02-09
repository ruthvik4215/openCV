import numpy as np
import cv2

img = cv2.imread("logo.jpeg", 0)
img = cv2.resize(img, (0, 0), fx=2, fy=2)

cv2.imwrite("new_color_logo.jpeg", img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()