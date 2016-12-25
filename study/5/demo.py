#!/bin/env python
# _*_ coding:utf-8 _*_

import pexpect

mypassword = "123456"
child = pexpect.spawn('ssh root@192.168.100.150') # spawn 启动scp 程序
child.expect('password:') #expect 方法等待子程序产生的输出，判断是否匹配定义的字符串#'Password:'
child.sendline(mypassword) # 匹配后则发送密码串进行回应'
