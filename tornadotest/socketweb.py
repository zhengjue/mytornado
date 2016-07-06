#!/usr/bin/env python
#coding:utf-8

import socket

def handle_request(client_conn):
    buf=client_conn.recv(1024)
    client_conn.send("HTTP/1.1 200 OK\r\n\r\n")
    client_conn.send("Hello world!!")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("0.0.0.0",8888))
    sock.listen(5)

    while 1:
        conn,address=sock.accept()
        handle_request(conn)
        conn.close()

if __name__ == "__main__":
    main()
