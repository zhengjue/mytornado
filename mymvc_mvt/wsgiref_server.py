#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: wsgiref_server.py
# Author: lza
# Created Time: 2016-08-08 14:49:38
############################

from wsgiref.simple_server import make_server


def RunServer(request_env, response):
    response("200 ok", [('Content-Type', 'text/html')])
    return "<h1>hello world!!</h1>"

if __name__ == "__main__":
    httpd = make_server("", 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()
