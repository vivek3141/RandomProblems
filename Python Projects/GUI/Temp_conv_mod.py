import sys
from PyQt4 import QtCore, QtGui, uic 
 
from Temp_conv_auto import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.btn_C_to_F, QtCore.SIGNAL('clicked()'), self.C_to_F)
        QtCore.QObject.connect(self.btn_F_to_C, QtCore.SIGNAL('clicked()'), self.F_to_C)
        QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL('clicked()'), self.clear)
    def C_to_F(self):
        a = float(self.lne_C.text())
        c = (a*9/5)+32
        self.sb_F.setValue(int(c))
    def F_to_C(self):
        a = float(self.sb_F.value())
        f = (a-32)*5/9
        self.lne_C.setText(str(f))
    def clear(self):
        self.lne_C.setText("")
        self.sb_F.setValue(0)

if (__name__ == "__main__"):
    print("Barney")
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_() 
