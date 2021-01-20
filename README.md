# team11
109-1 programming final project

# reproduce
* install module
  * dlib
  * opencv

* 新增picture資料夾(與程式檔案同層)
* gui.py


# 需改動的程式碼
* blink_detection1.py
  * 第51行
    ```
    predictor = dlib.shape_predictor("C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\dlib\shape_predictor_68_face_landmarks.dat")
    ```
    > filepath改成正確的 dlib\shape_predictor_68_face_landmarks.dat 所在位置
    
* blink_detection2.py
  * 第51行
    ```
    predictor = dlib.shape_predictor("C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\dlib\shape_predictor_68_face_landmarks.dat")
    ```
    > filepath改成正確的 dlib\shape_predictor_68_face_landmarks.dat 所在位置
    
* gui.py
  * 第35, 36, 39, 48, 49, 52, 58, 60, 61, 64, 65, 67行
    > filepath 改成正確路徑
  
* compare_face.py
  * 第39行
    ```
    a = cv2.imread("C:/Users/hp/Desktop/project1/spongebob.jpg")
    ```
    > 選一張"如果沒有需要替換的人臉"會顯示的圖片
    > 並放上正確路徑
    
  * 第40行
    ```
    cv2.imwrite("C:/Users/hp/Desktop/project1/picture/face_swap.jpg", a)        
    ```
    > filepath 改成正確路徑
  
* face_swap.py
  * 第37行
    ```
    cv2.imwrite("picture/face_swap.jpg", normal_clone )
    ```
    > filepath 改成正確路徑





