# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreOrder_advanced.ui'
#
# Created: Sat Sep 12 10:53:27 2015
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
        MainWindow.resize(449, 294)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(19, 20, 121, 81))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rb_patties = QtGui.QRadioButton(self.groupBox)
        self.rb_patties.setGeometry(QtCore.QRect(20, 30, 271, 17))
        self.rb_patties.setObjectName(_fromUtf8("rb_patties"))
        self.cbx_chillies = QtGui.QCheckBox(self.groupBox)
        self.cbx_chillies.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.cbx_chillies.setObjectName(_fromUtf8("cbx_chillies"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 100, 120, 80))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cbx_onion = QtGui.QCheckBox(self.groupBox_2)
        self.cbx_onion.setGeometry(QtCore.QRect(10, 60, 301, 17))
        self.cbx_onion.setObjectName(_fromUtf8("cbx_onion"))
        self.rb_soup = QtGui.QRadioButton(self.groupBox_2)
        self.rb_soup.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.rb_soup.setObjectName(_fromUtf8("rb_soup"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 29, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pb_add = QtGui.QPushButton(self.centralwidget)
        self.pb_add.setGeometry(QtCore.QRect(240, 180, 31, 23))
        self.pb_add.setObjectName(_fromUtf8("pb_add"))
        self.pb_delete = QtGui.QPushButton(self.centralwidget)
        self.pb_delete.setGeometry(QtCore.QRect(280, 180, 31, 23))
        self.pb_delete.setObjectName(_fromUtf8("pb_delete"))
        self.pb_remove = QtGui.QPushButton(self.centralwidget)
        self.pb_remove.setEnabled(True)
        self.pb_remove.setGeometry(QtCore.QRect(320, 180, 31, 23))
        self.pb_remove.setObjectName(_fromUtf8("pb_remove"))
        self.lwi_1 = QtGui.QListWidget(self.centralwidget)
        self.lwi_1.setGeometry(QtCore.QRect(180, 10, 231, 161))
        self.lwi_1.setObjectName(_fromUtf8("lwi_1"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 241, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cb_main = QtGui.QComboBox(self.centralwidget)
        self.cb_main.setGeometry(QtCore.QRect(240, 220, 191, 22))
        self.cb_main.setObjectName(_fromUtf8("cb_main"))
        self.cb_main.addItem(_fromUtf8(""))
        self.cb_main.addItem(_fromUtf8(""))
        self.cb_main.addItem(_fromUtf8(""))
        self.cb_main.addItem(_fromUtf8(""))
        self.cb_main.addItem(_fromUtf8(""))
        self.cb_main.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.rb_patties.setText(_translate("MainWindow", "Green Patties", None))
        self.cbx_chillies.setText(_translate("MainWindow", "Green Chillies", None))
        self.label.setText(_translate("MainWindow", "Appetizers", None))
        self.cbx_onion.setText(_translate("MainWindow", "French Onion", None))
        self.rb_soup.setText(_translate("MainWindow", "Clear Soup", None))
        self.label_2.setText(_translate("MainWindow", "Soups", None))
        self.pb_add.setText(_translate("MainWindow", ">", None))
        self.pb_delete.setText(_translate("MainWindow", "<", None))
        self.pb_remove.setText(_translate("MainWindow", ">>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose your main course:</span></p></body></html>", None))
        self.cb_main.setItemText(0, _translate("MainWindow", "Butter Chicken", None))
        self.cb_main.setItemText(1, _translate("MainWindow", "Butter Paneer", None))
        self.cb_main.setItemText(2, _translate("MainWindow", "Pizza", None))
        self.cb_main.setItemText(3, _translate("MainWindow", "Mutton", None))
        self.cb_main.setItemText(4, _translate("MainWindow", "Pasta", None))
        self.cb_main.setItemText(5, _translate("MainWindow", "Fish fry", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

