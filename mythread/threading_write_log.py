#!/bin/env python
# _*_ coding:utf-8 _*_

import threading
import time
import sys
"""
多线程生成日志
"""

_author="lza"

#写入500行警告日志
def WriteWarnLog(logfile,lock):
    count=0
    while count<500:
        try:
            lock.acquire()
            logfile.write('%s|zookeeper|WARN|m1|172.17.1.15\n'%(time.ctime()))
            count +=1
            lock.release()
        except Exception ,e:
            print  'write warn log error',str(e)
            break
    print  'write warn log finished'


#写入200行错误日志
def WriteErrorLog(logfile,lock):
    count=0
    while count<200:
        try:
            lock.acquire()
            logfile.write('%s|zookeeper|ERROR|m1|all\n'%(time.ctime()))
            count +=1
            lock.release()
        except Exception ,e:
            print  'write error log error',str(e)
            break
    print  'write error log finished'

def main():
   with  open("logfile.txt","a+") as  logfile:
        try:
            lock=threading.Lock()
            t1=threading.Thread(target=WriteWarnLog,args=(logfile,lock))
            t2=threading.Thread(target=WriteErrorLog,args=(logfile,lock))

            t1.start()
            t2.start()

            t1.join()
            t2.join()

        except  Exception ,e:
            print  "write log falied!!",str(e)
            sys.exit()
        finally :
            logfile.close()
        print "log write finished"

if __name__ == "__main__":
    main()
