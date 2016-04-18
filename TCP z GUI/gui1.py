# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(482, 361)
        self.sendTool = QtGui.QToolButton(Form)
        self.sendTool.setGeometry(QtCore.QRect(130, 230, 61, 31))
        self.sendTool.setObjectName(_fromUtf8("sendTool"))
        self.recTool = QtGui.QToolButton(Form)
        self.recTool.setGeometry(QtCore.QRect(310, 190, 61, 31))
        self.recTool.setObjectName(_fromUtf8("recTool"))
        self.IPsendTool = QtGui.QLineEdit(Form)
        self.IPsendTool.setGeometry(QtCore.QRect(60, 90, 131, 31))
        self.IPsendTool.setObjectName(_fromUtf8("IPsendTool"))
        self.IPrecTool = QtGui.QLineEdit(Form)
        self.IPrecTool.setGeometry(QtCore.QRect(280, 90, 131, 31))
        self.IPrecTool.setObjectName(_fromUtf8("IPrecTool"))
        self.PortsendTool = QtGui.QLineEdit(Form)
        self.PortsendTool.setGeometry(QtCore.QRect(60, 140, 131, 31))
        self.PortsendTool.setObjectName(_fromUtf8("PortsendTool"))
        self.PortrecTool = QtGui.QLineEdit(Form)
        self.PortrecTool.setGeometry(QtCore.QRect(280, 140, 131, 31))
        self.PortrecTool.setObjectName(_fromUtf8("PortrecTool"))
        self.FilegetTool = QtGui.QToolButton(Form)
        self.FilegetTool.setGeometry(QtCore.QRect(50, 230, 71, 31))
        self.FilegetTool.setObjectName(_fromUtf8("FilegetTool"))
        self.FilePath = QtGui.QLineEdit(Form)
        self.FilePath.setGeometry(QtCore.QRect(60, 190, 131, 31))
        self.FilePath.setObjectName(_fromUtf8("FilePath"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.sendTool.setText(_translate("Form", "Wyślij", None))
        self.recTool.setText(_translate("Form", "Odbierz", None))
        self.IPsendTool.setText(_translate("Form", "127.0.0.1", None))
        self.IPrecTool.setText(_translate("Form", "127.0.0.1", None))
        self.PortsendTool.setText(_translate("Form", "50007", None))
        self.PortrecTool.setText(_translate("Form", "50007", None))
        self.FilegetTool.setText(_translate("Form", "Wybierz plik", None))
        self.FilePath.setText(_translate("Form", "Ścieżka", None))

