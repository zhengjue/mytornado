# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from pexpect import pxssh
import getpass
import pexpect
import sys


child = pexpect.spawn('ftp 127.0.0.1')
child.expect('(?i)name .*:')
child.sendline('lza')
child.expect('(?i)password')
child.sendline('centos')
child.expect('ftp> ')
child.sendline("bin")
child.expect('ftp> ')
child.sendline("get ftp.txt")
child.expect('ftp> ')
sys.stdout.write(child.before)
print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush()
child.interact()
child.sendline('bye')
child.close()

