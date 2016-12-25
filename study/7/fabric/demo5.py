#!/bin/env python
#_*_ coding:utf-8 _*_
from fabric.api import *
from fabric.colors import *
#  from fabric.context_managers import *
#  from fabric.contrib.console import confirm

env.user = "root"
env.roledefs = {
    'webservers':['192.168.1.146'],
    'dbservers':['192.168.1.147']
}
env.passwords = {
    'root@192.168.1.146:22': "centos",
    'root@192.168.1.147:22': "centos",
}


@roles("webservers")
def webtask():
    print yellow("install http")
    with settings(warn_only=True):
        run("yum -y install httpd")
        run("chkconfig --level 235 httpd on")

@roles("dbservers")
def dbtask():
    print yellow("install mysql-server mysql")
    with settings(warn_only=True):
        run("yum -y install mysql-server mysql")
        run("chkconfig --level 235 mysql on")

@roles("webservers", "dbservers")
def publicktask():
    print yellow("Install ntp epel")
    with settings(warn_only=True):
        run("rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run("yum -y install ntp")

def deploy():
    execute(publicktask)
    execute(webtask)
    execute(dbtask)
