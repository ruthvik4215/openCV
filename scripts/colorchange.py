import numpy as np
import cv2

# getting live video from camera.
lf_video = cv2.VideoCapture(0)

#loops through evrry single frame.
while True:
    
    # reads the frame.
    ret, frame = lf_video.read()
    
    #adusting the width and height of the video.
    width = int(lf_video.get(3))
    height = int(lf_video.get(4))

    #changing the original frame color to hsv color .
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #fixing the lower bound color and upper bound color.
    lower_light_blue_50 = np.array([90, 50, 50])
    upper_light_blue_255 = np.array([130, 255, 255])

    # selecting the specific color(or color range) for showing on the video(or in pixels).
    face_mask_color = cv2.inRange(hsv, lower_light_blue_50, upper_light_blue_255)

    #displays specific pixels if gievn color is in the frame(or video).
    result_mask = cv2.bitwise_and(frame, frame, face_mask_color=face_mask_color)

    #displaying the video.
    cv2.imshow('frame', result_mask)
    cv2.imshow('mask', result_mask)

    #stops displaying the video if user press the key 'q'.
    if cv2.waitKey(1) == ord('q'):
        break

#releases the video after user press the key 'q'.
lf_video.release()
cv2.destroyAllWindows()
