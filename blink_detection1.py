from sys import argv
import cv2
import dlib
import math
from imutils import face_utils
import shutil
import os

#此為自行下載的檔案，有可能出錯，可以上網自行下載不同的版本嘗試
shape_predictor_68_face_landmarks = "shape_predictor_68_face_landmarks.dat"

#刪除後建立資料夾
#有時會出錯還請助教手動自行建立，否則會出錯
shutil.rmtree('blink1')
shutil.rmtree('no_blink1')
os.mkdir('blink1')
os.mkdir('no_blink1')


BLINK_RATIO_THRESHOLD = 5.5

def midpoint(point1 ,point2):
    return (point1.x + point2.x)/2,(point1.y + point2.y)/2

def euclidean_distance(point1 , point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_blink_ratio(eye_points, facial_landmarks):
    
    #loading all the required points
    corner_left  = (facial_landmarks.part(eye_points[0]).x, 
                    facial_landmarks.part(eye_points[0]).y)
    corner_right = (facial_landmarks.part(eye_points[3]).x, 
                    facial_landmarks.part(eye_points[3]).y)
    
    center_top    = midpoint(facial_landmarks.part(eye_points[1]), 
                             facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), 
                             facial_landmarks.part(eye_points[4]))

    #calculating distance
    horizontal_length = euclidean_distance(corner_left,corner_right)
    vertical_length = euclidean_distance(center_top,center_bottom)

    ratio = horizontal_length / vertical_length

    return ratio

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
predictor = dlib.shape_predictor(shape_predictor_68_face_landmarks)

#these landmarks are based on the dlib shape_predictor
left_eye_landmarks  = [36, 37, 38, 39, 40, 41,36]
right_eye_landmarks = [42, 43, 44, 45, 46, 47,42]

f = argv[1]
img = cv2.imread(f)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces1 = detector(img_gray, 1)



count_all = 0
count_blink = 0

#detect the faces 
#classify and save
#show who blinks or not 
for rect in faces1:
    landmarks = predictor(img, rect)
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    #Calculating blink ratio for one eye
    left_eye_ratio  = get_blink_ratio(left_eye_landmarks, landmarks)
    right_eye_ratio = get_blink_ratio(right_eye_landmarks, landmarks)
    blink_ratio     = (left_eye_ratio + right_eye_ratio) / 2

    if blink_ratio > BLINK_RATIO_THRESHOLD:
        face = img[y:y+h, x:x+w]
        cv2.imwrite("blink1/%s.jpg" %count_all, face)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        count_blink += 1
    else:
        face = img[y:y+h, x:x+w]
        cv2.imwrite("no_blink1/%s.jpg" %count_all, face)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    count_all += 1

cv2.imwrite("picture/test_result1.jpg", img )
