#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: test3.py
# Author: lza
# Created Time: 2016-10-24 11:29:30
############################
#  自己定框架

from wsgiref.simple_server import make_server
import conf

def Request_handler(Environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 获取用户请求URL
    #  envrion 包含用户请求的一切信息
    userurls = Environ['PATH_INFO']

    for item in conf.urls:
        if item[0] == userurls: #  如果url路由表里的某条正则对应用户访问url
            return item[1]() #  返回正则对应的处理函数

    return "404"



    #  if urls == "/index/":
        #  return "<h1>index</h1>"
    #  elif urls == '/login/':
        #  return "<h1>login</h1>"
    #  else:
        #  return "<h1>404 no found</h1>"


if __name__ == "__main__":
    httpd = make_server('',8000,Request_handler)
    print "Server HTTP on port 8000"
    httpd.serve_forever()

