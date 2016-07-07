#!/bin/env python
#_*_ coding:utf-8 _*_
import setting
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#myself define setting
user,passwd=setting.MyMail()
print user,passwd
sender_mail="loveziyou1234@sina.com"
#to_mail 可以是一个列表
to_mail="318724186@qq.com"
subject="python email test"

message=MIMEText("python test email","plain")
message["From"] = Header(sender_mail)#Header 里面可以是一些自定义字符串
message["To"] = Header(to_mail)
message["Subject"] = Header(subject)

s = smtplib.SMTP()
s.connect("smtp.sina.com",25)
s.login(user,passwd)
s.sendmail(sender_mail,to_mail,message.as_string())


