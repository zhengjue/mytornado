#!/bin/env python
# _*_ coding:utf-8 _*_

import socket

host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.sendall("hello")

while True:
    buf = s.recv(2048)
    if not len(buf):
        break
    print buf
    s.send("nice to meet server")
