#!/bine/env python
#_*_ coding:utf-8 _*_

import os

print "start main process",os.getpid()

p=os.fork()

if p == 0:
    print "current process is child process:  %s and parent process is:  %s" %(os.getpid(),os.getppid())

else:
    print "current process is :",os.getpid()

