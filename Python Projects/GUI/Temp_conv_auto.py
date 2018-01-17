# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Temp_converter.ui'
#
# Created: Sat Aug  1 13:12:53 2015
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
        MainWindow.resize(331, 308)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_C_to_F = QtGui.QPushButton(self.centralwidget)
        self.btn_C_to_F.setGeometry(QtCore.QRect(90, 130, 141, 23))
        self.btn_C_to_F.setObjectName(_fromUtf8("btn_C_to_F"))
        self.btn_F_to_C = QtGui.QPushButton(self.centralwidget)
        self.btn_F_to_C.setGeometry(QtCore.QRect(90, 190, 141, 23))
        self.btn_F_to_C.setObjectName(_fromUtf8("btn_F_to_C"))
        self.sb_F = QtGui.QSpinBox(self.centralwidget)
        self.sb_F.setGeometry(QtCore.QRect(240, 160, 81, 22))
        self.sb_F.setMaximum(999999999)
        self.sb_F.setObjectName(_fromUtf8("sb_F"))
        self.txb_info = QtGui.QTextBrowser(self.centralwidget)
        self.txb_info.setGeometry(QtCore.QRect(20, 10, 291, 111))
        self.txb_info.setObjectName(_fromUtf8("txb_info"))
        self.lne_C = QtGui.QLineEdit(self.centralwidget)
        self.lne_C.setGeometry(QtCore.QRect(20, 160, 81, 20))
        self.lne_C.setObjectName(_fromUtf8("lne_C"))
        self.btn_clear = QtGui.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.btn_Close = QtGui.QPushButton(self.centralwidget)
        self.btn_Close.setGeometry(QtCore.QRect(240, 240, 75, 23))
        self.btn_Close.setObjectName(_fromUtf8("btn_Close"))
        self.label_C = QtGui.QLabel(self.centralwidget)
        self.label_C.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.label_C.setObjectName(_fromUtf8("label_C"))
        self.label_F = QtGui.QLabel(self.centralwidget)
        self.label_F.setGeometry(QtCore.QRect(240, 140, 61, 20))
        self.label_F.setObjectName(_fromUtf8("label_F"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_Close, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_C_to_F.setText(_translate("MainWindow", "Celsius to Fahrenheit>>>", None))
        self.btn_F_to_C.setText(_translate("MainWindow", "Fahrenheit to Celsius>>>", None))
        self.txb_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enter a Fahernheit value and press Convert. The Celcius will be calculated and displayed. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Press Clear to clear all values.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enter a Celcius value and press Convert. The Fahernhiet will be calculated and displayed</span></p></body></html>", None))
        self.btn_clear.setText(_translate("MainWindow", "Clear", None))
        self.btn_Close.setText(_translate("MainWindow", "Close", None))
        self.label_C.setText(_translate("MainWindow", "Celsius", None))
        self.label_F.setText(_translate("MainWindow", "Fahrenheit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

