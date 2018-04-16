# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from register import Ui_RegisterWindow
from update import Ui_UpdateWindow
from delete import Ui_DeleteWindow
import sqlite3

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

class Ui_LoginWindow(object):
    def check(self):
        conn=sqlite3.connect('drug.db')
        conn.execute("SELECT * FROM drugs")

    def delete(self):
        self.delete=QtGui.QMainWindow()
        self.ui=Ui_DeleteWindow()
        self.ui.setupUi(self.delete)
        self.delete.show()


    def update(self):
        self.update=QtGui.QMainWindow()
        self.ui=Ui_UpdateWindow()
        self.ui.setupUi(self.update)
        self.update.show()


    def register(self):
        self.register=QtGui.QMainWindow()
        self.ui=Ui_RegisterWindow()
        self.ui.setupUi(self.register)
        self.register.show()


    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(486, 294)
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 70, 75, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.register)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 70, 75, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 150, 75, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_3.clicked.connect(self.update)

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 150, 75, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton_4.clicked.connect(self.delete)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LoginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow", None))
        self.label.setText(_translate("LoginWindow", "OWANBE PHARMACY", None))
        self.pushButton.setText(_translate("LoginWindow", "REGISTER", None))
        self.pushButton_2.setText(_translate("LoginWindow", "CHECK", None))
        self.pushButton_3.setText(_translate("LoginWindow", "UPDATE", None))
        self.pushButton_4.setText(_translate("LoginWindow", "DELETE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginWindow = QtGui.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

