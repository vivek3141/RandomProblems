import sys
from PyQt4 import QtCore, QtGui, uic 
import sqlite3
a1 = ""
a2 = ""
c = ""
z = ""
p = ""
from TelDir_auto import * 
from teldirup_auto import * 
  
class Dialog_Address(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog_address() 
        self.ui.setupUi(self) 
        self.conn= sqlite3.connect("teldir.db")
        self.ui.mode = "l"
        self.mode = "a"
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.update)
    def load(self, id):
        try:
            a = []
            cursor = self.conn.cursor()
            cursor.execute("select address_1, address_2, city, zip, profession from teldir where tel_id = "+id)
            row = cursor.fetchall()
            print (row)
            for j in row:
                a = j
            if len(a) == 0:
               return False 

            self.ui.lne_i.setText(id)
            self.ui.lne_a1.setText(a[0])
            self.ui.lne_a2.setText(a[1])
            self.ui.lne_c.setText(a[2])
            self.ui.lne_z.setText(a[3])
            self.ui.lne_p.setText(a[4])
            self.mode = "u"
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
            self.mode = "a"
            return False
    def update(self):
        if self.mode == "a":
 
            a1 = self.ui.lne_a1.text()
            a2 = self.ui.lne_a2.text()
            c = self.ui.lne_c.text()
            z = self.ui.lne_z.text()
            p = self.ui.lne_p.text()
            return a1, a2, c, z, p
        elif self.mode == "u":
            a1 = self.ui.lne_a1.text()
            a2 = self.ui.lne_a2.text()
            c = self.ui.lne_c.text()
            z = self.ui.lne_z.text()
            p = self.ui.lne_p.text()
            try:
                cursor = self.conn.cursor()
                cursor.execute("UPDATE teldir set address_1 = '"+a1+"', address_2 = '"+a2+"', city = '"+c+"', zip = '"+z+ "', profession = '"+p+"' where tel_id = "+self.ui.lne_i.text() );
                self.conn.commit()
            except sqlite3.Error as e:
                QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
                return False
            QtGui.QMessageBox.information(self,  "Not an Error", "Saved successfully")

        

                
        
                    
                    
        
                
        

        
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        self.mode = ""
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        self.conn= sqlite3.connect("teldir.db")
        self.refresh()
        QtCore.QObject.connect(self.pb_refresh, QtCore.SIGNAL('clicked()'), self.refresh)
        QtCore.QObject.connect(self.pb_select, QtCore.SIGNAL('clicked()'), self.select)
        QtCore.QObject.connect(self.pb_add, QtCore.SIGNAL('clicked()'), self.add)
        QtCore.QObject.connect(self.pb_save, QtCore.SIGNAL('clicked()'), self.save)
        QtCore.QObject.connect(self.pb_upd, QtCore.SIGNAL('clicked()'), self.showDetails)
    def showDetails(self):
        self.dAddress = Dialog_Address(self)
        self.dAddress.show()
        id  = self.lne_id.text()
        self.dAddress.load(id)
        pass
        
    def add(self):
        self.mode = "a"
        self.lne_id.setText("")
        self.lne_na.setText("")
        self.lne_ni.setText("")
        self.lne_ph.setText("")
        self.lne_la.setText("")
        self.lne_sh.setText("")
    def clear(self):
        self.dAddress = Dialog_Address(self)
        self.dAddress.ui.lne_a1.setText("")
        self.dAddress.ui.lne_a2.setText("")
        self.dAddress.ui.lne_c.setText("")
        self.dAddress.ui.lne_z.setText("")
        self.dAddress.ui.lne_p.setText("")
        self.lne_id.setText("")
        self.lne_na.setText("")
        self.lne_ni.setText("")
        self.lne_ph.setText("")
        self.lne_la.setText("")
        self.lne_sh.setText("")
    def save(self):
        if self.mode == "a":
            self.dAddress = Dialog_Address(self)
            a1, a2, c, z, p = self.dAddress.update()
            print(a1, a2, c, z, p)
            
            id = self.lne_id.text()
            na = self.lne_na.text()
            ni = self.lne_ni.text()
            ph = self.lne_ph.text()
            if len(str(ph)) != 10:
                QtGui.QMessageBox.information(self,  "Error!", "Phone nuber should be 10 digits")
                return False    
            la = self.lne_la.text()
            sh = self.lne_sh.text()
            id = id + " "*(15 - len(str(id)))
            na = na + " "*(15 - len(str(id)))
            ni = ni + " "*(15 - len(str(id)))
            ph = ph + " "*(15 - len(str(id)))
            la = la + " "*(15 - len(str(id)))
            sh = sh + " "*(15 - len(str(id)))
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO teldir VALUES (?,?,?,?,?,?,?,?,?,?,?)", (id, na, ni, ph, la, sh, a1, a2, c, z, p))
                self.conn.commit()
            except sqlite3.Error as e:
                QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
                return False
            self.refresh()
            self.clear()
            QtGui.QMessageBox.information(self,  "Not an Error", "Saved successfully")
            
        elif self.mode == "u":
            id = self.lne_id.text()
            na = self.lne_na.text()
            ni = self.lne_ni.text()
            ph = self.lne_ph.text()
            if len(str(ph)) != 10:
                QtGui.QMessageBox.information(self,  "Error!", "Phone nuber should be 10 digits")
                return False    
            la = self.lne_la.text()
            sh = self.lne_sh.text()
            try:
                cursor = self.conn.cursor()
                cursor.execute("UPDATE teldir set full_name = '"+na+"', nickname = '"+ni+"', telephone_no = '"+ph+"', landline = '"+la+"', address_short = '"+sh+"' where tel_id = "+id );
                self.conn.commit()
            except sqlite3.Error as e:
                QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
                return False
            self.refresh()
            self.clear()
            QtGui.QMessageBox.information(self,  "Not an Error", "Saved successfully")
            
    def select(self):
        self.mode = "u"
        a = self.lwe.currentItem().text()
        b = a.split(" ")
        print(len(b))
        for i in range(len(b) - 6) :
            b.remove('')
        id = b[0]
        na = b[1]
        ni = b[2]
        ph = b[3]
        la = b[4]
        sh = b[5]
        self.lne_id.setText(id)
        self.lne_na.setText(na)
        self.lne_ni.setText(ni)
        self.lne_ph.setText(ph)
        self.lne_la.setText(la)
        self.lne_sh.setText(sh)    
        
        
        
        
    def refresh(self):
        
        self.lwe.clear()
        self.lwe.addItem("Id             Name           Nickname       Phone No.      Landline       Short Address")
        b = ""
        a = 0
        try:
            cursor = self.conn.cursor()
            cursor.execute("select tel_id,full_name,nickname,telephone_no,landline,address_short from teldir")
            row = cursor.fetchall()
            for j in row:
                b = ""
                for i in j:
                    b = b + str(i) + " "*(15 - int(len(i)))
                  
                    
                self.lwe.addItem(b)
                    
        except sqlite3.Error as e:
                QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
        
         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
