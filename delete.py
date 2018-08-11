# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_DeleteWindow(object):
    def setupUi(self, DeleteWindow):
        DeleteWindow.setObjectName(_fromUtf8("DeleteWindow"))
        DeleteWindow.resize(367, 224)
        self.centralwidget = QtGui.QWidget(DeleteWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 171, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 75, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        DeleteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DeleteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        DeleteWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DeleteWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DeleteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DeleteWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteWindow)

    def retranslateUi(self, DeleteWindow):
        DeleteWindow.setWindowTitle(_translate("DeleteWindow", "DeleteWindow", None))
        self.label.setText(_translate("DeleteWindow", "DELETE DRUG", None))
        self.label_2.setText(_translate("DeleteWindow", "DRUG NAME:", None))
        self.pushButton.setText(_translate("DeleteWindow", "DELETE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DeleteWindow = QtGui.QMainWindow()
    ui = Ui_DeleteWindow()
    ui.setupUi(DeleteWindow)
    DeleteWindow.show()
    sys.exit(app.exec_())

