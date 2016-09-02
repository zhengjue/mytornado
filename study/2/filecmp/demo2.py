#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo2.py
# Author: lza
# Created Time: 2016-08-31 14:20:08
############################
import os, sys
import filecmp
import re
import shutil
holderlist = []
src_list = []
# 递归获取更新
def compareme(dir1, dir2):
    dirobj = filecmp.dircmp(dir1, dir2)
    src_only = dirobj.left_only   # 获取源目录 新增的文件或目录
    #  print "new",src_only
    src_update = dirobj.diff_files  # 获取源目录 已经更新的文件
    #  print "update", src_update
    src_abspath = os.path.abspath(dir1)  # 定义源目录绝对路径
    # 将更新的文件或者目录追加到 holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in src_only]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in src_update]


    if len(dirobj.common_dirs) > 0:
        #判断是否存在相同子目录，以便递归
        for item in dirobj.common_dirs:
            #递归子目录
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
            #  print holderlist
    return holderlist


def get_destination_files(dir1, dir2):
    global holderlist
    source_files = []
    destination_files=[]
    createdir_bool=False

    dir1 = os.path.abspath(dir1)
    if not dir2.endswith("/"):
        dir2 = dir2+"/"
    dir2 = os.path.abspath(dir2)

    # 获取源目录新增的文件，目录和更新的文件
    source_files = compareme(dir1, dir2)
    for item in source_files:
        destination_dir = re.sub(dir1, dir2 ,item)
        destination_files.append(destination_dir)
        if os.path.isdir(item):  # 如果源目标是目录
            if not os.path.exists(destination_dir):  # 如果备份目标不存在此目录
                os.makedirs(destination_dir)
                createdir_bool = True

    if createdir_bool:
        holderlist = [] #由于holderlist 是一个全局变量，每一次重复调用遍历源目录函数前，都应该清空原来的东西
        # 递归本函数时，不管递归多少层，都应该把里边那层的返回值给上一层，不然不会取到第一层的值
        source_files, destination_files = get_destination_files(dir1, dir2)

    return (source_files, destination_files)


def main():
    try:
        if len(sys.argv) > 2:
            dir1=sys.argv[1]
            dir2=sys.argv[2]
            if not os.path.isdir(dir1) or not os.path.isdir(dir2):
                print "Usage:", sys.argv[0] , "datadir  backdir"
                sys.exit(1)

        else:
            print "Usage:", sys.argv[0] , "datadir  backdir"
            sys.exit(1)
    except Exception, e:
        print "Error:" + str(e)
        print "Usage:", sys.argv[0] , "datadir  backdir"
        sys.exit(1)


    # 获取源目录新增的文件，目录和更新的文件
    source_files, destination_files = get_destination_files(dir1, dir2)

    print "update item:"
    #  print source_files    # 输出更新项列表清单
    for i in source_files:
        print i
    #  print destination_files
    copy_pair = zip(source_files, destination_files)    # 将源目录与备份目录文件清单拆分成元组
    for item in copy_pair:
        if os.path.isfile(item[0]):    #判断是否为文件，是则进行复制操作
                shutil.copyfile(item[0], item[1])


if __name__ == "__main__":
    main()
