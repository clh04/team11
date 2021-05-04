# team11
109-1 programming final project
project video https://www.youtube.com/watch?v=cUxxNwhWvkg

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
   (預設照片存於Downloads資料夾)
* 在project裡，創建5個新資料夾：
  * picture
  * blink1
  * blink2
  * no_blink1
  * no_blink2
* run gui.py

# 可能需要更改的程式
## 提醒：所有的路徑只能用英文命名，且不能包含空格
* blink_detection1.py
  * line 10
  ```
    shape_predictor_68_face_landmarks = "shape_predictor_68_face_landmarks.dat"
  ```
     >> 須確認shape_predictor_68_face_landmarks.dat和blink_detection1.py同層
* blink_detection2.py
  * line 10
  ```
    shape_predictor_68_face_landmarks = "shape_predictor_68_face_landmarks.dat"
  ```
     >> 須確認shape_predictor_68_face_landmarks.dat和blink_detection2.py同層

* gui.py
  * line 14
  ```
    photo_select = "C:/Users/hp/Downloads"
  ```
  >> 路徑："想要p圖的照片"所在資料夾

# 備註
>若dlib內找不到shape_predictor_68_face_landmarks.dat
可從：https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2 下載

>安裝dlib、face recognition 之前要先安裝Visual Studio (因為這些是c++的套件所以要有c++的環境)


