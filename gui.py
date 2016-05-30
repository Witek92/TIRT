# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(616, 390)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BoxReceiver = QtGui.QGroupBox(self.centralwidget)
        self.BoxReceiver.setGeometry(QtCore.QRect(170, 120, 141, 131))
        self.BoxReceiver.setObjectName(_fromUtf8("BoxReceiver"))
        self.PortrecTool = QtGui.QLineEdit(self.BoxReceiver)
        self.PortrecTool.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.PortrecTool.setObjectName(_fromUtf8("PortrecTool"))
        self.IPrecTool = QtGui.QLineEdit(self.BoxReceiver)
        self.IPrecTool.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.IPrecTool.setObjectName(_fromUtf8("IPrecTool"))
        self.BoxSender = QtGui.QGroupBox(self.centralwidget)
        self.BoxSender.setGeometry(QtCore.QRect(20, 100, 141, 181))
        self.BoxSender.setFlat(False)
        self.BoxSender.setCheckable(False)
        self.BoxSender.setObjectName(_fromUtf8("BoxSender"))
        self.FilePath = QtGui.QLineEdit(self.BoxSender)
        self.FilePath.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.FilePath.setObjectName(_fromUtf8("FilePath"))
        self.IPsendTool = QtGui.QLineEdit(self.BoxSender)
        self.IPsendTool.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.IPsendTool.setObjectName(_fromUtf8("IPsendTool"))
        self.PortsendTool = QtGui.QLineEdit(self.BoxSender)
        self.PortsendTool.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.PortsendTool.setObjectName(_fromUtf8("PortsendTool"))
        self.sendTool = QtGui.QPushButton(self.centralwidget)
        self.sendTool.setGeometry(QtCore.QRect(40, 290, 91, 31))
        self.sendTool.setObjectName(_fromUtf8("sendTool"))
        self.recTool = QtGui.QPushButton(self.centralwidget)
        self.recTool.setGeometry(QtCore.QRect(190, 290, 91, 31))
        self.recTool.setObjectName(_fromUtf8("recTool"))
        self.FileSaveLine = QtGui.QLineEdit(self.centralwidget)
        self.FileSaveLine.setGeometry(QtCore.QRect(450, 250, 121, 31))
        self.FileSaveLine.setObjectName(_fromUtf8("FileSaveLine"))
        self.fileSaver = QtGui.QPushButton(self.centralwidget)
        self.fileSaver.setGeometry(QtCore.QRect(470, 290, 91, 31))
        self.fileSaver.setObjectName(_fromUtf8("fileSaver"))
        self.analyse = QtGui.QPushButton(self.centralwidget)
        self.analyse.setGeometry(QtCore.QRect(460, 100, 131, 31))
        self.analyse.setObjectName(_fromUtf8("analyse"))
        self.lowPass = QtGui.QPushButton(self.centralwidget)
        self.lowPass.setGeometry(QtCore.QRect(460, 20, 131, 31))
        self.lowPass.setObjectName(_fromUtf8("lowPass"))
        self.Prompt = QtGui.QLabel(self.centralwidget)
        self.Prompt.setGeometry(QtCore.QRect(80, 20, 211, 51))

        self.echo=QtGui.QPushButton(self.centralwidget)
        self.echo.setGeometry(QtCore.QRect(460, 180, 131, 31))
        self.echo.setObjectName(_fromUtf8("echo"))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(11)
        self.Prompt.setFont(font)
        self.Prompt.setObjectName(_fromUtf8("Prompt"))
        self.PromptFrame = QtGui.QGraphicsView(self.centralwidget)
        self.PromptFrame.setGeometry(QtCore.QRect(70, 20, 221, 51))
        self.PromptFrame.setObjectName(_fromUtf8("PromptFrame"))
        self.cutFreq = QtGui.QLineEdit(self.centralwidget)
        self.cutFreq.setGeometry(QtCore.QRect(390, 20, 61, 31))
        self.cutFreq.setObjectName(_fromUtf8("cutFreq"))
        self.highPass = QtGui.QPushButton(self.centralwidget)
        self.highPass.setGeometry(QtCore.QRect(460, 60, 131, 31))
        self.highPass.setObjectName(_fromUtf8("highPass"))
        self.cutFreqHigh = QtGui.QLineEdit(self.centralwidget)
        self.cutFreqHigh.setGeometry(QtCore.QRect(390, 60, 61, 31))
        self.cutFreqHigh.setObjectName(_fromUtf8("cutFreqHigh"))
        self.buttonEqualizer = QtGui.QPushButton(self.centralwidget)
        self.buttonEqualizer.setGeometry(QtCore.QRect(460, 140, 131, 31))
        self.buttonEqualizer.setObjectName(_fromUtf8("buttonEqualizer"))
        self.BoxReceiver.raise_()
        self.BoxSender.raise_()
        self.sendTool.raise_()
        self.recTool.raise_()
        self.FileSaveLine.raise_()
        self.fileSaver.raise_()
        self.analyse.raise_()
        self.lowPass.raise_()
        self.PromptFrame.raise_()
        self.Prompt.raise_()
        self.cutFreq.raise_()
        self.highPass.raise_()
        self.cutFreqHigh.raise_()
        self.buttonEqualizer.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dżwiękowicz", None))
        self.BoxReceiver.setTitle(_translate("MainWindow", "Odbieranie", None))
        self.PortrecTool.setText(_translate("MainWindow", "50007", None))
        self.IPrecTool.setText(_translate("MainWindow", "127.0.0.1", None))
        self.BoxSender.setTitle(_translate("MainWindow", "Wysyłanie", None))
        self.FilePath.setText(_translate("MainWindow", "file.wav", None))
        self.IPsendTool.setText(_translate("MainWindow", "127.0.0.1", None))
        self.PortsendTool.setText(_translate("MainWindow", "50007", None))
        self.sendTool.setText(_translate("MainWindow", "Wyślij", None))
        self.recTool.setText(_translate("MainWindow", "Odbierz", None))
        self.fileSaver.setText(_translate("MainWindow", "Zapisz plik", None))
        self.analyse.setText(_translate("MainWindow", "Analiza dżwięku", None))
        self.lowPass.setText(_translate("MainWindow", "Filtr dolnoprzepustowy", None))
        self.Prompt.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.cutFreq.setText(_translate("MainWindow", "500.0", None))
        self.highPass.setText(_translate("MainWindow", "Filtr górnoprzepustowy", None))
        self.cutFreqHigh.setText(_translate("MainWindow", "1250.0", None))
        self.buttonEqualizer.setText(_translate("MainWindow", "Korektor graficzny", None))
        self.echo.setText(_translate("MainWindow", "Echo", None))


