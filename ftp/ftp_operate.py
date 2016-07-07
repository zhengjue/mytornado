#!/bin/env python
#_*_ coding:utf-8 _*_
import sys
from  ftplib  import FTP
f = FTP("127.0.0.1")
print "welcome",f.getwelcome()
f.login(sys.argv[1],sys.argv[2])

print f.pwd()
print f.dir()
#print "*"*40
#print f.nlst()
#print "*"*40
#f.delete("ftp.txt")
#print "*"*40
#print f.dir()
#f.rmd("ftp.dir")
#print f.dir()
print "*"*40
#f.mkd("ftp.dir.new")
f.rename("ftp.dir.new","ftp.dir")
f.close()

if __name__ == "__main__":
    pass
