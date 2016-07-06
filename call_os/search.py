#!/bin/env python
#_*_ coding:utf-8 _*_

import os
import sys

def search(str1,path=None):
    if path==None:
        mypath=os.getcwd()
    else:
        try:
            if os.path.isdir(path):
                mypath=path
        except:
            return "input path error"

    for root,dirs,names in os.walk(mypath):
        for filename in names:
            if str1 in filename:
                filepath=os.path.join(root,filename)
                print filepath


if __name__ == "__main__":
    search("s","/etc")
