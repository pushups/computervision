import sys
import cv2
import numpy as np

filename = sys.argv[1]

cap = cv2.VideoCapture(filename)

last_frame = None

frame_buffer = []

_, frame = cap.read()

num_frames = 1

while(True):
	# Capture frame-by-frame
	_, new_frame = cap.read()
	num_frames += 1

	if num_frames >= 2:
		frame = cv2.addWeighted(frame, 0.9, new_frame, 0.1, 0)

	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
