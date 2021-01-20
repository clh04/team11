import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

#資料夾路徑，以防萬一可以檢查一下路徑
blink1 = "blink1"
blink2 = "blink2"
no_blink1 = "no_blink1"
no_blink2 = "no_blink2"
#下面這一行是選擇照片時預設開啟的資料夾，我們預設在下載，是唯一一個非相對路徑，請助教自行重新指定路徑
photo_select = "C:/Users/hp/Downloads"


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("test.ui",self)
        #self.pushButton.clicked.connect(self.browsefiles)
        self.pushButton.setStyleSheet("background-color:powderblue")
        self.pushButton_2.setStyleSheet("background-color:powderblue")
        self.pushButton_3.setStyleSheet("background-color:powderblue")
        #self.Browse.setStyleSheet("background-color:powderblue")
        self.textEdit.setStyleSheet("background-color:cornflowerblue")
        self.textEdit_2.setStyleSheet("background-color:lightsteelblue")
        self.origin_file1 = ""
        self.origin_file2 = ""

        #connet button to function
        self.pushButton.clicked.connect(self.browsefiles1)
        self.pushButton_2.clicked.connect(self.browsefiles2)
        self.pushButton_3.clicked.connect(self.finish)
        
        

    def browsefiles1(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', photo_select)
        self.origin_file1 = fname[0]
        os.system("blink_detection1.py %s" %(fname[0]))
        faces_number1 = str(len(os.listdir(blink1)) + len(os.listdir(no_blink1)))
        blink_number1 = str(len(os.listdir(blink1)))
        self.filename.setText(faces_number1+" faces are found, "+blink_number1+" people blinks")
        self.filename_2.setText(fname[0])
        pixmap = QPixmap("picture/test_result1.jpg")
        widget.setFixedHeight(900)
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)

    def browsefiles2(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', photo_select)
        self.origin_file2 = fname[0]
        os.system("blink_detection2.py %s" %(fname[0]))
        faces_number2 = str(len(os.listdir(blink2)) + len(os.listdir(no_blink2)))
        blink_number2 = str(len(os.listdir(blink2)))
        self.filename_3.setText(faces_number2+" faces are found, "+blink_number2+" people blinks")
        self.filename_4.setText(fname[0])
        pixmap = QPixmap("picture/test_result2.jpg")
        widget.setFixedHeight(900)
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)

    def finish(self):
        if len(os.listdir(blink1)) <= len(os.listdir(blink2)):
            origin = self.origin_file1
            base = blink1
            candidate = no_blink2
        else:
            origin = self.origin_file2
            base = blink2
            candidate = no_blink1
        os.system("compare_face.py %s %s %s" %(base,candidate,origin))
        pixmap = QPixmap("picture/face_swap.jpg")
        widget.setFixedHeight(900)
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True) 



app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(200)
widget.show()
widget.move(400, 50)
sys.exit(app.exec_())



