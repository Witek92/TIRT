#!/usr/bin/env python
import socket
import sys
import select
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print >>sys.stderr, 'Starting up on %s. Port %s' % server_address
s.bind(server_address)

file1 = open('file.mp3', 'ab')


while 1:

    try:
        data, address = s.recvfrom(4096)
        
        #Printing out received data, e.g. text
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
       # print repr(data)
        
        s.settimeout(2)
        file1.write(data)
        
    except:
        break

file1.close()
s.close()
print "Received"



