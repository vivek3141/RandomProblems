import sys
from PyQt4 import QtCore, QtGui, uic 
 
from String_auto import * 
from String_Handling import *
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.actionE, QtCore.SIGNAL('triggered()'), self.e)
        QtCore.QObject.connect(self.actionForb, QtCore.SIGNAL('triggered()'), self.fob)

        QtCore.QObject.connect(self.rb_e, QtCore.SIGNAL('clicked()'), self.e_2)
        QtCore.QObject.connect(self.rb_fob,  QtCore.SIGNAL('clicked()'), self.fob_2)
        
    def e(self):
        b = has_no_e_percent(self.txe.toPlainText())
        a = has_no_e_mod(self.txe.toPlainText())
        print(str(a))
        self.lbl_main.setText("Words which do not have e:" + str(a) +"; Percentage without e:" + str(b))
    def e_2(self):
        self.lbl_1.hide()
        self.lne.hide()
        self.lbl_2.setText("Sentence:?")
    def fob_2(self):
        self.lbl_1.show()
        self.lne.show()
        self.lbl_2.setText("Sentence:?")
        self.lbl_1.setText("Forbidden:")
    def fob(self):
        
        a = avoids_mod(self.txe.toPlainText(), self.lne.text())
        print(str(a))
        self.lbl_main.setText("Words which do not have the letters:" + str(a) )
    
 	     
         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
