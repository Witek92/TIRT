#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wave

class FileSaver():
    def __init__(self):
        self.fileName = ''
        self.data = ''
        self.outfile = ''
        self.FileType = ''
        
    def runMp3(self):            
        self.outfile.write(self.data)
        
    def runWav(self):
        self.outfile.writeframes(self.data)
        
    def setData(self, data):
        self.data = data
        
    def setFileInit(self, name):
        self.fileName = str(name)
        if self.FileType == 'mp3':
            self.outfile = open(self.fileName, 'wb')
        if self.FileType == 'wav':
            self.outfile = wave.open(self.fileName, 'wb')
            self.outfile.setparams((1,2,16000,0,'NONE','not compressed'))
        
    def closeFile(self):
        self.outfile.close()
        
    def setFileType(self, Ftype):
        self.FileType = Ftype
    
        