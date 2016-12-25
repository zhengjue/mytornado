#!/bin/env python
#_*_ coding:utf-8 _*_

import paramiko

username = "root"
password = "centos"
hostname = "192.168.1.146"
port = 22

try:
    t = paramiko.Transport((hostname,port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put("/tmp/boot.log.tar.gz", "/tmp/b1.log.tar.gz")
    sftp.get("/tmp/b1.log.tar.gz", "/tmp/b2.log.tar.gz")
    sftp.mkdir("/tmp/userdir", 0755)
    sftp.rmdir("/tmp/userdir")
    sftp.rename("/tmp/b1.log.tar.gz", "/tmp/b11.log.tar.gz")
    print sftp.stat("/tmp/b11.log.tar.gz")
    print sftp.listdir("/tmp")
    t.close()
except Exception, e:
    print str(e)
