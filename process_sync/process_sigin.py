#!/bine/env python
#_*_ coding:utf-8 _*_

import signal

#define signal handler function
def myHnadler(signum,frame):
    print"I received:",signum

#register signal.SIGTSTP's handler
signal.signal(signal.SIGTSTP, myHnadler)
signal.pause()
print "END of Signal Demo"

