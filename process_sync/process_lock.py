#!/bine/env python
#_*_ coding:utf-8 _*_

import  multiprocessing
import time

def foo(lock):
    lock.acquire()
    print "foo"
    time.sleep(3)
    lock.release()

def bar(lock):
    lock.acquire()
    print "bar"
    time.sleep(3)
    lock.release()

if  __name__ == "__main__":
     lock=multiprocessing.Lock()
     P1=multiprocessing.Process(target=foo,args=(lock,))
     P2=multiprocessing.Process(target=bar,args=(lock,))
     P1.start()
     P1.join()
     P2.start()
     P2.join()
