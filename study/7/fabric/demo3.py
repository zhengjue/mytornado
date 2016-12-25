#!/bin/env python
#_*_ coding:utf-8 _*_
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = "root"
env.gateway="192.168.1.146"
env.hosts= ['192.168.1.147']
#  env.password = "centos"
env.passwords = {
    'root@192.168.1.146:22': "centos",
}

lpackpath = "/tmp/nginx-1.10.1.tar.gz"
rpackpath = "/tmp/install"

@task
def put_task():
    run("mkdir -p /tmp/install")

    with settings(warn_only=True):
        result = put(lpackpath, rpackpath)
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):
        abort("Aborting file put task!")

@task
def run_task():
    with cd("/tmp/install"):
        run("tar -zxvf nginx-1.10.1.tar.gz")
        with cd("nginx-1.10.1/"):
            run("./configure")

@task
def go():
    put_task()
    run_task()
