'''
Created on 25 05 2013

@author: roma
'''
import socket


Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Socket.connect(("127.0.0.1",81))

while True:
    str=raw_input("Enter string,please")
    Socket.send(str)
    data=Socket.recv(1024)
    print 'Received: '+data

Socket.close()

