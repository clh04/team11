import face_recognition
import os
from sys import argv
import cv2

#眨眼與沒有眨眼的人臉照片位置
blink = argv[1]
no_blink = argv[2]
origin = argv[3]
results = []


#tolerance: How much distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.
#試了一下覺得0.35比較好
Tolerance = 0.35


for i in os.listdir(blink):
    blink_image_idx = blink + i 
    blink_image = face_recognition.load_image_file(blink_image_idx) 
    try:
        blink_encoding = face_recognition.face_encodings(blink_image)[0]  
    except:
        continue
    for j in os.listdir(no_blink):
        no_blink_image_idx = no_blink + j        
        no_blink_image = face_recognition.load_image_file(no_blink_image_idx)
        try:
            no_blink_encoding = face_recognition.face_encodings(no_blink_image)[0]
        except:
            continue

        if face_recognition.compare_faces([no_blink_encoding], blink_encoding,tolerance = Tolerance)[0] == True:
            results.append(no_blink_image_idx)
            os.system("face_swap.py %s %s" %(origin,no_blink_image_idx))
        else:
            continue
if results == []:
    a = cv2.imread("C:/Users/hp/Desktop/project1/spongebob.jpg")
    cv2.imwrite("C:/Users/hp/Desktop/project1/picture/face_swap.jpg", a)        
