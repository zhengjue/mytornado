#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: webFrame.py
# Author: lza
# Created Time: 2016-10-24 15:42:40
############################
from wsgiref.simple_server import make_server
from Controller import Admin, Account
"""
def index():
    html = "return index page"
    return html


def login():
    html = "return login page"
    return html

"""
urls = (
    ("/index/", Admin.index),
    ("/login/", Account.login),
)

def Request_Hndele(env, response):
    response("200 OK", [("Content-Type", "text/html")])
    userurl=env["PATH_INFO"]

    for item in urls:
        if item[0] == userurl:
            return item[1]()

    return "404"


if __name__ == "__main__":
    httpd = make_server("",8000,Request_Hndele)
    print "start web server start 8000"
    httpd.serve_forever()
