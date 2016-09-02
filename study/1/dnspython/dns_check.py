#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-08-30 16:29:35
############################

import dns.resolver
import os
import httplib

iplist=[]    #定义域名IP列表变量
appdomain="www.baidu.com"    #定义业务域名"

def get_iplist (domain=""):    #域名解析函数，解析成功IP将被追加到iplist
    try:
        A = dns.resolver.query(domain, "A")
    except Exception, e:
        print "dns resolver error:" + str(e)
        return
    for i in A.response.answer:
        if not "CNAME" in str(i):
            for j in i.items:
                iplist.append(j.address)
    return True

def checkip(ip):
    url = ip + ":80"
    result = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(url)
    try:
        conn.request("GET", "/", headers = {"Host": appdomain})  # 发起URL请求，添加host主机头
        r=conn.getresponse()
        result = r.read(15)   #获取URL页面前15个字符，以便做可用性校验
    finally:
        if result == "<!DOCTYPE html>":
            print ip + "[OK]"
        else:
            print ip + "[error]"


if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for i in iplist:
            checkip(i)
    else:
        print "dns resolver error."


