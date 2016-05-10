import socket

class TcpRec(socket.socket):
    
    name = ""
    HOST = ''
    PORT = 0

    def __init__(self):
        TcpRec.name = "file2.wav"
        TcpRec.HOST = '127.0.0.1'
        TcpRec.PORT = 50007
        
    def receive(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            s.listen(1)
        except socket.error, msg :
            if s:
                s.close()
            print 'Socket error: %s' % msg
            return 0
        
        print('Listening...')
        conn, addr = s.accept()
        print('Connected by', addr)
        outfile = open(self.name, 'wb')
        while True:
            data = conn.recv(1024)
            if not data: break
            outfile.write(data)
        conn.close()
        outfile.close()
        print ("Completed.")
        return True
    
    def setName(self,name):
        if (name==""):
            return 0
        TcpRec.name = name
    
    def setHost(self,hostname):
        if hostname == "":
            return 0
        TcpRec.HOST = hostname
        
    def setPort(self,portname):
        if portname == "":
            return 0
        TcpRec.PORT = portname
        