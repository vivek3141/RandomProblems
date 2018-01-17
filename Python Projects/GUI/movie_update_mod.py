import sys
from PyQt4 import QtCore, QtGui, uic, QtSql 
from movie_query_mod import*
from movie_update_auto import *
import sqlite3
class Dialog_Update(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL('clicked()'), self.btn_retrieveall)
        QtCore.QObject.connect(self.ui.pb_save, QtCore.SIGNAL('clicked()'), self.btn_save)
        QtCore.QObject.connect(self.ui.pb_add, QtCore.SIGNAL('clicked()'), self.btn_add)
        QtCore.QObject.connect(self.ui.pb_lang, QtCore.SIGNAL('clicked()'), self.lang)
        QtCore.QObject.connect(self.ui.pb_genre, QtCore.SIGNAL('clicked()'), self.genre)
        self.conn= sqlite3.connect("movie.db")
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("movie.db")
        db.open()
        self.btn_retrieveall()

    def lang(self):
        lang = Query(self)
        lang.show()
        lang.lang()
        lang.ui.tv.doubleClicked.connect(self.double)
        
    def genre(self):
        lang = Query(self)
        lang.show()
        lang.genre()
    def btn_retrieveall(self):         
        self.model = QtSql.QSqlTableModel(self)         
        self.model.setTable("movie") 
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)         
        self.model.select()         
        self.ui.tv.setModel(self.model)  
    def btn_save(self):
        self.model.submitAll()
        self.model.select()
    def btn_add(self):
        self.model.insertRows(self.model.rowCount(), 1)
       
    def double(self):
        pass
          
         
if __name__=="__main__": 
    app = QtGui.QApplication(sys.argv)
    my = Dialog_Update(None)
    my.show()
    app.exec_() 
