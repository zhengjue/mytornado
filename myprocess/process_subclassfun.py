#!/bine/env python
#_*_ coding:utf-8 _*_

import  multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval=interval

    def run(self):
        n=3
        while n>0:
            print  "run:",time.time()
            time.sleep(self.interval)
            n -=1

if __name__ == "__main__":
    p=ClockProcess(3)
    p.start()
