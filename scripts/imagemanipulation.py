import cv2
import random

# color inversion or reading the image.
tryn_logo = cv2.imread("./images/logo.jpeg", -1)
# resizing the array of image
tryn_logo = cv2.resize(tryn_logo, (0, 0), fx=3, fy=3)
# changing the BGR of the pixel
for x in range(167):
	for y in range(tryn_logo[1]):
		tryn_logo[x][y] = [random.randint(19, 234), random.randint(89, 178), random.randint(101, 229)]

# copying the part of image and pasting it in another part
copy_paste_logo = tryn_logo[423:623, 571:871]
tryn_logo[123:323, 593:893] = copy_paste_logo


cv2.imshow("Try logo", tryn_logo)
cv2.waitKey(0)
cv2.destroyAllWindows()