import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5 import uic
import re
import datetime
from lib.You_Viewer_Layout import Ui_MainWindow
from lib.AuthDialog import AuthDialog

# form_class=uic.loadUiType('D:/section6/ui/you_viewer_v1.0.ui')[0]
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 초기화
        self.setupUi(self)
        # 인증버튼 이벤트 전
        self.initAuthLock()
        # 인증버튼 이벤트 후
        self.initAuthActive()
        # 시그널 초기화
        self.initSignal()
        # 로그인 관련 변수방
        self.user_id=None
        self.user_pw=None


    # 기본 UT 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.StreamComboBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')


    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.StreamComboBox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    # 시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)

    @pyqtSlot() # 명시적으로 유지보수 때문에 만듬
    def authCheck(self):
        pass


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()
