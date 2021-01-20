from sys import argv
import cv2
import numpy as np
from imutils import face_utils
import dlib

def rect_to_bb(rect):
	# take a bounding predicted by dlib and convert it
	# to the format (x, y, w, h) as we would normally do with OpenCV
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
	# return a tuple of (x, y, w, h)
	return (x, y, w, h)

detector = dlib.get_frontal_face_detector()

print(argv)
origin = argv[1]
no_blink = argv[2]


f1 = cv2.imread(origin)
f1_gray = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
f2 = cv2.imread(no_blink)

face1 = detector(f1_gray, 1)

mask = 255 * np.ones(f2.shape, f2.dtype)
(x, y, w, h) = face_utils.rect_to_bb(face1[0])
width, height, channels = f1.shape
center = (int(x+w/2),int(y+h/2))
# Seamlessly clone
normal_clone = cv2.seamlessClone(f2, f1, mask, center, cv2.NORMAL_CLONE)

cv2.imwrite("picture/face_swap.jpg", normal_clone )