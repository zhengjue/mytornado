#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: test1.py
# Author: lza
# Created Time: 2016-10-24 10:25:46
############################

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("<h1>django test</h1>")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0',8000))
    sock.listen(5)

    while True:
        connect,add = sock.accept()
        handle_request(connect)
        connect.close()

if __name__ == "__main__":
    main()

