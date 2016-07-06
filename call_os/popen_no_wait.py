#!/bin/env python
# _*_ coding:utf-8 _*_

import subprocess

child=subprocess.Popen(["ping","-c","5","www.baidu.com"])
print "parent process"
