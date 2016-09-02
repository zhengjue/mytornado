#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: my_pustil_test.py
# Author: lza
# Created Time: 2016-08-30 14:42:13
############################
import psutil
import datetime

print psutil.cpu_times()
print psutil.cpu_times().user

if __name__ == "__main__":
    pass

