# _*_ coding:utf-8 _*_
from pexpect import pxssh
import getpass



try:
    s = pxssh.pxssh() # 创建pxssh对象
    hostname = raw_input("hostname:")
    username = raw_input("username:")
    password = getpass.getpass("please input passowd")
    s.login(hostname, username, password)
    s.sendline("uptime")
    s.prompt()
    print s.before
    s.sendline("ls -l")
    s.prompt()
    print s.before
    s.sendline("df")
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)

