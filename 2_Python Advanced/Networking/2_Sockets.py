# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 13:59:43 2018

@author: SilverDoe
"""
'''
https://www.tutorialspoint.com/python/python_networking.htm

'''

'''=================== Server ================================================='''

import socket                                         

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
   txt = clientsocket.recv(1024)  
   print(txt.decode('ascii'))
   msg = 'Thank you for connecting to zombieApocalypse'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()
   
   
'''================== Client =================================================='''

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               
s.send('nice game'.encode('ascii'))
# Receive no more than 1024 bytes
msg = s.recv(1024)                                     

s.close()
print (msg.decode('ascii'))



'''============= General Socket Methods =======================================

1	s.recv() : This method receives TCP message

2	s.send() : This method transmits TCP message

3	s.recvfrom() : This method receives UDP message

4	s.sendto() : This method transmits UDP message

5	s.close() : This method closes socket

6	socket.gethostname() : Returns the hostname.

'''
   
   
