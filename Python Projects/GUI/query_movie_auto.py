# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_movie.ui'
#
# Created: Sat Feb 13 12:55:04 2016
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
        Dialog.resize(798, 461)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 110, 781, 331))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.cb_genre = QtGui.QComboBox(Dialog)
        self.cb_genre.setGeometry(QtCore.QRect(21, 61, 111, 20))
        self.cb_genre.setObjectName(_fromUtf8("cb_genre"))
        self.cb_format = QtGui.QComboBox(Dialog)
        self.cb_format.setGeometry(QtCore.QRect(150, 60, 121, 20))
        self.cb_format.setObjectName(_fromUtf8("cb_format"))
        self.cb_lang = QtGui.QComboBox(Dialog)
        self.cb_lang.setGeometry(QtCore.QRect(290, 60, 111, 20))
        self.cb_lang.setObjectName(_fromUtf8("cb_lang"))
        self.lne_dir = QtGui.QLineEdit(Dialog)
        self.lne_dir.setGeometry(QtCore.QRect(420, 60, 133, 20))
        self.lne_dir.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_dir.setText(_fromUtf8(""))
        self.lne_dir.setObjectName(_fromUtf8("lne_dir"))
        self.lne_main = QtGui.QLineEdit(Dialog)
        self.lne_main.setGeometry(QtCore.QRect(570, 60, 133, 20))
        self.lne_main.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_main.setText(_fromUtf8(""))
        self.lne_main.setObjectName(_fromUtf8("lne_main"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 40, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(430, 40, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(580, 40, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pb_q = QtGui.QPushButton(Dialog)
        self.pb_q.setGeometry(QtCore.QRect(720, 30, 61, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pb_q.setFont(font)
        self.pb_q.setObjectName(_fromUtf8("pb_q"))
        self.cxb = QtGui.QCheckBox(Dialog)
        self.cxb.setGeometry(QtCore.QRect(20, 20, 291, 17))
        self.cxb.setObjectName(_fromUtf8("cxb"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Genre", None))
        self.label_2.setText(_translate("Dialog", "Format", None))
        self.label_3.setText(_translate("Dialog", "Languages", None))
        self.label_4.setText(_translate("Dialog", "Director", None))
        self.label_5.setText(_translate("Dialog", "Main Lead", None))
        self.pb_q.setText(_translate("Dialog", "Q", None))
        self.cxb.setText(_translate("Dialog", "Available", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

