import sys
from PyQt4 import QtCore, QtGui, uic 
 
from laluprasad import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.abc, QtCore.SIGNAL('clicked()'), self.abc_2)
    def abc_2(self):
        self.hi.setChecked(False)
        a = self.abc
        a.setText("YAM")
 	     
         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
