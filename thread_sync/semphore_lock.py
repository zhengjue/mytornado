#!/bin/env python
# _*_ coding:utf-8 _*_

import time,random
import threading

class MyThread(threading.Thread):
    availableTables=["A","B","C","D","E"]

    def __init__(self,threadName,semaphore):
        self.interval=random.randint(1,6)
        self.semaphore=semaphore
        threading.Thread.__init__(self,name=threadName)

    def run(self):
        self.semaphore.acquire()
        table =MyThread.availableTables.pop()
        print "current thread name:",self.getName(),table
        time.sleep(self.interval)
        MyThread.availableTables.append(table)
        self.semaphore.release()

MySemaphore =threading.Semaphore(len(MyThread.availableTables))

def Test():
    threads =[]
    for i in range(10):
        threads.append(MyThread("thread"+str(i),MySemaphore))

    for i in threads:
        i.start()

if __name__ =="__main__":
    Test()

