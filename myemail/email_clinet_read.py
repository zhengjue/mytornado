#!/bin/env python
#_*_ coding:utf-8 _*_
import setting
import poplib
import chardet

user,passwd=setting.MyMail()

p=poplib.POP3("pop.sina.com",110)
p.user(user)
p.pass_(passwd)

nun_of_message = len(p.list()[1])
print nun_of_message #邮件数目

for i in range(nun_of_message):
    mail = p.retr(i+1)[1]#获取邮件，计数从1开始，不是0
    for m in mail:
        if u"尊敬的 loveziyou1234".encode("utf-8") in m:
            print m
