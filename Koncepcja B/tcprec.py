import socket

class TcpRec(socket.socket):
    
    HOST = ''
    PORT = 0    
    

    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 50007
        self.data = ''
        self.flagR = False
        self.flagA = False
        
    def receive(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            s.listen(1)
        except socket.error, msg:
            if s:
                s.close()
            print 'Socket error: %s' % msg
            return 0
        self.flagA = True
        print('Listening...')
        conn, addr = s.accept()
        print('Connected by', addr)
        self.flagR = True
        while True:
            self.data = conn.recv(1024)
            if not self.data: break
        conn.close()
        print ("Completed.")
        self.flagR = False
        self.flagA = False
    
    def setHost(self,hostname):
        if hostname == "":
            return 0
        TcpRec.HOST = hostname
        
    def setPort(self,portname):
        if portname == "":
            return 0
        TcpRec.PORT = portname
        
    def getData(self):
        return self.data
    
        