import cv2
import random
from random import randrange


# loading the trained data set from the opencv.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# getting live feed form the default webcam or any other video processing programs in your system .
default_v_p = cv2.VideoCapture(0)

# continues the live feed video for ever until we shut it down.
while True:
	
	# reading the frames from the live feed.
	successful_frame_read, frame = default_v_p.read()

	# changing the color for the live feed video to enable the facial detection.
	gray_scale_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# pointing out the coordinate location for face in the image for drawing a rectangle around it.
	face_coordinates = trained_face_data.detectMultiScale(gray_scale_video)

	# looping through multiple human faces in a single frame.
	for (x, y, w, h) in face_coordinates:
		
		# drawing a rectangle around a face
		cv2.rectangle(frame, (x, y), (x+w,y+h), (0, 255, 0), 4)

	# pulling out the frame
	cv2.imshow("Ruthvik", frame)

	# waitkey waits for proccessing the video for 1 second to continue the frames.
	key = cv2.waitKey(1)
	
	# if Q button in keyborad is pressed than the live feed will be terminated.
	# As of ASCII the  number for the character 'Q' is 113.
	if key==81 or key==113:
		break
	
	# Release's thew default_v_p video.
	default_v_p.release()
	
