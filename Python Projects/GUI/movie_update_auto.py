# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_update.ui'
#
# Created: Sat Feb  6 12:07:48 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(740, 384)
        self.tv = QtGui.QTableView(Dialog)
        self.tv.setGeometry(QtCore.QRect(10, 40, 721, 281))
        self.tv.setObjectName(_fromUtf8("tv"))
        self.pb_r = QtGui.QPushButton(Dialog)
        self.pb_r.setGeometry(QtCore.QRect(401, 341, 75, 23))
        self.pb_r.setObjectName(_fromUtf8("pb_r"))
        self.pb_add = QtGui.QPushButton(Dialog)
        self.pb_add.setGeometry(QtCore.QRect(482, 341, 75, 23))
        self.pb_add.setObjectName(_fromUtf8("pb_add"))
        self.pb_close = QtGui.QPushButton(Dialog)
        self.pb_close.setGeometry(QtCore.QRect(644, 341, 75, 23))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.pb_save = QtGui.QPushButton(Dialog)
        self.pb_save.setGeometry(QtCore.QRect(563, 341, 75, 23))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.pb_lang = QtGui.QPushButton(Dialog)
        self.pb_lang.setGeometry(QtCore.QRect(120, 10, 31, 23))
        self.pb_lang.setObjectName(_fromUtf8("pb_lang"))
        self.pb_genre = QtGui.QPushButton(Dialog)
        self.pb_genre.setGeometry(QtCore.QRect(170, 10, 41, 23))
        self.pb_genre.setObjectName(_fromUtf8("pb_genre"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pb_r.setText(_translate("Dialog", "Retrieve", None))
        self.pb_add.setText(_translate("Dialog", "Add", None))
        self.pb_close.setText(_translate("Dialog", "Close", None))
        self.pb_save.setText(_translate("Dialog", "Save", None))
        self.pb_lang.setText(_translate("Dialog", "lang", None))
        self.pb_genre.setText(_translate("Dialog", "genre", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

