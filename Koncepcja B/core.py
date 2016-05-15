#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import thread
import threading
import time
import pyaudio
import wave
from PyQt4 import QtCore, QtGui
from gui import Ui_MainWindow
from tcpsender import TcpSend
from tcprec import TcpRec
#import audioAnalysis
#import dolnoPrzepustowy
from audioplay import WavePlay
from FileSaver import FileSaver

class StartQT4(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.sendTool,QtCore.SIGNAL("clicked()"), self.sending)
        QtCore.QObject.connect(self.ui.recTool, QtCore.SIGNAL("clicked()"), self.receiving)
        #QtCore.QObject.connect(self.ui.analyse, QtCore.SIGNAL("clicked()"), self.freqPlotting)
        #QtCore.QObject.connect(self.ui.lowPass, QtCore.SIGNAL("clicked()"), dolnoPrzepustowy.run)
        QtCore.QObject.connect(self.ui.FilePlayer, QtCore.SIGNAL("clicked()"), self.audioPlayer)
        QtCore.QObject.connect(self.ui.fileSaver, QtCore.SIGNAL("clicked()"), self.savingFile)
        self.data = ''
        self.recor = TcpRec()
        
    def sending(self):            
        sender = TcpSend()          
        sender.setName(self.ui.FilePath.text())
        sender.setHost(self.ui.IPsendTool.text())
        sender.setPort(int(self.ui.PortsendTool.text()))        
        thread.start_new_thread(sender.send, ())
        self.ui.Prompt.setText("Wysylanie...")
      
    def receiving(self):
        #recor = TcpRec()
        #recor.setName(self.ui.FilePath.text())
        self.recor.setHost(self.ui.IPrecTool.text())
        self.recor.setPort(int(self.ui.PortrecTool.text()))
        self.ui.Prompt.setText("Oczekiwanie na połączenie...")
        thread.start_new_thread(self.recor.receive, ())
        thread.start_new_thread(self.gettingRecdData, ())
        
    def freqPlotting(self):
        audioAnalysis.run() 
        
    def audioPlayer(self):
        player = WavePlay()
        player.setName(TcpRec.name)
        thread.start_new_thread(player.run, ())
        
    def savingFile(self):
        def saving():
            tempData = ''
            while True:
                if self.recor.flagR:  
                    if self.data != tempData:
                        if not self.ui.Prompt.text() != "Rozpoczęto zapis do pliku":
                            self.ui.Prompt.setText("Rozpoczęto zapis do pliku")
                        
                        fs.setData(self.data)
                        fs.run()
                        print 'Saved chunk to a file'
                        tempData = self.data
                if not self.recor.flagA:
                    fs.closeFile()
                    self.ui.Prompt.setText("Plik zapisano")
                    break; 
        fs = FileSaver()
        try:
            fs.setFileInit(self.ui.FileSaveLine.text())
        except IOError:
            self.ui.Prompt.setText("Zapis niemożliwy")
            return 0
        
        thread.start_new_thread(saving, ())

        
        
    def gettingRecdData(self):
        while True:
            if self.recor.flagR:
                if self.data != self.recor.getData():
                    self.data = self.recor.getData()
                    if self.recor.getData() == '':
                        break
            if not self.recor.flagA:
                break
                
        
        
        
                
if __name__ == "__main__":
    try:
        app = QtGui.QApplication(sys.argv)
        myapp = StartQT4()
        myapp.show()     
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print "Exited"