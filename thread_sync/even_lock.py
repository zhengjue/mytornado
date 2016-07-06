#!/bin/env python
# _*_ coding:utf-8 _*_

import time,random
import threading

Event  = threading.Event()
aList = []

class Produce(threading.Thread):
    def run(self):
        while True:
            aList.append(1)
            print "add 1"
            Event.set() #设置事件
            Event.clear() #发送事件
            time.sleep(3)

class Couster(threading.Thread):
    def run(self):
        while True:
            Event.wait() #等待事件被触发
            print aList

if __name__ == "__main__":
    p=Produce()
    p.start()
    c=Couster()
    c.start()
