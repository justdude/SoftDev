'''
Created on 25 05 2013

@author: roma
'''
import socket


Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Socket.bind("127.0.0.1",81)
Socket.bind()
print "Hello, World!"
print "Second hello world"