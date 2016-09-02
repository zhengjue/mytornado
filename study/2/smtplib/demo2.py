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

msgtext = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
    <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
        <td colspan=2>*官网性能数据  <a href="monitor.domain.com">更多>></a></td>
    </tr>
    <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td><img src="cid:io"></td>
        <td><img src="cid:key_hit"></td>
    </tr>
    <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td> <img src="cid:men"></td>
        <td> <img src="cid:swap"></td>
    </tr>
</table>""", "html", "utf-8")

# <img>标签的src属性是通过Content-ID来引用的
msg.attach(msgtext)   # MIMEMultipart对象附加MIMEText的内容
msg.attach(addimg("img/bytes_io.png", "io"))    # 使用MIMEMultipart对象附加MIMEImage的内容
msg.attach(addimg("img/myisam_key_hit.png", "key_hit"))
msg.attach(addimg("img/os_mem.png", "men"))
msg.attach(addimg("img/os_swap.png", "swap"))

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

