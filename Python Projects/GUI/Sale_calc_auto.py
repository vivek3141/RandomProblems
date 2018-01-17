# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sale_calc.ui'
#
# Created: Sat Aug  8 12:03:48 2015
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
        Dialog.resize(385, 260)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 68, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(21, 80, 73, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 61, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.ln_unit = QtGui.QLineEdit(Dialog)
        self.ln_unit.setGeometry(QtCore.QRect(94, 40, 133, 20))
        self.ln_unit.setObjectName(_fromUtf8("ln_unit"))
        self.ln_no = QtGui.QLineEdit(Dialog)
        self.ln_no.setGeometry(QtCore.QRect(100, 80, 133, 20))
        self.ln_no.setObjectName(_fromUtf8("ln_no"))
        self.ln_dis = QtGui.QLineEdit(Dialog)
        self.ln_dis.setGeometry(QtCore.QRect(87, 130, 133, 20))
        self.ln_dis.setObjectName(_fromUtf8("ln_dis"))
        self.pb_calc = QtGui.QPushButton(Dialog)
        self.pb_calc.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.pb_calc.setObjectName(_fromUtf8("pb_calc"))
        self.pb_close = QtGui.QPushButton(Dialog)
        self.pb_close.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.lbl_Sale = QtGui.QLabel(Dialog)
        self.lbl_Sale.setGeometry(QtCore.QRect(240, 90, 141, 23))
        self.lbl_Sale.setObjectName(_fromUtf8("lbl_Sale"))
        self.pb_clear = QtGui.QPushButton(Dialog)
        self.pb_clear.setGeometry(QtCore.QRect(150, 220, 75, 23))
        self.pb_clear.setObjectName(_fromUtf8("pb_clear"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Unit Price</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">No of Unit</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Discount</span></p></body></html>", None))
        self.pb_calc.setText(_translate("Dialog", "Calculate", None))
        self.pb_close.setText(_translate("Dialog", "Close", None))
        self.lbl_Sale.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Sale Price</span></p></body></html>", None))
        self.pb_clear.setText(_translate("Dialog", "Clear", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

