#!/bin/env python
# _*_ coding:utf-8 _*_

import time,random
import threading,Queue

q  = Queue.Queue()

class Produce(threading.Thread):
    def run(self):
        while True:
            num = random.randint(1,10000)
            q.put(num)
            print self.getName,"Produce put :" ,num
            time.sleep(1)

class Couster(threading.Thread):
    def run(self):
        while True:
            v = q.get()
            print self.getName,"Couster get :" ,v
            time.sleep(1)

if __name__ == "__main__":
    for i in range(2):
        p=Produce()
        p.start()

    for i in range(5):
        c=Couster()
        c.start()
