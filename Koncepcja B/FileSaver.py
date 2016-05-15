#!/usr/bin/env python
# -*- coding: utf-8 -*-

class FileSaver():
    def __init__(self):
        self.fileName = ''
        self.data = ''
        self.outfile = ''
        
    def run(self):            
        self.outfile.write(self.data)
        
    def setData(self, data):
        self.data = data
        
    def setFileInit(self, name):
        self.fileName = name
        self.outfile = open(self.fileName, 'wb')
        
    def closeFile(self):
        self.outfile.close()
        