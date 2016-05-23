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
import audioAnalysis
from audioplay import WavePlay
from FileSaver import FileSaver

class StartQT4(QtGui.QMainWindow):
    
    from dolnoPrzepustowy import lowPassRun
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.sendTool,QtCore.SIGNAL("clicked()"), self.sending)
        QtCore.QObject.connect(self.ui.recTool, QtCore.SIGNAL("clicked()"), self.receiving)
        QtCore.QObject.connect(self.ui.analyse, QtCore.SIGNAL("clicked()"), self.freqPlotting)
        QtCore.QObject.connect(self.ui.lowPass, QtCore.SIGNAL("clicked()"), self.lowPassFilter)
        #QtCore.QObject.connect(self.ui.FilePlayer, QtCore.SIGNAL("clicked()"), self.audioPlayer)
        QtCore.QObject.connect(self.ui.fileSaver, QtCore.SIGNAL("clicked()"), self.savingFile)
        self.data = ''
        self.filteredData = ''
        self.recor = TcpRec()
        self.anyFilterAlive = False
        
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
        self.savingFile()
        audioAnalysis.run() 
    
    def lowPassFilter(self):
        self.savingFile('temp.wav')
        time.sleep(0.2)
        thread.start_new_thread(self.lowPassRun, ())
        
    def audioPlayer(self):
        player = WavePlay()
        player.setData(self.data)
        thread.start_new_thread(player.run, ())
       
    def savingFile(self, fileName = ''):
        
        def savingMp3(usedData = 0):
            tempData = ''
            while True:
                if usedData == 0:
                    usedData = self.data
                else:
                    usedData = self.filteredData
                
                if self.recor.flagR:  
                    if usedData != tempData:
                        if not self.ui.Prompt.text() == "Rozpoczeto zapis do pliku":
                            self.ui.Prompt.setText("Rozpoczeto zapis do pliku")
                        
                        fs.setData(usedData)
                        fs.runMp3()
                        print 'Saved chunk to a file'
                        tempData = usedData
                if not self.recor.flagA:
                    fs.closeFile()
                    self.ui.Prompt.setText("Plik zapisano")
                    break
                
        def savingWav(dataUseFlag = 0):
            tempData = ''
            while True:
                if dataUseFlag == 0:
                    usedData = self.data
                else:
                    usedData = self.filteredData
                    
                if self.recor.flagR: 
                    if usedData != tempData:
                        if not fs.fileName == 'temp.wav':
                            if not self.ui.Prompt.text() == "Rozpoczeto zapis do pliku":
                                self.ui.Prompt.setText("Rozpoczeto zapis do pliku")
                        
                        fs.setData(usedData)
                        fs.runWav()
                        print 'Saved chunk to a file'
                        tempData = usedData
                        
                if not self.recor.flagA:
                    fs.closeFile()
                    if not fs.fileName == 'temp.wav':
                        self.ui.Prompt.setText("Plik zapisano")
                    break
        
        fs = FileSaver()
        
        if fileName == '':
            fileName = self.ui.FileSaveLine.text()
            
        if fileName == '':
            fileName = 'reqFile.wav'
            
        splittedFileName = fileName.split('.')
        
        fs.setFileType(splittedFileName[1])
        fs.setFileInit(fileName)

        if fs.FileType == 'wav':
            thread.start_new_thread(savingWav, ())
        else:
            thread.start_new_thread(savingMp3, ())
 
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