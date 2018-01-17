# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teldirup.ui'
#
# Created: Sat Jan 23 12:35:33 2016
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

class Ui_Dialog_address(object):
    def setupUi(self, Dialog_address):
        Dialog_address.setObjectName(_fromUtf8("Dialog_address"))
        Dialog_address.resize(247, 285)
        Dialog_address.setModal(True)
        self.label = QtGui.QLabel(Dialog_address)
        self.label.setGeometry(QtCore.QRect(24, 58, 46, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lne_p = QtGui.QLineEdit(Dialog_address)
        self.lne_p.setGeometry(QtCore.QRect(90, 198, 133, 20))
        self.lne_p.setObjectName(_fromUtf8("lne_p"))
        self.lne_a2 = QtGui.QLineEdit(Dialog_address)
        self.lne_a2.setGeometry(QtCore.QRect(90, 114, 133, 20))
        self.lne_a2.setObjectName(_fromUtf8("lne_a2"))
        self.label_4 = QtGui.QLabel(Dialog_address)
        self.label_4.setGeometry(QtCore.QRect(24, 142, 46, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_7 = QtGui.QLabel(Dialog_address)
        self.label_7.setGeometry(QtCore.QRect(23, 15, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Serif"))
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lne_z = QtGui.QLineEdit(Dialog_address)
        self.lne_z.setGeometry(QtCore.QRect(90, 170, 133, 20))
        self.lne_z.setObjectName(_fromUtf8("lne_z"))
        self.label_5 = QtGui.QLabel(Dialog_address)
        self.label_5.setGeometry(QtCore.QRect(24, 170, 46, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog_address)
        self.label_6.setGeometry(QtCore.QRect(24, 198, 171, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_2 = QtGui.QLabel(Dialog_address)
        self.label_2.setGeometry(QtCore.QRect(24, 86, 46, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lne_c = QtGui.QLineEdit(Dialog_address)
        self.lne_c.setGeometry(QtCore.QRect(90, 142, 133, 20))
        self.lne_c.setObjectName(_fromUtf8("lne_c"))
        self.label_3 = QtGui.QLabel(Dialog_address)
        self.label_3.setGeometry(QtCore.QRect(24, 114, 46, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lne_a1 = QtGui.QLineEdit(Dialog_address)
        self.lne_a1.setGeometry(QtCore.QRect(90, 86, 133, 20))
        self.lne_a1.setObjectName(_fromUtf8("lne_a1"))
        self.lne_i = QtGui.QLineEdit(Dialog_address)
        self.lne_i.setGeometry(QtCore.QRect(90, 58, 133, 20))
        self.lne_i.setObjectName(_fromUtf8("lne_i"))
        self.pushButton = QtGui.QPushButton(Dialog_address)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog_address)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 240, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog_address)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog_address.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_address)

    def retranslateUi(self, Dialog_address):
        Dialog_address.setWindowTitle(_translate("Dialog_address", "Dialog", None))
        self.label.setText(_translate("Dialog_address", "ID", None))
        self.label_4.setText(_translate("Dialog_address", "City", None))
        self.label_7.setText(_translate("Dialog_address", "Update Details", None))
        self.label_5.setText(_translate("Dialog_address", "Zip", None))
        self.label_6.setText(_translate("Dialog_address", "Profession", None))
        self.label_2.setText(_translate("Dialog_address", "Adress_1", None))
        self.label_3.setText(_translate("Dialog_address", "Adress_2", None))
        self.pushButton.setText(_translate("Dialog_address", "Save", None))
        self.pushButton_2.setText(_translate("Dialog_address", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_address = QtGui.QDialog()
    ui = Ui_Dialog_address()
    ui.setupUi(Dialog_address)
    Dialog_address.show()
    sys.exit(app.exec_())

