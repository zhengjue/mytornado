#!/bin/env python
# _*_ conding:utf-8 _*_

import time

def foo():
    start=time.ctime()
    print 'foo start on :',start
    time.sleep(2)
    stop=time.ctime()
    print 'foo stop on:',stop

def bar():
    start=time.ctime()
    print 'bar start on :',start
    time.sleep(4)
    stop=time.ctime()
    print 'bar stop on:',stop

if __name__ == "__main__":
    print "main start on :",time.ctime()
    foo()
    bar()
    print "main stop on:",time.ctime()
