#!/bine/env python
#_*_ coding:utf-8 _*_

import  multiprocessing
import time

def worker1(interval):
    print "worker1 start"
    time.sleep(interval)
    print "worker1 stop"


def worker2(interval):
    print "worker2 start"
    time.sleep(interval)
    print "worker2 stop"


def worker3(interval):
    print "worker3 start"
    time.sleep(interval)
    print "worker3 stop"

if  __name__ == "__main__":
     P1=multiprocessing.Process(target=worker1,args=(2,))
     P2=multiprocessing.Process(target=worker2,args=(3,))
     P3=multiprocessing.Process(target=worker3,args=(4,))
     print "the number of  cpu:" ,multiprocessing.cpu_count()
     P1.start()
     P2.start()
     P3.start()
     for p in multiprocessing.active_children():
        print "current active child name :",p.name+"   current process pid is :",p.pid
     P1.join()
     P2.join()
     P3.join()
