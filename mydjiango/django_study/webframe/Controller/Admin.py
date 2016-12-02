#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: Admin.py
# Author: lza
# Created Time: 2016-10-24 16:06:42
############################
def index():
    f = file("/home/lza/mycord/mydjiango/django_study/webframe/View/index.html")
    f=f.read()
    return f


if __name__ == "__main__":
    pass

