import sys
from PyQt4 import QtCore, QtGui, uic 
 
from calc_auto import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.pb_calc, QtCore.SIGNAL('clicked()'), self.calculate)
        QtCore.QObject.connect(self.actionAdd, QtCore.SIGNAL('triggered()'), self.add)
        QtCore.QObject.connect(self.actionSub, QtCore.SIGNAL('triggered()'), self.sub)
        QtCore.QObject.connect(self.actionMul, QtCore.SIGNAL('triggered()'), self.mul)
        QtCore.QObject.connect(self.actionDiv, QtCore.SIGNAL('triggered()'), self.div)
        self.res = 0 
        self.rb_add.setChecked(True)
        self.lne_f1_1.setFocus(True)
    def calculate(self):
        
        try:
            fnum = float(self.lne_f1_1.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f1_1.setText("")
            self.lne_f1_1.setFocus(True)
            return False
        try:
            snum=float(self.lne_f2_3.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f2_3.setText("")
            self.lne_f2_3.setFocus(True)
            return False
            
        if self.rb_add.isChecked() == True:
            self.res =  fnum + snum
        if self.rb_sub.isChecked() == True:
            self.res = fnum - snum
        if self.rb_multiply.isChecked() == True:
            self.res = fnum * snum
        if self.rb_divide.isChecked() == True:
            try:
                self.res = fnum / snum
            except ZeroDivisionError:
                QtGui.QMessageBox.warning(self, "error","Please do not divide by 0")
                return False
                
        self.lne_r_1.setText(str(self.res))
        self.lne_r_2.setText(str(self.res))
        self.lne_f1_2.setText(str(self.lne_f1_1.text()))
        self.lne_f2_2.setText(str(self.lne_f2_3.text()))
        self.lne_f1_1.setText(str(self.lne_r_1.text()))
        self.lne_f2_3.setText("")
        self.lne_f2_3.setFocus(True)
    def add(self):
        
        try:
            fnum = float(self.lne_f1_1.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f1_1.setText("")
            self.lne_f1_1.setFocus(True)
            return False
        try:
            snum=float(self.lne_f2_3.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f2_3.setText("")
            self.lne_f2_3.setFocus(True)
            return False
            
        
        self.res =  fnum + snum
        
                
        self.lne_r_1.setText(str(self.res))
        self.lne_r_2.setText(str(self.res))
        self.lne_f1_2.setText(str(self.lne_f1_1.text()))
        self.lne_f2_2.setText(str(self.lne_f2_3.text()))
        self.lne_f1_1.setText(str(self.lne_r_1.text()))
        self.lne_f2_3.setText("")
        self.lne_f2_3.setFocus(True)
        self.rb_add.setChecked(True)
    def sub(self):
        
        try:
            fnum = float(self.lne_f1_1.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f1_1.setText("")
            self.lne_f1_1.setFocus(True)
            return False
        try:
            snum=float(self.lne_f2_3.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f2_3.setText("")
            self.lne_f2_3.setFocus(True)
            return False
            
       
        self.res = fnum - snum
      
                
        self.lne_r_1.setText(str(self.res))
        self.lne_r_2.setText(str(self.res))
        self.lne_f1_2.setText(str(self.lne_f1_1.text()))
        self.lne_f2_2.setText(str(self.lne_f2_3.text()))
        self.lne_f1_1.setText(str(self.lne_r_1.text()))
        self.lne_f2_3.setText("")
        self.lne_f2_3.setFocus(True)
        self.rb_sub.setChecked(True)
    def div(self):
        
        try:
            fnum = float(self.lne_f1_1.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f1_1.setText("")
            self.lne_f1_1.setFocus(True)
            return False
        try:
            snum=float(self.lne_f2_3.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f2_3.setText("")
            self.lne_f2_3.setFocus(True)
            return False
            
        
        try:
            self.res = fnum / snum
        except ZeroDivisionError:
            QtGui.QMessageBox.warning(self, "error","Please do not divide by 0")
            return False
                
        self.lne_r_1.setText(str(self.res))
        self.lne_r_2.setText(str(self.res))
        self.lne_f1_2.setText(str(self.lne_f1_1.text()))
        self.lne_f2_2.setText(str(self.lne_f2_3.text()))
        self.lne_f1_1.setText(str(self.lne_r_1.text()))
        self.lne_f2_3.setText("")
        self.lne_f2_3.setFocus(True)
        self.rb_divide.setChecked(True)
    def mul(self):
        
        try:
            fnum = float(self.lne_f1_1.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f1_1.setText("")
            self.lne_f1_1.setFocus(True)
            return False
        try:
            snum=float(self.lne_f2_3.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "error","Please enter a valid number")
                  
            self.lne_f2_3.setText("")
            self.lne_f2_3.setFocus(True)
            return False
            
        
        self.res = fnum * snum
        
                
        self.lne_r_1.setText(str(self.res))
        self.lne_r_2.setText(str(self.res))
        self.lne_f1_2.setText(str(self.lne_f1_1.text()))
        self.lne_f2_2.setText(str(self.lne_f2_3.text()))
        self.lne_f1_1.setText(str(self.lne_r_1.text()))
        self.lne_f2_3.setText("")
        self.lne_f2_3.setFocus(True)
        self.rb_multiply.setChecked(True)
        
 
    
        
           
            
            
            
            
            
        
        
        
        
 	     
         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
