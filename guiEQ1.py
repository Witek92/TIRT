# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiEQ1.ui'
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

class Eq_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(656, 256)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 200, 16, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.slider64 = QtGui.QSlider(self.centralwidget)
        self.slider64.setGeometry(QtCore.QRect(80, 40, 19, 160))
        self.slider64.setMaximum(100)
        self.slider64.setSliderPosition(50)
        self.slider64.setOrientation(QtCore.Qt.Vertical)
        self.slider64.setObjectName(_fromUtf8("slider64"))

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 200, 21, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.slider32 = QtGui.QSlider(self.centralwidget)
        self.slider32.setGeometry(QtCore.QRect(30, 40, 19, 160))
        self.slider32.setBaseSize(QtCore.QSize(0, 0))
        self.slider32.setMaximum(100)
        self.slider32.setPageStep(10)
        self.slider32.setProperty("value", 50)
        self.slider32.setOrientation(QtCore.Qt.Vertical)
        self.slider32.setObjectName(_fromUtf8("slider32"))

        self.slider1k = QtGui.QSlider(self.centralwidget)
        self.slider1k.setGeometry(QtCore.QRect(280, 40, 19, 160))
        self.slider1k.setMaximum(100)
        self.slider1k.setProperty("value", 50)
        self.slider1k.setOrientation(QtCore.Qt.Vertical)
        self.slider1k.setObjectName(_fromUtf8("slider1k"))

        self.slider8k = QtGui.QSlider(self.centralwidget)
        self.slider8k.setGeometry(QtCore.QRect(430, 40, 19, 160))
        self.slider8k.setMaximum(100)
        self.slider8k.setProperty("value", 50)
        self.slider8k.setOrientation(QtCore.Qt.Vertical)
        self.slider8k.setObjectName(_fromUtf8("slider8k"))

        self.slider16k = QtGui.QSlider(self.centralwidget)
        self.slider16k.setGeometry(QtCore.QRect(480, 40, 19, 160))
        self.slider16k.setMaximum(100)
        self.slider16k.setProperty("value", 50)
        self.slider16k.setOrientation(QtCore.Qt.Vertical)
        self.slider16k.setObjectName(_fromUtf8("slider16k"))

        self.slider250 = QtGui.QSlider(self.centralwidget)
        self.slider250.setGeometry(QtCore.QRect(180, 40, 19, 160))
        self.slider250.setMaximum(100)
        self.slider250.setProperty("value", 50)
        self.slider250.setOrientation(QtCore.Qt.Vertical)
        self.slider250.setObjectName(_fromUtf8("slider250"))

        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 200, 31, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(610, 200, 41, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))



        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 200, 21, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.slider125 = QtGui.QSlider(self.centralwidget)
        self.slider125.setGeometry(QtCore.QRect(130, 40, 19, 160))
        self.slider125.setMaximum(100)
        self.slider125.setProperty("value", 50)
        self.slider125.setOrientation(QtCore.Qt.Vertical)
        self.slider125.setObjectName(_fromUtf8("slider125"))

        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 200, 21, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.sliderAmp = QtGui.QSlider(self.centralwidget)
        self.sliderAmp.setGeometry(QtCore.QRect(560, 40, 19, 160))
        self.sliderAmp.setMaximum(4)
        self.sliderAmp.setProperty("value", int(1))
        self.sliderAmp.setOrientation(QtCore.Qt.Vertical)
        self.sliderAmp.setObjectName(_fromUtf8("sliderAmp"))

        self.sliderSpeed = QtGui.QSlider(self.centralwidget)
        self.sliderSpeed.setGeometry(QtCore.QRect(620, 40, 19, 160))
        self.sliderSpeed.setMinimum(1)
        self.sliderSpeed.setMaximum(5)

        self.sliderSpeed.setProperty("value", int(1))
        self.sliderSpeed.setOrientation(QtCore.Qt.Vertical)
        self.sliderSpeed.setObjectName(_fromUtf8("sliderSpeed"))


        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 16, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.slider4k = QtGui.QSlider(self.centralwidget)
        self.slider4k.setGeometry(QtCore.QRect(380, 40, 19, 160))
        self.slider4k.setMaximum(100)
        self.slider4k.setProperty("value", 50)
        self.slider4k.setOrientation(QtCore.Qt.Vertical)
        self.slider4k.setObjectName(_fromUtf8("slider4k"))

        self.slider2k = QtGui.QSlider(self.centralwidget)
        self.slider2k.setGeometry(QtCore.QRect(330, 40, 19, 160))
        self.slider2k.setMaximum(100)
        self.slider2k.setProperty("value", 50)
        self.slider2k.setOrientation(QtCore.Qt.Vertical)
        self.slider2k.setObjectName(_fromUtf8("slider2k"))

        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 200, 16, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 200, 16, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 200, 21, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.slider500 = QtGui.QSlider(self.centralwidget)
        self.slider500.setGeometry(QtCore.QRect(230, 40, 19, 160))
        self.slider500.setMaximum(100)
        self.slider500.setProperty("value", 50)
        self.slider500.setOrientation(QtCore.Qt.Vertical)
        self.slider500.setObjectName(_fromUtf8("slider500"))

        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 200, 16, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 200, 16, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Korektor graficzny", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">32</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">125</span></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">AMP</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">250</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">500</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">64</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">4k</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">2k</span></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">16k</span></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">8k</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">1k</span></p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SPEED</span></p></body></html>", None))

