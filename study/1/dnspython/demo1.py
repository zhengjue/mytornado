#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-08-30 16:29:35
############################

import dns.resolver

domain =  raw_input ('Please input an domain: ')    #输入域名地址

MX = dns.resolver.query(domain , "MX") #指定查询类型为A记录

for i in MX:  # 遍历回应结果，输出MX记录的preference及exchanger信息
    print 'MX preference =', i.preference, 'mail exchanger =', i.exchange



if __name__ == "__main__":
    pass

