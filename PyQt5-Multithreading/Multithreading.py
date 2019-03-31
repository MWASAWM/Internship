import threading
import sys
import time
import qdarkstyle
from GUI import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.button_init()

    def button_init(self):
        self.btns.clicked.connect(self.starts)
        self.btnr.clicked.connect(self.startr)
        self.stops.clicked.connect(self.stop_send)
        self.stopr.clicked.connect(self.stop_receive)
        self.alls.clicked.connect(self.all_start)
        self.alle.clicked.connect(self.all_end)

    def starts(self):
        global threads
        threads=sending_thread()
        threads.start()

    def startr(self):
        global threadr
        threadr=receiving_thread()
        threadr.start()

    def stop_send(self):
        threads.stop()

    def stop_receive(self):
        threadr.stop()

    def all_start(self):
        global threads
        threads=sending_thread()
        global threadr
        threadr=receiving_thread()
        threads.start()
        threadr.start()

    def all_end(self):
        threads.stop()
        threadr.stop()

class sending_thread(QThread):

    def __init__(self,parent=None):
        super(sending_thread,self).__init__(parent)
        self.keep=True

    def stop(self):
        self.keep=False

    def run(self):
        while self.keep:
            lockr.acquire()
            print ('sending')
            locks.release()
            self.sleep(1)
        self.keep=True

class receiving_thread(QThread):

    def __init__(self,parent=None):
        super(receiving_thread,self).__init__(parent)
        self.keep=True

    def stop(self):
        self.keep=False

    def run(self):
        while self.keep:
            locks.acquire()
            print ('receiving')
            lockr.release()
            self.sleep(1)
        self.keep=True


if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    win=MainWindow()
    locks=threading.Lock()
    lockr=threading.Lock()
    locks.acquire()
    win.show()
    sys.exit(app.exec_())
