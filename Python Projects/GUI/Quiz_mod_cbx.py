import sys
from PyQt4 import QtCore, QtGui, uic 

 
from Quiz_auto_cbx import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        
        self.score = 0
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        self.rb_2_1.hide()
        self.rb_2_2.hide()
        QtCore.QObject.connect(self.btn_submit, QtCore.SIGNAL('clicked()'), self.submit)
        QtCore.QObject.connect(self.btn_next, QtCore.SIGNAL('clicked()'), self.next)
    def next(self):
 
        if(self.rb_2.isChecked() == True):
            self.score = self.score + 1
        if(self.rb_3.isChecked() == True):
            self.score = self.score + 1
        if(self.rb_6.isChecked() == True):
            self.score = self.score + 1
        self.lbl_modi.setText("PyQt4 is a single platform toolkit(T/F)?")
        self.lbl_w10.setText("The no. of electrons in Al is 17(T/F)?")
        self.lbl_ap.setText("The last noble gas is Rn(T/F)?")
        
        print(self.radioButton.isChecked())
        self.rb_2_1.show()
        self.rb_2_2.show()
#        self.radioButton.setChecked(False)
#        self.rb_2.setChecked(False)
#        self.rb_3.setChecked(0)
#        self.rb_4.setChecked(False)
#        self.rb_5.setChecked(0)
#        self.rb_6.setChecked(0)
       
        self.lbl_score.setText("Your Score:"+str(self.score))
        QtGui.QMessageBox.about(self, "Result?", "Your score is currently " + str(self.score))
        self.btn_next.hide()
    
        
    def submit(self):
        self.btn_next.hide()
        if(self.rb_2.isChecked() == True):
            self.score = self.score + 1
        if(self.rb_3.isChecked() == True):
            self.score = self.score + 1
        if(self.rb_6.isChecked() == True):
            self.score = self.score + 1
        self.lbl_modi.setText("")
        self.lbl_w10.setText("")
        self.lbl_ap.setText("")
        self.lbl_score.setText("Your Score:"+str(self.score))
        self.radioButton.setChecked(False)
        self.rb_2.setChecked(False)
        self.rb_3.setChecked(False)
        self.rb_4.setChecked(False)
        self.rb_5.setChecked(False)
        self.rb_6.setChecked(False)
        QtGui.QMessageBox.about(self, "Result?", "Your score is " + str(self.score) + ". Thank you for taking this test")    
   
        
 	     
         

if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_() 
