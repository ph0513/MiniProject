import sys
import io
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class TestForm(QMainWindow): # PyQT5.QtWidgets에서 상속됨
    #생성자
    def __init__(self):
        super().__init__() # 부모의 생성자 함수 호출
        self.setupUI() # 함수 선언
    def setupUI(self):
        self.setWindowTitle("PyQT test") # 제목 표시줄
        self.setGeometry(800,400,500,500) # 윈도우화면상의 위치 800 400에 500,300 창 크기

        label_1=QLabel("입력 테스트",self)
        label_2=QLabel("출력 테스트",self)

        label_1.move(20,20)
        label_2.move(20,60)

        self.lineEdit=QLineEdit("",self) # "" 초기값
        self.plainEdit=QtWidgets.QPlainTextEdit(self)

        self.lineEdit.move(110,20)
        self.plainEdit.setGeometry(QtCore.QRect(20,90,360,230))
        # self.plainEdit.setReadOnly(True) # 읽기 전용(쓰기 방지)

        self.lineEdit.textChanged.connect(self.lineEditChanged) # 시그널
        self.lineEdit.returnPressed.connect(self.lineEditor)

        self.statusBar=QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text()) # 슬롯

    def lineEditor(self):
        self.plainEdit.appendPlainText(self.lineEdit.text())
        self.lineEdit.clear() # 메모리 해제 / 엔터후 글씨 클리어

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
