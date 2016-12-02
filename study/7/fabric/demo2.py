#!/bin/env python
#_*_ coding:utf-8 _*_

from fabric.api import *

env.user = "root"
env.hosts= ['192.168.1.146','192.168.1.147']
env.password = "centos"

@runs_once
def input_raw():
    return prompt("please input directory name:", default="/tmp")

def worktask(dirname):
    run("ls -l "+dirname )


@task
def go():
    getdirname = input_raw()
    worktask(getdirname)
