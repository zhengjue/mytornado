#!/bin/env python
# _*_ coding:utf-8 _*_

import subprocess

child=subprocess.Popen(["ping","-c","5","www.baidu.com"])
child.wait()

#print child.kill()
#child.send_signal()
#child.terminate()

#检查子进程的状态
print child.poll()

#主进程最后退出
print "parent process"

