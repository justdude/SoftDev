import socket


Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Socket.bind(("127.0.0.1",81))
Socket.listen(100)
conn, adr = Socket.accept()
print "Connected", adr

while True:
    data=conn.recv(1024) 
    if not data:
        break
    conn.send(data.upper())
conn.close()