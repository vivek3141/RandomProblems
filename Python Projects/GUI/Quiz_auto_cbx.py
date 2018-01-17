# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Quiz_cbx.ui'
#
# Created: Sat Aug 29 13:06:23 2015
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
        MainWindow.resize(299, 308)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_close = QtGui.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.btn_next = QtGui.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.lbl_modi = QtGui.QLabel(self.centralwidget)
        self.lbl_modi.setGeometry(QtCore.QRect(20, 20, 251, 16))
        self.lbl_modi.setObjectName(_fromUtf8("lbl_modi"))
        self.lbl_w10 = QtGui.QLabel(self.centralwidget)
        self.lbl_w10.setGeometry(QtCore.QRect(20, 90, 321, 16))
        self.lbl_w10.setObjectName(_fromUtf8("lbl_w10"))
        self.lbl_ap = QtGui.QLabel(self.centralwidget)
        self.lbl_ap.setGeometry(QtCore.QRect(20, 160, 281, 16))
        self.lbl_ap.setObjectName(_fromUtf8("lbl_ap"))
        self.btn_submit = QtGui.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.btn_submit.setObjectName(_fromUtf8("btn_submit"))
        self.lbl_score = QtGui.QLabel(self.centralwidget)
        self.lbl_score.setGeometry(QtCore.QRect(205, 10, 71, 20))
        self.lbl_score.setObjectName(_fromUtf8("lbl_score"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 251, 31))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.rb_2 = QtGui.QRadioButton(self.groupBox)
        self.rb_2.setGeometry(QtCore.QRect(100, 10, 82, 17))
        self.rb_2.setObjectName(_fromUtf8("rb_2"))
        self.rb_2_1 = QtGui.QRadioButton(self.groupBox)
        self.rb_2_1.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.rb_2_1.setObjectName(_fromUtf8("rb_2_1"))
        self.rb_2_2 = QtGui.QRadioButton(self.groupBox)
        self.rb_2_2.setGeometry(QtCore.QRect(100, 0, 82, 17))
        self.rb_2_2.setObjectName(_fromUtf8("rb_2_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 120, 251, 31))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.rb_3 = QtGui.QRadioButton(self.groupBox_3)
        self.rb_3.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.rb_3.setObjectName(_fromUtf8("rb_3"))
        self.rb_4 = QtGui.QRadioButton(self.groupBox_3)
        self.rb_4.setGeometry(QtCore.QRect(100, 10, 82, 17))
        self.rb_4.setObjectName(_fromUtf8("rb_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 190, 251, 31))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.rb_5 = QtGui.QRadioButton(self.groupBox_2)
        self.rb_5.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.rb_5.setObjectName(_fromUtf8("rb_5"))
        self.rb_6 = QtGui.QRadioButton(self.groupBox_2)
        self.rb_6.setGeometry(QtCore.QRect(100, 10, 82, 17))
        self.rb_6.setObjectName(_fromUtf8("rb_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_close, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Quiz(Beta)", None))
        self.btn_close.setText(_translate("MainWindow", "Close", None))
        self.btn_next.setText(_translate("MainWindow", "Next>>", None))
        self.lbl_modi.setText(_translate("MainWindow", "The First PM of India was Modi.(T/F)?", None))
        self.lbl_w10.setText(_translate("MainWindow", "Windows 10 is the last version of windows(T/F)?", None))
        self.lbl_ap.setText(_translate("MainWindow", "Telengana is a part of Andhra Pradesh(T/F)?", None))
        self.btn_submit.setText(_translate("MainWindow", "Submit", None))
        self.lbl_score.setText(_translate("MainWindow", "Your Score:", None))
        self.radioButton.setText(_translate("MainWindow", "True", None))
        self.rb_2.setText(_translate("MainWindow", "False", None))
        self.rb_2_1.setText(_translate("MainWindow", "RadioButton", None))
        self.rb_2_2.setText(_translate("MainWindow", "RadioButton", None))
        self.rb_3.setText(_translate("MainWindow", "True", None))
        self.rb_4.setText(_translate("MainWindow", "False", None))
        self.rb_5.setText(_translate("MainWindow", "True", None))
        self.rb_6.setText(_translate("MainWindow", "False", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

