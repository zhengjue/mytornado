#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: ip_test.py
# Author: lza
# Created Time: 2016-08-30 16:16:30
############################
from IPy import IP

ip_s = raw_input('Please enter an IP address or range: ')
try:
    ips = IP(ip_s)
except ValueError:
    print('Could not understand your input %s. Exiting.' % ip_s)
    from sys import exit
    exit(1)

print('I understood: %s' % ips)
print('This is an IPv%d address.' % ips.version())

if len (ips) > 1:    #为一个网络地址
    print ('net: %s' % ips.net ())    #输出网络地址
    print ('netmask: %s' % ips.netmask ())    #输出网络掩码地址
    print ('broadcast: %s' % ips.broadcast ())    #输出网络广播地址
    print ('reverse address: %s' % ips.reverseNames ()[0])    #输出地址反向解析
    print ('subnet: %s' % len (ips))    #输出网络子网数
else:    #为单个IP地址
    print ('reverse address: %s' % ips.reverseNames ()[0])    #输出IP反向解析
print ('hexadecimal: %s' % ips.strHex ())    #输出十六进制地址
print ('binary ip: %s' % ips.strBin ())    #输出二进制地址
print ('iptype: %s' % ips.iptype ())    #输出地址类型，如PRIVATE、PUBLIC、LOOPBACK等

if __name__ == "__main__":
    pass

