# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MakeSentence.ui'
#
# Created: Sat Aug 29 11:34:00 2015
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
        MainWindow.resize(520, 448)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 21, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 60, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 130, 241, 101))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cbx_badi = QtGui.QCheckBox(self.groupBox)
        self.cbx_badi.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.cbx_badi.setObjectName(_fromUtf8("cbx_badi"))
        self.cbx_swim = QtGui.QCheckBox(self.groupBox)
        self.cbx_swim.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.cbx_swim.setObjectName(_fromUtf8("cbx_swim"))
        self.cbx_cricket = QtGui.QCheckBox(self.groupBox)
        self.cbx_cricket.setGeometry(QtCore.QRect(10, 70, 70, 17))
        self.cbx_cricket.setObjectName(_fromUtf8("cbx_cricket"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 250, 241, 101))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.rb_npshsr = QtGui.QRadioButton(self.groupBox_2)
        self.rb_npshsr.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.rb_npshsr.setObjectName(_fromUtf8("rb_npshsr"))
        self.rb_tisb = QtGui.QRadioButton(self.groupBox_2)
        self.rb_tisb.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.rb_tisb.setObjectName(_fromUtf8("rb_tisb"))
        self.rb_npsinr = QtGui.QRadioButton(self.groupBox_2)
        self.rb_npsinr.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.rb_npsinr.setObjectName(_fromUtf8("rb_npsinr"))
        self.pb_mks = QtGui.QPushButton(self.centralwidget)
        self.pb_mks.setGeometry(QtCore.QRect(140, 370, 231, 23))
        self.pb_mks.setObjectName(_fromUtf8("pb_mks"))
        self.txe_sent = QtGui.QTextEdit(self.centralwidget)
        self.txe_sent.setGeometry(QtCore.QRect(320, 10, 181, 111))
        self.txe_sent.setObjectName(_fromUtf8("txe_sent"))
        self.tne_fname = QtGui.QLineEdit(self.centralwidget)
        self.tne_fname.setGeometry(QtCore.QRect(100, 21, 133, 20))
        self.tne_fname.setObjectName(_fromUtf8("tne_fname"))
        self.lne_lname = QtGui.QLineEdit(self.centralwidget)
        self.lne_lname.setGeometry(QtCore.QRect(100, 60, 133, 20))
        self.lne_lname.setObjectName(_fromUtf8("lne_lname"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "First Name", None))
        self.label_2.setText(_translate("MainWindow", "Last Name", None))
        self.label_3.setText(_translate("MainWindow", "Sport", None))
        self.label_4.setText(_translate("MainWindow", "School", None))
        self.cbx_badi.setText(_translate("MainWindow", "Badminton", None))
        self.cbx_swim.setText(_translate("MainWindow", "Swimming", None))
        self.cbx_cricket.setText(_translate("MainWindow", "Cricket", None))
        self.rb_npshsr.setText(_translate("MainWindow", "NPS HSR", None))
        self.rb_tisb.setText(_translate("MainWindow", "TISB", None))
        self.rb_npsinr.setText(_translate("MainWindow", "NPS INR", None))
        self.pb_mks.setText(_translate("MainWindow", "Make My Sentence!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

