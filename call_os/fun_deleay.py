#!/bin/env python
# _*_ coding:utf-8 _*_

import time,sched

 #被调度触发的函数
def event_func(msg):
        print "Current Time:",time.time(),'msg:',msg

if __name__ == "__main__":
   #初始化sched模块的scheduler类
   s = sched.scheduler(time.time,time.sleep)
   #设置两个调度
   s.enter(1,2,event_func,("Small event.",))
   s.enter(2,1,event_func,("Big event.",))
   s.run()
   while True:
       time.sleep(100)
