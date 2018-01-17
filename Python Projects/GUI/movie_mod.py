import sys
from PyQt4 import QtCore, QtGui, uic, QtSql 
from query_movie_mod import * 
from movie_auto import * 
from movie_query_mod import * 
import sqlite3
from movie_update_mod import * 

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionlang, QtCore.SIGNAL('triggered()'), self.query_lang)
        QtCore.QObject.connect(self.actionGenre, QtCore.SIGNAL('triggered()'), self.query_genre)
        QtCore.QObject.connect(self.actionFormat, QtCore.SIGNAL('triggered()'), self.query_format)
        QtCore.QObject.connect(self.actionMovies, QtCore.SIGNAL('triggered()'), self.up_movie)
        QtCore.QObject.connect(self.actionMov, QtCore.SIGNAL('triggered()'), self.mov)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("movie.db")
        db.open()
    
    def mov(self):
        mov = MyForm(self)
        mov.show()
    def up_movie(self):
        up = Dialog_Update(self)
        up.show()
        up.exec_() 
    def query_lang(self):
        lang = Query(self)
        lang.show()
        lang.lang()
    def query_genre(self):
        lang = Query(self)
        lang.show()
        lang.genre()
    def query_format(self):
        lang = Query(self)
        lang.show()
        lang.format()
        

        
 	     

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
