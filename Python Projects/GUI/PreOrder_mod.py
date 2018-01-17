import sys
from PyQt4 import QtCore, QtGui, uic 
 
from PreOrder_auto import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.pb_process, QtCore.SIGNAL('clicked()'), self.process)
        QtCore.QObject.connect(self.rb_mr, QtCore.SIGNAL('clicked()'), self.mr)
        QtCore.QObject.connect(self.rb_ms, QtCore.SIGNAL('clicked()'), self.ms) 
        QtCore.QObject.connect(self.rb_patties, QtCore.SIGNAL('clicked()'), self.patties)
        QtCore.QObject.connect(self.rb_soup, QtCore.SIGNAL('clicked()'), self.soup) 
        QtCore.QObject.connect(self.cbx_onion, QtCore.SIGNAL('clicked()'), self.onion)
        QtCore.QObject.connect(self.cbx_chillies, QtCore.SIGNAL('clicked()'), self.chillies) 
        self.text = ""
    def mr(self):
        self.text = self.text + "Mr."
        self.text = self.text + self.lne_name.text()
    def ms(self):
        self.text = self.text + "Ms."
        self.text = self.text + self.lne_name.text()
    def patties(self):
        self.text = self.text + "Patties"
    def soup(self):
        self.text = self.text + "Clear soup"
    def onion(self):
        self.text = self.text + "Onion"
    def chillies(self):
        self.text = self.text + "Soup"
    def process(self):
        self.text = self.text + str(self.sb_1.value())
        self.text = self.text + str(self.dsb_1.value())
        QtGui.QMessageBox.about(self, "Result?", self.text)
   
        
    
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
