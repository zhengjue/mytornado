#!/bine/env python
#_*_ coding:utf-8 _*_

import  multiprocessing
import time

def foo(interval):
    time.sleep(interval)

if  __name__ == "__main__":
     P=multiprocessing.Process(target=foo,args=(10,))
     P.start()
     P.join()
