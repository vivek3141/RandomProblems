import sys
from movie_query_auto import * 
from PyQt4 import QtCore, QtGui, uic, QtSql 
import sqlite3
class Query(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        self.conn= sqlite3.connect("movie.db")
     #   self.ui.tv.doubleClicked.connect(self.double)
        self.lang()

    def lang(self):
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("select * from types where type_desc = 'lang'")
        self.ui.tv.setModel(self.model)
    def genre(self):
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("select * from types where type_desc = 'genre'")
        self.ui.tv.setModel(self.model)
    def format(self):
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("select * from types where type_desc = 'format'")
        self.ui.tv.setModel(self.model)
#    def double(self):
#        index = self.ui.tv.selectedIndexes()[0]         
#        id_us = self.ui.tv.model().data(index)      
#        cursor = self.conn.cursor()
#        
#        cursor.execute("SELECT type_cd from types where type_type = '"+str(id_us)+"' or type_id = '"+str(id_us)+"' or type_cd = '"+str(id_us)+"'")
#        row = cursor.fetchall()
#        for i in row:
#            for j in i:
#                a = j
#        return str(a)
       
        
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Query()
    myapp.show()
    sys.exit(app.exec_()) 
