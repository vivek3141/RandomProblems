# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie.ui'
#
# Created: Sat Feb 13 12:29:15 2016
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
        MainWindow.resize(669, 536)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 671, 541))
        self.graphicsView.setStyleSheet(_fromUtf8("background-image: url(:/movie/movie.jpg);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAdd = QtGui.QMenu(self.menubar)
        self.menuAdd.setObjectName(_fromUtf8("menuAdd"))
        self.menuTransact = QtGui.QMenu(self.menubar)
        self.menuTransact.setObjectName(_fromUtf8("menuTransact"))
        self.menuQuery = QtGui.QMenu(self.menubar)
        self.menuQuery.setObjectName(_fromUtf8("menuQuery"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionlang = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.actionlang.setFont(font)
        self.actionlang.setObjectName(_fromUtf8("actionlang"))
        self.actionGenre = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actionGenre.setFont(font)
        self.actionGenre.setObjectName(_fromUtf8("actionGenre"))
        self.actionFormat = QtGui.QAction(MainWindow)
        self.actionFormat.setObjectName(_fromUtf8("actionFormat"))
        self.actionMovies = QtGui.QAction(MainWindow)
        self.actionMovies.setObjectName(_fromUtf8("actionMovies"))
        self.actionCodes = QtGui.QAction(MainWindow)
        self.actionCodes.setObjectName(_fromUtf8("actionCodes"))
        self.actionMov = QtGui.QAction(MainWindow)
        self.actionMov.setObjectName(_fromUtf8("actionMov"))
        self.menuAdd.addAction(self.actionMovies)
        self.menuAdd.addAction(self.actionCodes)
        self.menuQuery.addAction(self.actionlang)
        self.menuQuery.addAction(self.actionGenre)
        self.menuQuery.addAction(self.actionFormat)
        self.menuQuery.addAction(self.actionMov)
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuTransact.menuAction())
        self.menubar.addAction(self.menuQuery.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuAdd.setTitle(_translate("MainWindow", "Add", None))
        self.menuTransact.setTitle(_translate("MainWindow", "Transact", None))
        self.menuQuery.setTitle(_translate("MainWindow", "Query", None))
        self.actionlang.setText(_translate("MainWindow", "Languages", None))
        self.actionGenre.setText(_translate("MainWindow", "Genre", None))
        self.actionFormat.setText(_translate("MainWindow", "Format", None))
        self.actionMovies.setText(_translate("MainWindow", "Movies", None))
        self.actionCodes.setText(_translate("MainWindow", "Codes", None))
        self.actionMov.setText(_translate("MainWindow", "Movies - Basic Query", None))

import movie_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

