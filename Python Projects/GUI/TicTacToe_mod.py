import sys
from PyQt4 import QtCore, QtGui, uic 
import random
import sqlite3
 
from TicTacToe_auto import * 


        

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        self.turn = 1
        self.no = 0
        self.conn= sqlite3.connect("saveTicTacToe.db")
        
        #To decide whether it is x's self.turn or 0's self.turn
        #Change this to 1 for x to start first, 0 for 0 to start first
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        #Setting up the PushButtons
        QtCore.QObject.connect(self.pb_1, QtCore.SIGNAL('clicked()'), self.pb1)
        QtCore.QObject.connect(self.pb_2, QtCore.SIGNAL('clicked()'), self.pb2)
        QtCore.QObject.connect(self.pb_3, QtCore.SIGNAL('clicked()'), self.pb3) 
        QtCore.QObject.connect(self.pb_4, QtCore.SIGNAL('clicked()'), self.pb4)
        QtCore.QObject.connect(self.pb_5, QtCore.SIGNAL('clicked()'), self.pb5) 
        QtCore.QObject.connect(self.pb_6, QtCore.SIGNAL('clicked()'), self.pb6)
        QtCore.QObject.connect(self.pb_7, QtCore.SIGNAL('clicked()'), self.pb7) 
        QtCore.QObject.connect(self.pb_8, QtCore.SIGNAL('clicked()'), self.pb8)
        QtCore.QObject.connect(self.pb_9, QtCore.SIGNAL('clicked()'), self.pb9)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL('triggered()'), self.exit)
        QtCore.QObject.connect(self.actionRestart, QtCore.SIGNAL('triggered()'), self.restart)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL('triggered()'), self.save)
        QtCore.QObject.connect(self.actionLoad, QtCore.SIGNAL('triggered()'), self.load)
        QtCore.QObject.connect(self.actionpvp, QtCore.SIGNAL('triggered()'), self.pvp)
        QtCore.QObject.connect(self.actionpvc1, QtCore.SIGNAL('triggered()'), self.pvc1)
        QtCore.QObject.connect(self.actionpvc2, QtCore.SIGNAL('triggered()'), self.pvc2)
        self.lne_p1.setText("Player 1")
        self.lne_p2.setText("Player 2")
    def pvp(self):
        self.actionpvc1.setChecked(False)
        self.actionpvc2.setChecked(False)
    def pvc1(self):
        self.actionpvp.setChecked(False)
        self.actionpvc2.setChecked(False)
    def pvc2(self):
        self.actionpvc1.setChecked(False)
        self.actionpvp.setChecked(False)
    def save(self):
        (text, thruth) = QtGui.QInputDialog.getText(self, "Save As", "Name for the game to be saved")
        if thruth:
            b1 = self.pb_1.text()
            b2 = self.pb_2.text()
            b3 = self.pb_3.text()
            b4 = self.pb_4.text()
            b5 = self.pb_5.text()
            b6 = self.pb_6.text()
            b7 = self.pb_7.text()
            b8 = self.pb_8.text()
            b9 = self.pb_9.text()
            
            player_1 = self.lne_p1.text()
            player_2 = self.lne_p2.text()
            
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO tictacsave VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (text, player_1, player_2, b1, b2, b3, b4, b5, b6, b7, b8, b9))
                self.conn.commit()
            except sqlite3.Error as e:
                QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
                return False
            w = QtGui.QWidget()
            QtGui.QMessageBox.about(w, "Saved as -->" + text, "\n Your game was saved")
            return True
        else:
            return False
    def load_pbset(self, lb, text):
        if text in ("X",  "0"):
            lb.setText(text)
            self.pb(lb)
    def load(self):
        
        (text, thruth) = QtGui.QInputDialog.getText(self, "Save As", "Name for the game to be saved")
        try:
            cursor = self.conn.cursor()
            cursor.execute("select * from tictacsave where game_name = '"+text+"'")
            row = cursor.fetchall()
            if len(row) == 0:
                w = QtGui.QWidget()
                QtGui.QMessageBox.about(w, "Not Found!", "\n Your game was not found")
                return False
            self.restart()
            for i in row:
                g, p1, p2, b1, b2, b3, b4, b5, b6, b7, b8, b9 = i
            self.lne_p1.setText(p1)
            self.lne_p2.setText(p2)
            self.load_pbset(self.pb_1, b1)
            self.load_pbset(self.pb_2, b2)
            self.load_pbset(self.pb_3, b3)
            self.load_pbset(self.pb_4, b4)
            self.load_pbset(self.pb_5, b5)
            self.load_pbset(self.pb_6, b6)
            self.load_pbset(self.pb_7, b7)
            self.load_pbset(self.pb_8, b8)
            self.load_pbset(self.pb_9, b9)
        except sqlite3.Error as e:
                QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
                return False
            
            
           
    def restart(self):
        self.pb_1.setText("T")
        self.pb_2.setText("i")
        self.pb_3.setText("c")
        self.pb_4.setText("T")
        self.pb_5.setText("a")
        self.pb_6.setText("c")
        self.pb_7.setText("T")
        self.pb_8.setText("o")
        self.pb_9.setText("e")
        self.pb_1.setEnabled(True)
        self.pb_2.setEnabled(True)
        self.pb_3.setEnabled(True)
        self.pb_4.setEnabled(True)
        self.pb_5.setEnabled(True)
        self.pb_6.setEnabled(True)
        self.pb_7.setEnabled(True)
        self.pb_8.setEnabled(True)
        self.pb_9.setEnabled(True)
        self.turn = 1
        self.no = 0
        
    
    def exit(self):
        exit()
    def check(self, pb1,  pb2,  pb3,  letter):
        if pb1.text() == str(letter): 
            if pb2.text() == str(letter): 
                if pb3.text() == str(letter):
                    if letter == "X":
                        QtGui.QMessageBox.about(self, "Result",  self.lne_p1.text() + " Wins! Congratulations! \n \t Press OK to restart")
                        self.restart()
                    elif letter == "0":
                        QtGui.QMessageBox.about(self, "Result",  self.lne_p2.text() + " Wins! Congratulations!  \n \t Press OK to restart")
                        self.restart()
    def win(self, letter):
        self.check(self.pb_1, self.pb_2, self.pb_3, letter)
        self.check(self.pb_4, self.pb_5, self.pb_6, letter)
        self.check(self.pb_7, self.pb_8, self.pb_9, letter)
        self.check(self.pb_1, self.pb_4, self.pb_7, letter)
        self.check(self.pb_2, self.pb_5, self.pb_8, letter)
        self.check(self.pb_3, self.pb_6, self.pb_9, letter)
        self.check(self.pb_1, self.pb_5, self.pb_9, letter)
        self.check(self.pb_3, self.pb_5, self.pb_7, letter)
    def set(self, btn):
        self.btn.setText("0")
        self.win("0")
      


    #Defining functions for the pushbutton
    def pb(self, pb):
        if self.actionpvp.isChecked(): 
            if self.turn == 1:
                pb.setEnabled(False)
                pb.setText("X")
                self.turn = 0
                self.win("X")
                
            elif self.turn == 0:
                pb.setEnabled(False)
                pb.setText("0")
                self.turn = 1
                self.win("0")
            
            self.no = self.no + 1
            if self.no == 9:
                QtGui.QMessageBox.about(self, "Result",  "Its a TIE. Nobody wins.....")
                self.restart() 
        if self.actionpvc1.isChecked():
            self.lne_p2.setText("Computer")
            pb.setEnabled(False)
            pb.setText("X")
            self.win("X")
            a = random.randrange(1, 9)
            a = "pb_" + str(a)
            self.set(a)    
            if self.no == 9:
                QtGui.QMessageBox.about(self, "Result",  "Its a TIE. Nobody wins.....")
                self.restart()

    
            
    def pb1(self):
        self.pb(self.pb_1)
        
    def pb2(self):
        self.pb(self.pb_2)
        
    def pb3(self):
        self.pb(self.pb_3)
        
    def pb4(self):
        self.pb(self.pb_4)
        
    def pb5(self):
        self.pb(self.pb_5)
        
    def pb6(self):
        self.pb(self.pb_6)
        
    def pb7(self):
        self.pb(self.pb_7)
        
    def pb8(self):
        self.pb(self.pb_8)
        
    def pb9(self):
        self.pb(self.pb_9)
        
    
    
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
