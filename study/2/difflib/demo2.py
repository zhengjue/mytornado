#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-08-31 11:36:08
############################
import difflib
import sys
try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except Exception as e:
    print "Error:"+ str(e)
    print "Usage:"+ sys.argv[0] +" filename1 filename2"
    sys.exit(1)


def readfile(filename):
    try:
        with open(filename, "rb") as f:
            filetext = f.read().splitlines()
            #  print filetext
        return filetext
    except IOError as e:
        print "read file %s Error: %s" %(filename, str(e))
        sys.exit(1)

if file1 == "" or file2 == "":
    print "Usage:"+ sys.argv[0] +" filename1 filename2"
    sys.exit(1)
file1_lines = readfile(file1)
file2_lines = readfile(file2)


d = difflib.HtmlDiff()
print d.make_file(file1_lines, file2_lines)

if __name__ == "__main__":
    pass

