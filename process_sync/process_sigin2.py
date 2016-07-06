#!/bine/env python
#_*_ coding:utf-8 _*_
import signal

#define signal handler function
def myHnadler(signum,frame):
    print "now , it's the time"
    exit()

#register signal.SIGTSTP's handler
signal.signal(signal.SIGTSTP, myHnadler)
signal.alarm(5)
while True:
    print "not yet"

