#!/bin/env python
# _*_ coding:utf-8 _*_

import threading
import time

count = 2

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
    # thread.start_new_thread(foo,())
    # thread.start_new_thread(bar,())
    #因为thread模块没有结束控制，主线程结束全部就结束
    #time.sleep(6)#手动控制睡眠,方法一
    # while 1:
    #     if not count: #不断循环检测计数是否为0，为0表示所有线程执行完毕
    #        break
    t1=threading.Thread(target=foo)
    t2=threading.Thread(target=bar)
    #t1.setDaemon(True)#不阻塞主线程，主线程结束时，也让福线程一起结束
    #t2.setDaemon(True)
    t1.start()#没有加join时，主线程结束了福线程还在后台执行
    t2.start()
    #t1.join()#阻塞主线程等待福线程结束才能让主线程结束
    #t2.join()
    print "main stop on:",time.ctime()
