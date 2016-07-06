#!/bin/env python
# _*_ coding:utf-8 _*_

import threading
import time,sched

 #被调度触发的函数
def test_func(msg1,msg2):
        print "I m test_func",msg1,msg2

if __name__ == "__main__":
    t=threading.Timer(5,test_func,("msg1","msg2"))
    t.start()
    while True:
       time.sleep(1)
