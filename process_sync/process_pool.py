#!/bine/env python
#_*_ coding:utf-8 _*_

import  multiprocessing
import time,os
import random

def long_time_task(name):
    print "run task %s %s" %(name,os.getpid())
    start = time.time()
    time.sleep(random.randint(1 , 5))
    end = time.time()
    print "task %s runs %s seconds" % (name,end-start)

if __name__ == "__main__":
    print "Major process %s " % os.getpid()
    P =multiprocessing.Pool()
    for i in range(10):
        P.apply_async(long_time_task,args=(i,))

    print "waiting for all subprocess done"
    P.close()
    P.join()
    print "all task done"
