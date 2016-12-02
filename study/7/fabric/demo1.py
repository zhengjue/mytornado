#!/bin/env python
#_*_ coding:utf-8 _*_

from fabric.api import *

env.user = "root"
env.hosts= ['192.168.1.146','192.168.1.147']
env.password = "centos"

@runs_once
def local_task():
    local("uname -a")

def remote_task():
    with cd("/var/log"):
        run("ls -l")

