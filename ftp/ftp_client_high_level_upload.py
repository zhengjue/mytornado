#!/bin/env python
#_*_ coding:utf-8 _*_
import sys
import os
from  ftplib  import FTP
f = FTP("127.0.0.1")
print "welcome",f.getwelcome()
f.login(sys.argv[1],sys.argv[2])

print f.pwd()
print f.dir()

f.voidcmd("TYPE I")
#datasock,estsize = f.ntransfercmd("RETR ftp.txt")
datasock,estsize = f.ntransfercmd("STOR im.tar.gz")
estsize=os.stat("vim.tar.gz")[6]
transbytes = 0
fd= open('vim.tar.gz','rb')
while True:
    buf = fd.read(2048)
    if not len(buf):
        break
    datasock.sendall(buf)
    transbytes += len(buf)
    if estsize:
        print  str(round(transbytes/float(estsize),4)*100)+"%"



fd.close()
datasock.close()
f.voidresp()
f.close()

if __name__ == "__main__":
    pass
