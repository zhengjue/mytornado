#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-08-30 16:29:35
############################

import dns.resolver

domain =  raw_input ('Please input an domain: ')    #输入域名地址

A = dns.resolver.query(domain , "A") #指定查询类型为A记录

for i in A.response.answer: #通过response.answer方法获取查询回应信息
    if not "CNAME" in str(i):
        for j in i.items:
            print j.address



if __name__ == "__main__":
    pass

