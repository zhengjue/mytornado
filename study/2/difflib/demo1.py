#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-08-31 11:36:08
############################
import difflib
# 定义字符串1
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string"""
text1_lines = text1.splitlines()    # 以行进行分隔，以便进行对比
# 定义字符串2
text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""
text2_lines = text2.splitlines()

d = difflib.HtmlDiff()    # 创建HtmlDiff()对象
print d.make_file(text1_lines, text2_lines)


#  d = difflib.Differ()    # 创建Differ ()对象
#  diff = d.compare(text1_lines, text2_lines)    # 采用compare方法对字符串进行比较
#  print '\n'.join(list(diff))


if __name__ == "__main__":
    pass

