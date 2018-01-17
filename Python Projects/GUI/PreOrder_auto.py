# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreOrder.ui'
#
# Created: Sat Aug 22 13:10:52 2015
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
        MainWindow.resize(264, 253)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rb_ms = QtGui.QRadioButton(self.centralwidget)
        self.rb_ms.setGeometry(QtCore.QRect(63, 32, 40, 17))
        self.rb_ms.setObjectName(_fromUtf8("rb_ms"))
        self.lne_name = QtGui.QLineEdit(self.centralwidget)
        self.lne_name.setGeometry(QtCore.QRect(120, 30, 131, 20))
        self.lne_name.setObjectName(_fromUtf8("lne_name"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 61, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 141, 29, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sb_1 = QtGui.QSpinBox(self.centralwidget)
        self.sb_1.setGeometry(QtCore.QRect(160, 70, 61, 22))
        self.sb_1.setObjectName(_fromUtf8("sb_1"))
        self.dsb_1 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.dsb_1.setGeometry(QtCore.QRect(160, 150, 62, 22))
        self.dsb_1.setObjectName(_fromUtf8("dsb_1"))
        self.pb_process = QtGui.QPushButton(self.centralwidget)
        self.pb_process.setGeometry(QtCore.QRect(160, 110, 75, 23))
        self.pb_process.setObjectName(_fromUtf8("pb_process"))
        self.rb_mr = QtGui.QRadioButton(self.centralwidget)
        self.rb_mr.setGeometry(QtCore.QRect(20, 30, 35, 17))
        self.rb_mr.setObjectName(_fromUtf8("rb_mr"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(19, 50, 121, 81))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rb_patties = QtGui.QRadioButton(self.groupBox)
        self.rb_patties.setGeometry(QtCore.QRect(10, 30, 271, 17))
        self.rb_patties.setObjectName(_fromUtf8("rb_patties"))
        self.cbx_chillies = QtGui.QCheckBox(self.groupBox)
        self.cbx_chillies.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.cbx_chillies.setObjectName(_fromUtf8("cbx_chillies"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 120, 120, 80))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cbx_onion = QtGui.QCheckBox(self.groupBox_2)
        self.cbx_onion.setGeometry(QtCore.QRect(10, 60, 301, 17))
        self.cbx_onion.setObjectName(_fromUtf8("cbx_onion"))
        self.rb_soup = QtGui.QRadioButton(self.groupBox_2)
        self.rb_soup.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.rb_soup.setObjectName(_fromUtf8("rb_soup"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 264, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.rb_ms.setText(_translate("MainWindow", "Ms.", None))
        self.label.setText(_translate("MainWindow", "Appetizers", None))
        self.label_2.setText(_translate("MainWindow", "Soups", None))
        self.pb_process.setText(_translate("MainWindow", "Process", None))
        self.rb_mr.setText(_translate("MainWindow", "Mr", None))
        self.rb_patties.setText(_translate("MainWindow", "Green Patties", None))
        self.cbx_chillies.setText(_translate("MainWindow", "Green Chillies", None))
        self.cbx_onion.setText(_translate("MainWindow", "French Onion", None))
        self.rb_soup.setText(_translate("MainWindow", "Clear Soup", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

