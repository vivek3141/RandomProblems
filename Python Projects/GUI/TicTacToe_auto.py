# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TicTacToe.ui'
#
# Created: Sat Dec 12 12:43:56 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(297, 336)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pb_1 = QtGui.QPushButton(self.centralwidget)
        self.pb_1.setGeometry(QtCore.QRect(32, 51, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_1.setFont(font)
        self.pb_1.setObjectName(_fromUtf8("pb_1"))
        self.pb_2 = QtGui.QPushButton(self.centralwidget)
        self.pb_2.setGeometry(QtCore.QRect(113, 51, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_2.setFont(font)
        self.pb_2.setObjectName(_fromUtf8("pb_2"))
        self.pb_3 = QtGui.QPushButton(self.centralwidget)
        self.pb_3.setGeometry(QtCore.QRect(194, 51, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_3.setFont(font)
        self.pb_3.setObjectName(_fromUtf8("pb_3"))
        self.pb_7 = QtGui.QPushButton(self.centralwidget)
        self.pb_7.setGeometry(QtCore.QRect(32, 170, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pb_7.setFont(font)
        self.pb_7.setObjectName(_fromUtf8("pb_7"))
        self.pb_8 = QtGui.QPushButton(self.centralwidget)
        self.pb_8.setGeometry(QtCore.QRect(110, 170, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_8.setFont(font)
        self.pb_8.setObjectName(_fromUtf8("pb_8"))
        self.pb_4 = QtGui.QPushButton(self.centralwidget)
        self.pb_4.setGeometry(QtCore.QRect(32, 109, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_4.setFont(font)
        self.pb_4.setObjectName(_fromUtf8("pb_4"))
        self.pb_6 = QtGui.QPushButton(self.centralwidget)
        self.pb_6.setGeometry(QtCore.QRect(194, 109, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_6.setFont(font)
        self.pb_6.setObjectName(_fromUtf8("pb_6"))
        self.pb_5 = QtGui.QPushButton(self.centralwidget)
        self.pb_5.setGeometry(QtCore.QRect(113, 110, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_5.setFont(font)
        self.pb_5.setObjectName(_fromUtf8("pb_5"))
        self.pb_9 = QtGui.QPushButton(self.centralwidget)
        self.pb_9.setGeometry(QtCore.QRect(190, 170, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(18)
        self.pb_9.setFont(font)
        self.pb_9.setCheckable(False)
        self.pb_9.setFlat(False)
        self.pb_9.setObjectName(_fromUtf8("pb_9"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lne_p1 = QtGui.QLineEdit(self.centralwidget)
        self.lne_p1.setGeometry(QtCore.QRect(80, 230, 113, 20))
        self.lne_p1.setObjectName(_fromUtf8("lne_p1"))
        self.lne_p2 = QtGui.QLineEdit(self.centralwidget)
        self.lne_p2.setGeometry(QtCore.QRect(80, 260, 113, 20))
        self.lne_p2.setObjectName(_fromUtf8("lne_p2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 297, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionpvp = QtGui.QAction(MainWindow)
        self.actionpvp.setCheckable(True)
        self.actionpvp.setChecked(True)
        self.actionpvp.setObjectName(_fromUtf8("actionpvp"))
        self.actionpvc1 = QtGui.QAction(MainWindow)
        self.actionpvc1.setCheckable(True)
        self.actionpvc1.setObjectName(_fromUtf8("actionpvc1"))
        self.actionpvc2 = QtGui.QAction(MainWindow)
        self.actionpvc2.setCheckable(True)
        self.actionpvc2.setObjectName(_fromUtf8("actionpvc2"))
        self.actionRestart = QtGui.QAction(MainWindow)
        self.actionRestart.setObjectName(_fromUtf8("actionRestart"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRestart)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionpvp)
        self.menuOptions.addAction(self.actionpvc1)
        self.menuOptions.addAction(self.actionpvc2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe", None))
        self.pb_1.setText(_translate("MainWindow", "T", None))
        self.pb_2.setText(_translate("MainWindow", "i", None))
        self.pb_3.setText(_translate("MainWindow", "c", None))
        self.pb_7.setText(_translate("MainWindow", "T", None))
        self.pb_8.setText(_translate("MainWindow", "o", None))
        self.pb_4.setText(_translate("MainWindow", "T", None))
        self.pb_6.setText(_translate("MainWindow", "c", None))
        self.pb_5.setText(_translate("MainWindow", "a", None))
        self.pb_9.setText(_translate("MainWindow", "e", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Tic Tac Toe</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "Player 1:", None))
        self.label_3.setText(_translate("MainWindow", "Player 2:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E", None))
        self.actionpvp.setText(_translate("MainWindow", "Player vs Player", None))
        self.actionpvc1.setText(_translate("MainWindow", "Player vs Computer (Level 1)", None))
        self.actionpvc2.setText(_translate("MainWindow", "Player vs Computer (Level 2)", None))
        self.actionRestart.setText(_translate("MainWindow", "Restart", None))
        self.actionRestart.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
