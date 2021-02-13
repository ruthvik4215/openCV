import cv2
import random
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

while True:

	successful_frame_read, frame = webcam.read()

	grayscale_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	face_coordinates = trained_face_data.detectMultiScale(grayscale_video)

	for (x, y, w, h) in face_coordinates:
		cv2.rectangle(frame, (x, y), (x+w,y+h), (0, 255, 0), 4)

	cv2.imshow("Ruthvik", frame)

	cv2.waitKey(1)