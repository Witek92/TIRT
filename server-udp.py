#!/usr/bin/env python
import socket
import sys
import select
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
print >>sys.stderr, 'Starting up on %s. Port %s' % server_address
s.bind(server_address)

file1 = open('file1.mp3', 'ab')

try:
    while 1:
        data, address = s.recvfrom(4096)
        
        #Printing out received data, e.g. text
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
       # print repr(data)
        
        s.settimeout(2)
        file1.write(data)
        
except timeout:   
    plik.close()
    s.close()
    print "Received"



