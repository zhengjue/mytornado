import pexpect
import sys

ip = "192.168.1.146"
user = "root"
password = "centos"
target_file = "/var/log/boot.log"

child = pexpect.spawn('/usr/bin/ssh', [user+"@"+ip])
f=file("b.log",'w')
child.logfile = f


try:
    child.expect('(?i)password')
    child.sendline(password)
    child.expect("#")
    child.sendline(" tar -czf /var/log/boot.log.tar.gz "+target_file)

    child.expect("#")
    print child.before
    child.sendline("exit")
    f.close()
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"


child = pexpect.spawn('/usr/bin/scp' , [user+"@"+ip+':/var/log/boot.log.tar.gz','/tmp'])
f=file("b.log",'a')
child.logfile = f

try:
    child.expect('(?i)password')
    child.sendline(password)
    child.expect(pexpect.EOF)
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"

