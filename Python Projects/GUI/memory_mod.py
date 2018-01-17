import sys
from PyQt4 import QtCore, QtGui, uic 
import random
 
from memory_auto import * 
 
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        self.pb1 = ""
        self.pb2 = ""
        self.pb3 = ""
        self.pb4 = ""
        self.c = 0
        self.t1 = ""
        self.t2 = ""
        self.t = 0 
        
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.pb_1, QtCore.SIGNAL('clicked()'), self.b1)
        QtCore.QObject.connect(self.pb_2, QtCore.SIGNAL('clicked()'), self.b2)
        QtCore.QObject.connect(self.pb_3, QtCore.SIGNAL('clicked()'), self.b3)
        QtCore.QObject.connect(self.pb_4, QtCore.SIGNAL('clicked()'), self.b4)
        self.randomise()
    def randomise(self):
        a = random.sample(range(1,5), 4)
        y = 1
        for i in a:
            
            if y == 1 or y == 2:
                a = "CUP"
                if i == 1:
                    self.pb1 = a
                if i == 2:
                    self.pb2 = a
                if i == 3:
                    self.pb3 = a
                if i == 4:
                    self.pb4 = a
            if y == 3 or y == 4:
                a = "TEA"
                if i == 1:
                    self.pb1 = a
                if i == 2:
                    self.pb2 = a
                if i == 3:
                    self.pb3 = a
                if i == 4:
                    self.pb4 = a
            y = y + 1
    def b1(self):
        self.c = 1
        self.pb_1.setText(self.pb1)
        self.t = 0
        if self.t == 0:
            self.t1 = self.pb1
            self.t = 1
        elif self.t == 1:
            self.t2 = self.pb1
            self.t = 0
            if self.t1 == self.t2:
                QtGui.QMessageBox.about(self, "END", "You WIN!!!")
                self.restart()
                
            if self.c == 1:
                QtGui.QMessageBox.about(self, "END", "You LOSE!!!")
                self.c = 0
                self.restart()
            #else:
            #    self.refresh()
            #    self.c = 1
    def b2(self):
        self.c = 1
        self.pb_2.setText(self.pb2)
        if self.t == 0:
            self.t1 = self.pb2
            self.t = 1
        elif self.t == 1:
            self.t2 = self.pb2
            self.t = 0
            if self.t1 == self.t2:
                QtGui.QMessageBox.about(self, "END", "You WIN!!!")
                self.restart()
                
            if self.c == 1:
                QtGui.QMessageBox.about(self, "END", "You LOSE!!!")
                self.c = 0
                self.restart()
            #else:
            #    self.refresh()
            #    self.c = 1
    def b3(self):
        self.c = 1
        self.pb_3.setText(self.pb3)
        if self.t == 0:
            self.t1 = self.pb3
            self.t = 1
        elif self.t == 1:
            self.t2 = self.pb3
            self.t = 0
            if self.t1 == self.t2:
                QtGui.QMessageBox.about(self, "END", "You WIN!!!")
                self.restart()
                
            if self.c == 1:
                QtGui.QMessageBox.about(self, "END", "You LOSE!!!")
                self.c = 0
                self.restart()
            #else:
            #    self.refresh()
            #   self.c = 1
    def b4(self):
        self.c = 1
        self.pb_4.setText(self.pb4)
        if self.t == 0:
            self.t1 = self.pb4
            self.t = 1
        elif self.t == 1:
            self.t2 = self.pb4
            self.t = 0
            if self.t1 == self.t2:
                QtGui.QMessageBox.about(self, "END", "You WIN!!!")
                self.restart()
                
                
            if self.c == 1:
                QtGui.QMessageBox.about(self, "END", "You LOSE!!!")
                self.c = 0
                self.restart()
               
            #else:
             #   self.refresh()
                #self.c = 1
    def refresh(self):
        self.pb_1.setText("")
        self.pb_2.setText("")
        self.pb_3.setText("")
        self.pb_4.setText("")
    def restart(self):
        self.refresh()
        self.randomise()
        self.c = 0

        

         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
