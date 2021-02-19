import numpy as np
import cv2

lf = cv2.VideoCapture(0)

while True:
    sf_img_frm_ret, frame = lf.read()
    width = int(lf.get(3))
    height = int(lf.get(4))

    img_draw = cv2.line(frame, (0, 0), (width, height), (255, 120, 221), 10)
    img_draw = cv2.line(img_draw, (0, height), (width, 0), (0, 255, 0), 5)
    img_draw = cv2.rectangle(img_draw, (300, 300), (400, 300), (128, 128, 128), 5)
    img_draw = cv2.circle(img_draw, (300, 300), 60, (94, 23, 167), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img_draw = cv2.putText(img_draw, 'Ruthvik bemidi!', (20, height - 20), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img_draw)

    if cv2.waitKey(1) == ord('q'):
        break

lf.release()
cv2.destroyAllWindows()
