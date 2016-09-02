#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-09-01 13:54:34
############################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import myinfo

username = myinfo.username
password = myinfo.password
HOST = "smtp.sina.com"
SUBJECT = u"业务数据报表"
TO = "318724186@qq.com"
FROM = "loveziyou1234@sina.com"

# 添加图片函数


def addimg(src, imgid):   # 添加图片函数, 参数1:图片路径, 参数2:图片id
    with open(src, "rb") as fp:
        msgImgae = MIMEImage(fp.read())
    msgImgae.add_header('Content-ID',  imgid)    # 指定图片文件的Content-ID, <img>标签src用到)
    return msgImgae

msg = MIMEMultipart("related")   # 创建MIMEMultipart对象, 采用related定义内嵌资源的邮件体

msgtext = MIMEText(
    "<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>",
    "html", "utf-8")

# <img>标签的src属性是通过Content-ID来引用的
msg.attach(msgtext)   # MIMEMultipart对象附加MIMEText的内容
msg.attach(addimg("img/weekly.png", "weekly"))    # 使用MIMEMultipart对象附加MIMEImage的内容

# 创建一个MIMEText对象, 附加week_report.xlsx文档
attach = MIMEText(open("doc/week_report.xlsx",  "rb").read(),  "base64",  "utf-8")
attach["Content-Type"] = "application/octet-stream"   # 指定文件格式类型
# 指定Content-Disposition值为attachment则出现下载保存对话框, 保存的默认文件名使用filename指定
# 由于qqmail使用gb18030页面编码, 为保证中文文件名不出现乱码, 对文件名进行编码转换
attach["Content-Disposition"] = "attachment;filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)   # MIMEMultipart对象附加MIMEText附件内容
msg["Subject"] = SUBJECT
msg["From"] = FROM
msg["To"] = TO
try:
    server = smtplib.SMTP()
    server.connect(HOST, "25")
    server.starttls()  # 启动安全传输模式
    server.login(username, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "邮件发送成功!"
except Exception, e:
    print "邮件发送失败:"+str(e)
if __name__ == "__main__":
    pass

