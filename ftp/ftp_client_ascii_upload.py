#!/bin/env python
#_*_ coding:utf-8 _*_
import sys
from  ftplib  import FTP
f = FTP("127.0.0.1")
print "welcome",f.getwelcome()
f.login(os.argv[1],os.argv[2])

print f.pwd()
print f.dir()

fd= open('download.txt','rt')


f.storlines("STOR ftp_upload.txt",fd)

fd.close()
f.close()

if __name__ == "__main__":
    pass
