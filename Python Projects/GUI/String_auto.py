# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'String.ui'
#
# Created: Sat Sep 26 11:51:41 2015
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
        MainWindow.resize(369, 316)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rb_e = QtGui.QRadioButton(self.centralwidget)
        self.rb_e.setGeometry(QtCore.QRect(271, 21, 82, 17))
        self.rb_e.setObjectName(_fromUtf8("rb_e"))
        self.rb_fob = QtGui.QRadioButton(self.centralwidget)
        self.rb_fob.setGeometry(QtCore.QRect(271, 60, 82, 17))
        self.rb_fob.setObjectName(_fromUtf8("rb_fob"))
        self.lne = QtGui.QLineEdit(self.centralwidget)
        self.lne.setGeometry(QtCore.QRect(73, 32, 171, 20))
        self.lne.setObjectName(_fromUtf8("lne"))
        self.txe = QtGui.QTextEdit(self.centralwidget)
        self.txe.setGeometry(QtCore.QRect(73, 71, 177, 139))
        self.txe.setObjectName(_fromUtf8("txe"))
        self.lbl_1 = QtGui.QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(21, 32, 46, 16))
        self.lbl_1.setObjectName(_fromUtf8("lbl_1"))
        self.lbl_2 = QtGui.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(21, 71, 46, 16))
        self.lbl_2.setObjectName(_fromUtf8("lbl_2"))
        self.lbl_main = QtGui.QLabel(self.centralwidget)
        self.lbl_main.setGeometry(QtCore.QRect(10, 220, 351, 20))
        self.lbl_main.setObjectName(_fromUtf8("lbl_main"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionE = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/e.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionE.setIcon(icon)
        self.actionE.setObjectName(_fromUtf8("actionE"))
        self.actionForb = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/forb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForb.setIcon(icon1)
        self.actionForb.setObjectName(_fromUtf8("actionForb"))
        self.actionOnly = QtGui.QAction(MainWindow)
        self.actionOnly.setObjectName(_fromUtf8("actionOnly"))
        self.actionAll = QtGui.QAction(MainWindow)
        self.actionAll.setObjectName(_fromUtf8("actionAll"))
        self.menuFile.addAction(self.actionE)
        self.menuFile.addAction(self.actionForb)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionE)
        self.toolBar.addAction(self.actionForb)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.rb_e.setText(_translate("MainWindow", "Has no e?", None))
        self.rb_fob.setText(_translate("MainWindow", "Forbidden?", None))
        self.lbl_1.setText(_translate("MainWindow", "Choose:", None))
        self.lbl_2.setText(_translate("MainWindow", "Choose:", None))
        self.lbl_main.setText(_translate("MainWindow", "TextLabel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionE.setText(_translate("MainWindow", "Has no e", None))
        self.actionE.setShortcut(_translate("MainWindow", "Ctrl+E", None))
        self.actionForb.setText(_translate("MainWindow", "Forbidden", None))
        self.actionForb.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionOnly.setText(_translate("MainWindow", "Uses only", None))
        self.actionOnly.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionAll.setText(_translate("MainWindow", "Uses all", None))
        self.actionAll.setShortcut(_translate("MainWindow", "Ctrl+A", None))

import String_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

