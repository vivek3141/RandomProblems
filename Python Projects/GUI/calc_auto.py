# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc.ui'
#
# Created: Sat Sep 26 12:00:38 2015
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
        MainWindow.resize(424, 378)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(31, 40, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(31, 90, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pb_calc = QtGui.QPushButton(self.centralwidget)
        self.pb_calc.setGeometry(QtCore.QRect(21, 200, 75, 41))
        self.pb_calc.setObjectName(_fromUtf8("pb_calc"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 200, 75, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.rb_add = QtGui.QRadioButton(self.centralwidget)
        self.rb_add.setGeometry(QtCore.QRect(300, 21, 82, 17))
        self.rb_add.setObjectName(_fromUtf8("rb_add"))
        self.rb_sub = QtGui.QRadioButton(self.centralwidget)
        self.rb_sub.setGeometry(QtCore.QRect(300, 54, 82, 17))
        self.rb_sub.setObjectName(_fromUtf8("rb_sub"))
        self.rb_multiply = QtGui.QRadioButton(self.centralwidget)
        self.rb_multiply.setGeometry(QtCore.QRect(300, 87, 82, 17))
        self.rb_multiply.setObjectName(_fromUtf8("rb_multiply"))
        self.rb_divide = QtGui.QRadioButton(self.centralwidget)
        self.rb_divide.setGeometry(QtCore.QRect(300, 120, 82, 17))
        self.rb_divide.setObjectName(_fromUtf8("rb_divide"))
        self.lne_f1_1 = QtGui.QLineEdit(self.centralwidget)
        self.lne_f1_1.setGeometry(QtCore.QRect(120, 41, 131, 20))
        self.lne_f1_1.setObjectName(_fromUtf8("lne_f1_1"))
        self.lne_f2_3 = QtGui.QLineEdit(self.centralwidget)
        self.lne_f2_3.setGeometry(QtCore.QRect(120, 90, 133, 20))
        self.lne_f2_3.setObjectName(_fromUtf8("lne_f2_3"))
        self.lne_r_1 = QtGui.QLineEdit(self.centralwidget)
        self.lne_r_1.setGeometry(QtCore.QRect(120, 140, 133, 20))
        self.lne_r_1.setObjectName(_fromUtf8("lne_r_1"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 180, 171, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lne_f1_2 = QtGui.QLineEdit(self.groupBox)
        self.lne_f1_2.setGeometry(QtCore.QRect(20, 40, 41, 20))
        self.lne_f1_2.setObjectName(_fromUtf8("lne_f1_2"))
        self.lne_f2_2 = QtGui.QLineEdit(self.groupBox)
        self.lne_f2_2.setGeometry(QtCore.QRect(100, 40, 41, 20))
        self.lne_f2_2.setObjectName(_fromUtf8("lne_f2_2"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lne_r_2 = QtGui.QLineEdit(self.groupBox)
        self.lne_r_2.setGeometry(QtCore.QRect(50, 90, 41, 20))
        self.lne_r_2.setObjectName(_fromUtf8("lne_r_2"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 70, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
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
        self.actionAdd = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionSub = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/subtract.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSub.setIcon(icon1)
        self.actionSub.setObjectName(_fromUtf8("actionSub"))
        self.actionMul = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/multiply-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMul.setIcon(icon2)
        self.actionMul.setObjectName(_fromUtf8("actionMul"))
        self.actionDiv = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/mathematic-divide-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDiv.setIcon(icon3)
        self.actionDiv.setObjectName(_fromUtf8("actionDiv"))
        self.menuFile.addAction(self.actionAdd)
        self.menuFile.addAction(self.actionSub)
        self.menuFile.addAction(self.actionMul)
        self.menuFile.addAction(self.actionDiv)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionSub)
        self.toolBar.addAction(self.actionMul)
        self.toolBar.addAction(self.actionDiv)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "First Number", None))
        self.label_2.setText(_translate("MainWindow", "Second number", None))
        self.label_3.setText(_translate("MainWindow", "Result", None))
        self.pb_calc.setText(_translate("MainWindow", "&Calculate", None))
        self.pushButton_2.setText(_translate("MainWindow", "Close", None))
        self.rb_add.setText(_translate("MainWindow", "Add", None))
        self.rb_sub.setText(_translate("MainWindow", "Subtract", None))
        self.rb_multiply.setText(_translate("MainWindow", "Multiply", None))
        self.rb_divide.setText(_translate("MainWindow", "Divide", None))
        self.groupBox.setTitle(_translate("MainWindow", "Result Review", None))
        self.label_4.setText(_translate("MainWindow", "1st number", None))
        self.label_5.setText(_translate("MainWindow", "2nd number", None))
        self.label_6.setText(_translate("MainWindow", "Result", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAdd.setText(_translate("MainWindow", "Add", None))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionSub.setText(_translate("MainWindow", "Subtract", None))
        self.actionSub.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionMul.setText(_translate("MainWindow", "Multiply", None))
        self.actionMul.setShortcut(_translate("MainWindow", "Ctrl+M", None))
        self.actionDiv.setText(_translate("MainWindow", "Divide", None))
        self.actionDiv.setShortcut(_translate("MainWindow", "Ctrl+D", None))

import Calc_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

