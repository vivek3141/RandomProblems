import sys
from PyQt4 import QtCore, QtGui, uic 

 
from Quiz_auto import * 
  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        self.times = 0
        self.score = 0
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.btn_submit, QtCore.SIGNAL('clicked()'), self.submit)
        QtCore.QObject.connect(self.btn_next, QtCore.SIGNAL('clicked()'), self.next)
    def next(self):
        
        if(str(self.lne_modi.text()) == "F" or str(self.lne_modi.text()) == "f" ):
            self.score = self.score + 1
        if(str(self.lne_w10.text()) == "T" or str(self.lne_w10.text()) == "t" ):
            self.score = self.score + 1
        if(str(self.lne_ap.text()) == "F" or str(self.lne_ap.text()) == "f" ):
            self.score = self.score + 1
        self.lbl_modi.setText("PyQt4 is a single platform toolkit(T/F)?")
        self.lbl_w10.setText("The no. of electrons in Al is 17(T/F)?")
        self.lbl_ap.setText("The last noble gas is Rn(T/F)?")
        self.lne_modi.setText("")
        self.lne_w10.setText("")
        self.lne_ap.setText("")
        self.times = self.times + 1
        self.lbl_score.setText("Your Score:"+str(self.score))
        QtGui.QMessageBox.about(self, "Result?", "Your score is currently " + str(self.score))
        
    
        
    def submit(self):
        self.btn_next.hide()
        if(str(self.lne_modi.text()) == "F" or str(self.lne_modi.text()) == "f" ):
            self.score = self.score + 1
        if(str(self.lne_w10.text()) == "T" or str(self.lne_w10.text()) == "t" ):
            self.score = self.score + 1
        if(str(self.lne_ap.text()) == "F" or str(self.lne_ap.text()) == "f" ):
            self.score = self.score + 1
        self.lbl_modi.setText("")
        self.lbl_w10.setText("")
        self.lbl_ap.setText("")
        self.lne_modi.setText("")
        self.lne_w10.setText("")
        self.lne_ap.setText("")
        QtGui.QMessageBox.about(self, "Result?", "Your score is " + str(self.score) + ". Thank you for taking this test")    
   
        
 	     
         

if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_() 
