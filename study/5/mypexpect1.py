import pexpect
import sys

child = pexpect.spawn('ssh root@192.168.1.146')
f = open("mylog.txt",'w')
child.logfile = f
#child.logfile = sys.stdout

child.expect("password:")
child.sendline("centos")
child.expect("#")
child.sendline('ls /home')
child.expect("#")
