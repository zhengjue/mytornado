#!/bin/env python
#_*_ coding:utf-8 _*_
import sys
from  ftplib  import FTP
f = FTP("127.0.0.1")
print "welcome",f.getwelcome()
f.login(sys.argv[1],sys.argv[2])

print f.pwd()
print f.dir()

fd= open('vim.tar.gz','rb')


f.storbinary("STOR ftp_upload1.txt",fd)

fd.close()
f.close()

if __name__ == "__main__":
    pass
