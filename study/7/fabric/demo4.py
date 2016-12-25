#!/bin/env python
#_*_ coding:utf-8 _*_
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = "root"
#  env.gateway="192.168.1.146"
env.hosts= ['192.168.1.146','192.168.1.147']
env.password = "centos"
#  env.passwords = {
    #  'root@192.168.1.146:22': "centos",
#  }

@runs_once
def tar_task():
    with lcd("/var/log"):
        local("tar -czf boot.log.tar.gz boot.log")

@task
def put_task():
    run("mkdir /tmp/logs")
    with cd("/tmp/logs"):
        with settings(warn_only=True):
            result = put("/var/log/boot.log.tar.gz", "/tmp/logs/boot1.log.tar.gz")
        if result.failed and not confirm("put file failed Continue[Y/N]?"):
            abort("Aborting file put task")

@task
def check_task():
    with settings(warn_only=True):
        lmd5 = local("md5sum /var/log/boot.log.tar.gz", capture=True).split(" ")[0]
        rmd5 = run("md5sum /tmp/logs/boot1.log.tar.gz").split(" ")[0]
    if lmd5 == rmd5:
        print "OK"
    else:
        print "ERROR"

@task
def go():
    tar_task()
    put_task()
    check_task()
