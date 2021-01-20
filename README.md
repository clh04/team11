# team11
109-1 programming final project

# reproduce
* install module
  * opencv
  * pyqt5
  ```
     pip install PyQt5
  ```
  * imutils
  ```
     pip install imutils
  ```
  * face_recognition
  ```
     pip install face-recognition
  ```
  * dlib
  ```
     pip install dlib
  ```
* 下載好想要p圖的兩張照片
* 在project1裡，創建5個新資料夾：
  * picture
  * blink1
  * blink2
  * no_blink1
  * no_blink2
* run gui.py

# 需要更改的程式
## 提醒：所有的路徑只能用英文命名，且不能包含空格
* blink_detection1.py
  * line 10
  ```
    shape_predictor_68_face_landmarks = "C:\\Users\\hp\\Desktop\\project1\\shape_predictor_68_face_landmarks.dat"
  ```
     >> filepath須改為正確路徑
* blink_detection2.py
  * line 10
  ```
    shape_predictor_68_face_landmarks = "C:\\Users\\hp\\Desktop\\project1\\shape_predictor_68_face_landmarks.dat"
  ```
     >> filepath須改為正確路徑

* gui.py
  * line 14
  ```
    photo_select = "C:/Users/hp/Downloads"
  ```
  >> 存取"想要p圖的照片"的資料夾





