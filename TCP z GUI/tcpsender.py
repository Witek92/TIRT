from array import array
from os import stat
import socket

class TcpSend(socket.socket):
    
    name = ""
    HOST = ''
    PORT = 0
        
    def __init__(self):
        TcpSend.name = "file.mp3"
        TcpSend.HOST = '127.0.0.1'
        TcpSend.PORT = 50007
    
    def send(self):
        arr = array('B') # create binary array to hold the wave file
        result = stat(TcpSend.name)  # sample file is in the same folder
        f = open(TcpSend.name, 'rb')
        arr.fromfile(f, result.st_size) # using file size as the array length
        print("Length of data: " + str(len(arr)))
          
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        s.send(arr)
        print('Finished sending...')
        s.close()
        print('done.')
        
    def setName(self,name):
        if (name==""):
            return 0
        TcpSend.name = name
    
    def setHost(self,hostname):
        if hostname == "":
            return 0
        TcpSend.HOST = hostname
        
    def setPort(self,portname):
        if portname == "":
            return 0
        TcpSend.PORT = portname