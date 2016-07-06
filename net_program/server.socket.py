#!/bin/env python
# _*_ coding:utf-8 _*_

import socket

host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port))
s.listen(1)

while True:
    clientsock,clientaddr = s.accept()
    buf = clientsock.recv(2048)
    print buf
    clientsock.send("nice to meet you")
    clientsock.close()
