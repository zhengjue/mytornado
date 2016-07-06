#!/bin/env python
#_*_ coding:utf-8 _*_
import sys
from  ftplib  import FTP
f = FTP("127.0.0.1")
print "welcome",f.getwelcome()
f.login(sys.argv[1],sys.argv[2])

print f.pwd()
print f.dir()

f.voidcmd("TYPE I")
#datasock,estsize = f.ntransfercmd("RETR ftp.txt")
datasock,estsize = f.ntransfercmd("RETR myvim.tar.gz")
transbytes = 0
fd= open('vim.tar.gz','wb')
while True:
    buf = datasock.recv(2048)
    if not len(buf):
        break
    fd.write(buf)
    transbytes += len(buf)
    if estsize:
        print  str(round(transbytes/float(estsize),4)*100)+"%"



fd.close()
datasock.close()
f.voidresp()
f.close()

if __name__ == "__main__":
    pass
