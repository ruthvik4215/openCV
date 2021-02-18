import numpy as np
import cv2

# reads the 1ms frame from the video.
liveFootage = cv2.VideoCapture(0)

#loops through the every single frame.
while True:

    #read the footage.
    retx_x, frame = liveFootage.read()
    
    #dividing the original video into four individual frames.
    width = int(cap.get(3))
    height = int(cap.get(4))

    image_size = np.zeros(frame.shape, np.uint8)
    
    resizing_frame_into_four = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    image_size[:height//2, :width//2] = cv2.rotate(resizing_frame_into_four, cv2.cv2.ROTATE_180)
    
    image_size[height//2:, :width//2] = resizing_frame_into_four
    
    image_size[:height//2, width//2:] = cv2.rotate(resizing_frame_into_four, cv2.cv2.ROTATE_180)
    
    image_size[height//2:, width//2:] = resizing_frame_into_four

    cv2.imshow('frame', image_size)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
