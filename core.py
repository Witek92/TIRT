#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import thread
import time

from PyQt4 import QtCore, QtGui

import audioAnalysis
from FileSaver import FileSaver
from gui import Ui_MainWindow
from guiEQ1 import Eq_Form
from tcprec import TcpRec
from tcpsender import TcpSend


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.sendTool,QtCore.SIGNAL("clicked()"), self.sending)
        QtCore.QObject.connect(self.ui.recTool, QtCore.SIGNAL("clicked()"), self.receiving)
        QtCore.QObject.connect(self.ui.analyse, QtCore.SIGNAL("clicked()"), self.freqPlotting)
        QtCore.QObject.connect(self.ui.lowPass, QtCore.SIGNAL("clicked()"), self.lowPassFilter)
        QtCore.QObject.connect(self.ui.highPass, QtCore.SIGNAL("clicked()"), self.highPassFilter)
        QtCore.QObject.connect(self.ui.echo,QtCore.SIGNAL("clicked()"), self.echoRun)
        QtCore.QObject.connect(self.ui.buttonEqualizer, QtCore.SIGNAL("clicked()"), self.eqinit)

        #QtCore.QObject.connect(self.ui.buttonEqualizer, QtCore.SIGNAL("clicked()"), self.eqR)



        #QtCore.QObject.connect(self.ui.FilePlayer, QtCore.SIGNAL("clicked()"), self.audioPlayer)
        QtCore.QObject.connect(self.ui.fileSaver, QtCore.SIGNAL("clicked()"), self.savingFile)
        self.data = ''
        self.filteredData = ''
        self.recor = TcpRec()
        self.lowPassFilterRunCounter = 0
        self.highPassFilterRunCounter = 0
        self.echoRunCounter = 0
        self.eqRunCounter = 0
        self.speedRunCounter=0

        self.filterRunningAllowed = True
        
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

    def echoRun(self):
        if self.echoRunCounter%2 == 0:
            self.savingFile('temp.wav')
            time.sleep(0.2)
            thread.start_new_thread(self.echoR, ())
        else:
            self.filterRunningAllowed = False
            self.ui.Prompt.setText("Echo wylaczone")

        self.echoRunCounter += 1
        time.sleep(0.2)
        self.filterRunningAllowed = True

    def eqR(self):
        if self.eqRunCounter%2 == 0:
            self.savingFile('temp.wav')
            time.sleep(0.2)
            thread.start_new_thread(self.eqRun, ())
        else:
            self.filterRunningAllowed = False
            self.ui.Prompt.setText("Eq wylaczone")

        self.eqRunCounter += 1
        time.sleep(0.2)
        self.filterRunningAllowed = True

    def freqPlotting(self):
        self.savingFile('temp.wav')
        audioAnalysis.run()

    def eqinit(self):
        self.myeq = StartEQ()
        self.myeq.show()
        #self.eqR()
        self.speedinit()
    def speedinit(self):
        if self.speedRunCounter%2 == 0:
            self.savingFile('temp.wav')
            time.sleep(0.2)
            thread.start_new_thread(self.speedRun, ())
        else:
            self.filterRunningAllowed = False
            self.ui.Prompt.setText("Echo wylaczone")

        self.speedRunCounter += 1
        time.sleep(0.2)
        self.filterRunningAllowed = True
    
    def lowPassFilter(self):
        if self.lowPassFilterRunCounter%2 == 0:
            self.savingFile('temp.wav')
            time.sleep(0.2)
            thread.start_new_thread(self.lowPassRun, ())
        else:
            self.filterRunningAllowed = False
            self.ui.Prompt.setText("Filtr dolnoprzepustowy wylaczony")
            
        self.lowPassFilterRunCounter += 1
        time.sleep(0.2)
        self.filterRunningAllowed = True


    def highPassFilter(self):
        if self.highPassFilterRunCounter%2 == 0:
            self.savingFile('temp.wav')
            time.sleep(0.2)
            thread.start_new_thread(self.highPassRun, ())
        else:
            self.filterRunningAllowed = False
            self.ui.Prompt.setText("Filtr gornoprzepustowy wylaczony")

        self.highPassFilterRunCounter += 1
        time.sleep(0.2)
        self.filterRunningAllowed = True
        
        
    def audioPlayer(self):
        player = WavePlay()
        player.setData(self.data)
        thread.start_new_thread(player.run, ())
       
    def savingFile(self, fileName = ''):
        
        def savingMp3(dataFlag = 0):
            tempData = ''
            while True:
                if dataFlag == 0:
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
                
        def savingWav_forFilters():
            tempData = ''
            while True:
                if self.filterRunningAllowed:
                    if self.recor.flagR: 
                        if not self.data == tempData:
                            if not fs.fileName == 'temp.wav':
                                if not self.ui.Prompt.text() == "Rozpoczeto zapis do pliku":
                                    self.ui.Prompt.setText("Rozpoczeto zapis do pliku")
                            
                            fs.setData(self.data)
                            fs.runWav()
                            print 'Saved chunk to a file'
                            tempData = self.data
                            
                    if not self.recor.flagA:
                        fs.closeFile()
                        if not fs.fileName == 'temp.wav':
                            self.ui.Prompt.setText("Plik zapisano")
                        break
                else:
                    break
        
        def savingWavStandard():
            tempData = ''
            while True:
                if len(self.filteredData) == 0:
                    usedData = self.data
                else:
                    usedData = self.filteredData
                    
                if self.recor.flagR: 
                    if not usedData == tempData:
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
        
        if fs.fileName == 'temp.wav':
            thread.start_new_thread(savingWav_forFilters, ())
            
        elif fs.FileType == 'wav':
            thread.start_new_thread(savingWavStandard, ())
                
        elif fs.FileType == 'mp3':
            thread.start_new_thread(savingMp3, ())
            
        else:
            self.ui.Prompt.setText("Nieobslugiwany format pliku")
 
    def gettingRecdData(self):
        while True:
            if self.recor.flagR:
                if self.data != self.recor.getData():
                    self.data = self.recor.getData()
                    if self.recor.getData() == '':
                        break
            if not self.recor.flagA:
                break
                
class StartEQ(QtGui.QWidget, Eq_Form):

    def __init__(self, parent=None):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)

        
        
                
if __name__ == "__main__":
    try:
        app = QtGui.QApplication(sys.argv)
        myapp = StartQT4()
        myapp.show()     
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print "Exited"
