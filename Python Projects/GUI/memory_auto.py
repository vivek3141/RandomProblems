# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memory.ui'
#
# Created: Sat Jan 16 09:23:53 2016
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
        MainWindow.resize(224, 268)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pb_1 = QtGui.QPushButton(self.centralwidget)
        self.pb_1.setGeometry(QtCore.QRect(27, 64, 75, 51))
        self.pb_1.setText(_fromUtf8(""))
        self.pb_1.setObjectName(_fromUtf8("pb_1"))
        self.pb_4 = QtGui.QPushButton(self.centralwidget)
        self.pb_4.setGeometry(QtCore.QRect(130, 160, 75, 51))
        self.pb_4.setText(_fromUtf8(""))
        self.pb_4.setObjectName(_fromUtf8("pb_4"))
        self.pb_2 = QtGui.QPushButton(self.centralwidget)
        self.pb_2.setGeometry(QtCore.QRect(130, 64, 75, 51))
        self.pb_2.setText(_fromUtf8(""))
        self.pb_2.setObjectName(_fromUtf8("pb_2"))
        self.pb_3 = QtGui.QPushButton(self.centralwidget)
        self.pb_3.setGeometry(QtCore.QRect(27, 160, 75, 51))
        self.pb_3.setText(_fromUtf8(""))
        self.pb_3.setObjectName(_fromUtf8("pb_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 224, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Memory Game", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

