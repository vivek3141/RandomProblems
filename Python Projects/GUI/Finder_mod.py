import sys
from PyQt4 import QtCore, QtGui, uic

from Finder_auto import *


class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionFind, QtCore.SIGNAL('triggered()'), self.find)
        QtCore.QObject.connect(self.actionClear, QtCore.SIGNAL('triggered()'), self.clear)

    def clear(self):
        self.lineEdit.clear()
        self.textEdit.clear()

    def find(self):
        QtGui.QMessageBox.about(self, "How many", "Position found is (-1 means not found):" + str(
            self.textEdit.toPlainText().find(self.lineEdit.text(), 0)))


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
