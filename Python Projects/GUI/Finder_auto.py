# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Finder.ui'
#
# Created: Sat Sep 19 12:32:56 2015
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
        MainWindow.resize(383, 325)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(31, 60, 63, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(31, 110, 50, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 110, 271, 161))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 191, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionFind)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Find What:</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">In What:</span></p></body></html>", None))
        self.lineEdit.setToolTip(_translate("MainWindow", "Enter stuff to find", None))
        self.lineEdit.setStatusTip(_translate("MainWindow", "Enter stuff to find", None))
        self.textEdit.setToolTip(_translate("MainWindow", "Enter an essay", None))
        self.textEdit.setStatusTip(_translate("MainWindow", "Enter an essay", None))
        self.label_3.setText(_translate("MainWindow", "Find a string", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close              ", None))
        self.actionClose.setShortcut(_translate("MainWindow", "Alt+D", None))
        self.actionClear.setText(_translate("MainWindow", "Clear All               ", None))
        self.actionClear.setShortcut(_translate("MainWindow", "Ctrl+C, Alt+C", None))
        self.actionFind.setText(_translate("MainWindow", "Find the String    ", None))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F, Alt+F", None))
        self.actionOpen.setText(_translate("MainWindow", "Open                   ", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

