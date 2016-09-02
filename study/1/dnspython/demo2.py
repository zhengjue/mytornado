#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-08-30 16:29:35
############################

import dns.resolver

domain =  raw_input ('Please input an domain: ')    #输入域名地址

NS = dns.resolver.query(domain , "NS") #指定查询类型为A记录

for i in NS.response.answer:  # 遍历回应结果，输出MX记录的preference及exchanger信息
    for j in i.items:
        print j.to_text()



if __name__ == "__main__":
    pass

