#!/bin/env python
#_*_ coding:utf-8 _*_

import time
import threading

def foo(lock1,lock2):
    print "enter foo"
    time.sleep(4)
    lock2.acquire()
    lock1.release()
    lock2.release()

def bar(lock1,lock2):
    print "entrer bar"
    time.sleep(4)
    lock2.acquire()
    lock1.release()
    lock2.release()


if  __name__ == "__main__":
    locks= []
    for i in   range(2):
        lock=threading.Lock()
        lock.acquire()
        locks.append(lock)

    t1=threading.Thread(target=foo,args=(locks))
    t2=threading.Thread(target=bar,args=(locks[::-1]))
    threads=[t1,t2]

    for i in threads:
        i.start()

    for i in  threads:
        i.join()
