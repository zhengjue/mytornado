#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-08-31 13:54:07
############################
import filecmp

print filecmp.cmp("file1.txt", "file2.txt")

print filecmp.cmpfiles("dir1", "dir2", ['f1', 'f2', 'f3', 'f4', 'f5'] )


if __name__ == "__main__":
    pass

