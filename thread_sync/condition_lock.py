#!/bin/env python
# _*_ coding:utf-8 _*_

import time,random
import threading

count=500
Mycondition =threading.Condition()

class Produce(threading.Thread):
    def run(self):
        global count
        while True:
            if Mycondition.acquire():
                if count >1000:
                    Mycondition.wait()
                else:
                    count +=100
                    msg=self.name + "Produce 100, count=",str(count)
                    print msg
                    Mycondition.notify()

            Mycondition.release()
            time.sleep(1)


class Couster(threading.Thread):
    def run(self):
        global count
        while True:
            if Mycondition.acquire():
                if count <100:
                    Mycondition.wait()
                else:
                    count -=10
                    msg=self.name + "Couster 10, count=",str(count)
                    print msg
                    Mycondition.notify()

            Mycondition.release()
            time.sleep(1)

if __name__ == "__main__":
    cs = []
    p = Produce()
    for i in range(1,10):
        a=Couster()
        cs.append(a)

    p.start()
    for i in cs:
        i.start()
