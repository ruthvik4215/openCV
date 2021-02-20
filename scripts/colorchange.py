import numpy as np
import cv2

lf_video = cv2.VideoCapture(0)

while True:
    ret, frame = lf_video.read()
    width = int(lf_video.get(3))
    height = int(lf_video.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_light_blue_50 = np.array([90, 50, 50])
    upper_light_blue_255 = np.array([130, 255, 255])

    face_mask_color = cv2.inRange(hsv, lower_light_blue_50, upper_light_blue_255)

    result_mask = cv2.bitwise_and(frame, frame, face_mask_color=face_mask_color)

    cv2.imshow('frame', result_mask)
    cv2.imshow('mask', result_mask)

    if cv2.waitKey(1) == ord('q'):
        break

lf_video.release()
cv2.destroyAllWindows()
