#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: test2.py
# Author: lza
# Created Time: 2016-10-24 11:06:57
############################
from wsgiref.simple_server import make_server

def handle_request(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>hello test django</h1>'



if __name__ == "__main__":
    httpd = make_server('', 8000, handle_request)
    print "server http on port 8000"
    httpd.serve_forever()

