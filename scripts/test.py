import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray_scaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners_cut = cv2.goodFeaturesToTrack(gray_scaled_image, 100, 0.01, 10)
corners_cut = np.int0(corners_cut)

for corner in corners_cut:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners_cut)):
	for j in range(i + 1, len(corners_cut)):
		corner_cut_1 = tuple(corners_cut[i][0])
		corner_cut_2 = tuple(corners_cut[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(img, corner_cut_1, corner_cut_2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
