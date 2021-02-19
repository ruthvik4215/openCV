import numpy as np
import cv2

# reads every single frame from the camera.
lf = cv2.VideoCapture(0)

#continue the displaying the video until user press key 'q' on keyboard.
while True:
    
    # reads the frame.
    sf_img_frm_ret, frame = lf.read()
    
    #changing the width of the video captured.
    width = int(lf.get(3))
    
    #changing the height of the video captured.
    height = int(lf.get(4))

    # drawing a line on the video.
    img_draw = cv2.line(frame, (0, 0), (width, height), (255, 120, 221), 10)
    
    #drawing a line perpendicular to the previous line.
    img_draw = cv2.line(img_draw, (0, height), (width, 0), (0, 255, 0), 5)
    
    # drawing a rectangle.
    img_draw = cv2.rectangle(img_draw, (300, 300), (400, 300), (128, 128, 128), 5)
    
    # drawing a circle. 
    img_draw = cv2.circle(img_draw, (300, 300), 60, (94, 23, 167), -1)
    
    #selecting the font to be displayed on the video.
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #placing the text on the video.
    img_draw = cv2.putText(img_draw, 'Ruthvik bemidi!', (20, height - 20), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    #displaying the video.
    cv2.imshow('frame', img_draw)

    # if the user press the key 'q' it exits.
    if cv2.waitKey(1) == ord('q'):
        break

#releases the video.        
lf.release()
cv2.destroyAllWindows()
