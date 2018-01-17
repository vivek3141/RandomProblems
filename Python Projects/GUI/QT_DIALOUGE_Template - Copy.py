import sys
 
 
class Query(QtGui.QMainWindow, Ui_Query):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("select * from types where type_desc = 'lang'")
        self.tv.setModel(self.model)
        
         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_()) 
