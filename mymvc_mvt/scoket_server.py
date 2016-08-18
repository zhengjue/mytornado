#!/bin/env python
# _*_ coding:utf-8 _*_

import socket


def handler_request(client_connnect):
    buf = client_connnect.recv(1024)
    client_connnect.send("HTTP/1.1 200 OK\r\n\r\n")
    client_connnect.send("Hello, Seven")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", 8000))
    server_socket.listen(5)

    while True:
        client_connnect, clent_addr = server_socket.accept()
        handler_request(client_connnect)
        client_connnect.close()

if __name__ == "__main__":
    main()

