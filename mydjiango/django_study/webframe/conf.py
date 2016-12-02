#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: conf.py
# Author: lza
# Created Time: 2016-10-24 14:46:41
############################

def index():
    html = "<h1>index page</h1>"
    return html

def login():
    html = '<h1> login page </h1>'
    return html


urls = (
    ("/index/",index),
    ("/login/",login),
)

if __name__ == "__main__":
    pass


