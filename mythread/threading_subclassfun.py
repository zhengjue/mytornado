#!/bin/env python
# _*_ coding:utf-8 _*_

import threading
import time

sec_list=[2,4,6]

class MyThread(threading.Thread):
    def __init__(self,sec):
        threading.Thread.__init__(self)
        self.sec=sec

    def run(self):
         self.foo()

    def foo(self):
        start=time.ctime()
        print 'foo start on :',start
        time.sleep(self.sec)
        stop=time.ctime()
        print 'foo stop on:',stop

    def bar():
        start=time.ctime()
        print 'bar start on :',start
        time.sleep(4)
        stop=time.ctime()
        print 'bar stop on:',stop

if __name__ == "__main__":
    print "%s start on %s:" %(threading.current_thread().getName(),time.ctime())
    thread_list=[]
    for sec in  sec_list:
        t=MyThread(sec)
        print t.getName()
        thread_list.append(t)
        t.setName('hello'+str(sec))
        print t.getName()

    for T in  thread_list:
        T.start()

    print "threading list:" ,threading.enumerate()
    print "active thread count:",threading.active_count()

    for J in thread_list:
        J.join()
    print "main stop on:",time.ctime()
