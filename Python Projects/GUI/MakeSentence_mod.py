import sys
from PyQt4 import QtCore, QtGui, uic 
 
from MakeSentence_auto import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.cbx_badi, QtCore.SIGNAL('clicked()'), self.badi)
        QtCore.QObject.connect(self.cbx_cricket, QtCore.SIGNAL('clicked()'), self.cricket)
        QtCore.QObject.connect(self.cbx_swim, QtCore.SIGNAL('clicked()'), self.swim) 
        QtCore.QObject.connect(self.rb_npshsr, QtCore.SIGNAL('clicked()'), self.npshsr)
        QtCore.QObject.connect(self.rb_npsinr, QtCore.SIGNAL('clicked()'), self.npsinr) 
        QtCore.QObject.connect(self.rb_tisb, QtCore.SIGNAL('clicked()'), self.tisb)
        QtCore.QObject.connect(self.pb_mks, QtCore.SIGNAL('clicked()'), self.makeSent)
        self.a = ""
        self.b = ""
        self.text = ""
    def badi(self):
        self.a = self.a+",badminton"
    def cricket(self):
        self.a = self.a + ",cricket"
    def swim(self):
        self.a = self.a + ",swimming"
    def npshsr(self):
        self.b = " NPS HSR"
    def npsinr(self):
        self.b = " NPS INR"
    def tisb(self):
        self.b = " TISB"
    def makeSent(self):
        self.txe_sent.setText("")
        z = str(self.tne_fname.text() + "" + self.lne_lname.text() + " loves " + self.a + " and goes to" + self.b +".")
        self.txe_sent.setText(z)
         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
