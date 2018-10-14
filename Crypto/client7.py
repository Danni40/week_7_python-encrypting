#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import time                 #import time module to similate connection process
from CA2_example import main

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 443             # Reserve a port for your service.

s.connect((host, port))
#s.sendall(str.encode(input('Enter Greeting: ')))
print('Initiating Contact with the server...')
time.sleep(2)
data = s.recv(1024)
print('Certificate Received.  Validating Certificate..')
time.sleep(2)
print('Validation Successfull')




#data = s.recv(1024)
#print(data.decode("utf-8"))
##print(s.recv(1024).decode("utf-8"))
#s.close()