#!/usr/bin/env python
import socket
host = ''
port = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)

conn,addr = s.accept()
print 'Connected by ',addr
while True:
	data = conn.recv(1024)
	if data !='':
		print data
	else:
		break
	command = raw_input("Please input Your command: ")
	conn.sendall(command)

conn.close()
