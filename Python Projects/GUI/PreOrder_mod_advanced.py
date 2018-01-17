import sys
from PyQt4 import QtCore, QtGui, uic 
 
from PreOrder_auto_advanced import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
   
        QtCore.QObject.connect(self.rb_patties, QtCore.SIGNAL('clicked()'), self.patties)
        QtCore.QObject.connect(self.rb_soup, QtCore.SIGNAL('clicked()'), self.soup) 
        QtCore.QObject.connect(self.cbx_onion, QtCore.SIGNAL('clicked()'), self.onion)
        QtCore.QObject.connect(self.cbx_chillies, QtCore.SIGNAL('clicked()'), self.chillies) 
        QtCore.QObject.connect(self.pb_add, QtCore.SIGNAL('clicked()'), self.add)
        QtCore.QObject.connect(self.pb_delete, QtCore.SIGNAL('clicked()'), self.delete)
        QtCore.QObject.connect(self.pb_remove, QtCore.SIGNAL('clicked()'), self.remove)
        self.cb_main.activated[str].connect(self.cbadd)
        
        
        self.text = []
    
    def patties(self):
        self.text.append("Patties")
    def soup(self):
        self.text.append("Clear soup")
    def onion(self):
        self.text.append("Onion")
    def chillies(self):
        self.text.append("Soup")
    def add(self):
        for i in self.text:
            self.lwi_1.addItem(i)
    def delete(self):
        self.lwi_1.takeItem(self.lwi_1.currentRow())
    def remove(self):
        self.lwi_1.clear()
    def cbadd(self):
        self.lwi_1.addItem(str(self.cb_main.currentText()))
   
        
    
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
