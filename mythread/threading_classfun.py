#!/bin/env python
# _*_ coding:utf-8 _*_

import threading
import time

sec_list=[2,4,6]
class ThreadFun(object):
    def __init__(self,sec):
        self.sec=sec

    def __call__(self):
        foo(self.sec)

def foo(sec):
    start=time.ctime()
    print 'foo start on :',start
    time.sleep(sec)
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
    thread_list=[]
    for sec in  sec_list:
        t = threading.Thread(target=ThreadFun(sec))
        thread_list.append(t)
    for T in  thread_list:
        T.start()
    for J in thread_list:
        J.join()
    print "main stop on:",time.ctime()
