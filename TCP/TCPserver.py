import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Listening...')
conn, addr = s.accept()
print('Connected by', addr)
outfile = open("newfile.mp3", 'ab')
while True:
    data = conn.recv(1024)
    if not data: break
    outfile.write(data)
conn.close()
outfile.close()
print ("Completed.")