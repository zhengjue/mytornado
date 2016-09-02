#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-09-01 13:54:34
############################
import smtplib
import string
import myinfo

username = myinfo.username
password = myinfo.password
HOST = "smtp.sina.com"
SUBJECT = "smtplib test"
TO = "318724186@qq.com"
FROM = "loveziyou1234@sina.com"
text = "email test"
BODY = string.join(
    (
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
    ),
    "\r\n"
)

server = smtplib.SMTP()
server.connect(HOST, "25")
server.login(username, password)
server.sendmail(FROM, [TO], BODY)
server.quit()

if __name__ == "__main__":
    pass

