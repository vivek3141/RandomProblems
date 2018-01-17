import sys
from Sale_calc_auto import * 
 
class MyForm(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        QtCore.QObject.connect(self.ui.pb_calc, QtCore.SIGNAL('clicked()'), self.btn_calculate)
        QtCore.QObject.connect(self.ui.pb_clear, QtCore.SIGNAL('clicked()'), self.clear)
    
    def btn_calculate(self):
        a = float(self.ui.ln_unit.text())
        b = float(self.ui.ln_no.text())
        c = float(self.ui.ln_dis.text())
        d = a*b
        e = d -(d*(c/100))
        
        self.ui.lbl_Sale.setText("Final Resut="+str(e))
    def clear(self):
        self.ui.ln_unit.setText("0")
        self.ui.ln_no.setText("0")
        self.ui.ln_dis.setText("0")
         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_()) 
