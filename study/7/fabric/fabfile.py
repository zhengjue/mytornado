#!/bin/env python
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
import time

@task
def host_type():
    run('uname -s')

@task
def test_dir():
    with settings(warn_only=True):
        if run("test -d /tmp/aa").failed and not confirm("put file failed , Continue[Y/N]?"):
            abort("Aborting file put task!")
    print "ok"


