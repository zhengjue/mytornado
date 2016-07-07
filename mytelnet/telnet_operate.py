#!/bin/env python
#_*_ coding:utf-8 _*_

import telnetlib

host="127.0.0.1"
username="lza"
passwd="centos"

tn = telnetlib.Telnet(host)
tn.set_debuglevel(2)

tn.read_until("login:")
tn.write(username+"\n")

tn.read_until("passwd:")
tn.write(passwd+"\n")

tn.write("pwd \n")
tn.write("mkdir telnet_dir")
tn.readall()
tn.close()
