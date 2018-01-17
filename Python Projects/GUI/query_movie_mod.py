import sys
from query_movie_auto import * 
from PyQt4 import QtCore, QtGui, uic, QtSql 
import sqlite3
 
class MyForm(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        QtCore.QObject.connect(self.ui.pb_q, QtCore.SIGNAL('clicked()'), self.search)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("movie.db")
        db.open()
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("select * from movie")
        self.ui.tableView.setModel(self.model)
        self.conn= sqlite3.connect("movie.db")
        self.loadCombo()
    def loadCombo(self):
        self.ui.cb_genre.clear()
        cursor = self.conn.cursor()
        cursor.execute("select type_cd, type_type from types where type_desc = 'genre'")
        arows = cursor.fetchall()
        self.string = "A"+" "+"All"
        self.ui.cb_genre.addItem(self.string)
        for row in arows:
            type_cd, type_desc = row
            string = type_cd + " " + type_desc
            self.ui.cb_genre.addItem(string)
            
        self.ui.cb_lang.clear()
        cursor = self.conn.cursor()
        cursor.execute("select type_cd, type_type from types where type_desc = 'lang'")
        arows = cursor.fetchall()
        string = "A"+" "+"All"
        self.ui.cb_lang.addItem(string)
        for row in arows:
            type_cd, type_desc = row
            string = type_cd + " " + type_desc
            self.ui.cb_lang.addItem(string)
            
        self.ui.cb_format.clear()
        cursor = self.conn.cursor()
        cursor.execute("select type_cd, type_type from types where type_desc = 'format'")
        arows = cursor.fetchall()
        string = "A"+" "+"All"
        self.ui.cb_format.addItem(string)
        for row in arows:
            type_cd, type_desc = row
            string = type_cd + " " + type_desc
            self.ui.cb_format.addItem(string)
    def search(self):
        self.model = QtSql.QSqlQueryModel(self)
        a = self.ui.cxb.isChecked()
        if a == True:
            a = "y"
        else:
            a = "A"
        print(a)
        dir = self.ui.lne_dir.text()
        main = self.ui.lne_main.text()
        
        format = self.ui.cb_format.currentText()
        format = format[0]
        format = str(format)
        genre = self.ui.cb_genre.currentText()
        genre = genre[0]
        genre = str(genre)
        lang = self.ui.cb_lang.currentText()
        lang = lang[0]
        lang = str(lang)
        query = "select * from movie where \
            (lang = '"+lang+"' or '"+lang+"' = 'A')\
            and (genre = '"+genre+"' or '"+genre+"' = 'A')\
            and(format = '"+format+"' or '"+format+"' = 'A')\
            and(available = '"+a+"' or '"+a+"' = 'A')\
            and(director = '"+dir+"' or '"+dir+"' = '')\
            and(main_lead = '"+main+"' or '"+main+"' = '')"
        
            
        
        self.model.setQuery(query)
        self.ui.tableView.setModel(self.model)
        
            
        
        
    
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_()) 
