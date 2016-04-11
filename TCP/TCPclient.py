from array import array
from os import stat
import socket

arr = array('B') # create binary array to hold the wave file
result = stat("file.mp3")  # sample file is in the same folder
f = open("file.mp3", 'rb')
arr.fromfile(f, result.st_size) # using file size as the array length
print("Length of data: " + str(len(arr)))

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(arr)
print('Finished sending...')
s.close()
print('done.')