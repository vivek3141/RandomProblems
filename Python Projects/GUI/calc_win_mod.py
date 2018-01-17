import sys
from PyQt4 import QtCore, QtGui, uic 
 
from calc_win_auto import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.his = ""
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL('clicked()'), self.calculate)
        QtCore.QObject.connect(self.actionAdd, QtCore.SIGNAL('triggered()'), self.add)
        QtCore.QObject.connect(self.actionSub, QtCore.SIGNAL('triggered()'), self.sub)
        QtCore.QObject.connect(self.actionMul, QtCore.SIGNAL('triggered()'), self.mul)
        QtCore.QObject.connect(self.actionDiv, QtCore.SIGNAL('triggered()'), self.div)
        QtCore.QObject.connect(self.pb_add, QtCore.SIGNAL('clicked()'), self.add)
        QtCore.QObject.connect(self.pb_sub, QtCore.SIGNAL('clicked()'), self.sub)
        QtCore.QObject.connect(self.pb_mul, QtCore.SIGNAL('clicked()'), self.mul)
        QtCore.QObject.connect(self.pb_div, QtCore.SIGNAL('clicked()'), self.div)
        QtCore.QObject.connect(self.pb_1, QtCore.SIGNAL('clicked()'), self._1)
        QtCore.QObject.connect(self.pb_2, QtCore.SIGNAL('clicked()'), self._2)
        QtCore.QObject.connect(self.pb_3, QtCore.SIGNAL('clicked()'), self._3)
        QtCore.QObject.connect(self.pb_4, QtCore.SIGNAL('clicked()'), self._4)
        QtCore.QObject.connect(self.pb_5, QtCore.SIGNAL('clicked()'), self._5)
        QtCore.QObject.connect(self.pb_6, QtCore.SIGNAL('clicked()'), self._6)
        QtCore.QObject.connect(self.pb_7, QtCore.SIGNAL('clicked()'), self._7)
        QtCore.QObject.connect(self.pb_8, QtCore.SIGNAL('clicked()'), self._8)
        QtCore.QObject.connect(self.pb_9, QtCore.SIGNAL('clicked()'), self._9)
        QtCore.QObject.connect(self.pb_0, QtCore.SIGNAL('clicked()'), self._0)
        QtCore.QObject.connect(self.pb_C, QtCore.SIGNAL('clicked()'), self._C)
        QtCore.QObject.connect(self.pb_CE, QtCore.SIGNAL('clicked()'), self._CE)
        self.res = 0 
        self.his = ""
        self.str = ""
    def append(self, a):
        self.his = self.his + str(a)
        self.lineEdit.setText(str(self.lineEdit.text()) + str(a))
        
    def _1(self):

        self.append(1)
    def _2(self):

        self.append(2)
    def _3(self):

        self.append(3)
    def _4(self):
 
        self.append(4)
    def _5(self):

        self.append(5)
    def _6(self):

        self.append(6)
    def _7(self):

        self.append(7)
    def _8(self):

        self.append(8)
    def _9(self):

        self.append(9)
    def _0(self):
        self.append(0)
    def _C(self):
        self.lineEdit.setText("")
        self.res = 0
        self.his = ""
    
    def _CE(self):
        self.lineEdit.setText("")
        self.his = ""
    def calculate(self):
        self.lineEdit.setText(str(eval(self.lineEdit.text())))
    def add(self):
        self.append("+")
    def sub(self):
        self.append("-")
    def mul(self):
        self.append("*")
    def div(self):
        self.append("/")
    
        
           
            
            
            
            
            
        
        
        
        
 	     
         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
