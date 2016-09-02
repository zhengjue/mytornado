#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: demo.py
# Author: lza
# Created Time: 2016-09-01 13:54:34
############################
import smtplib
from email.mime.text import MIMEText
import string
import myinfo

username = myinfo.username
password = myinfo.password
HOST = "smtp.sina.com"
SUBJECT = u"数据报表"
TO = "318724186@qq.com"
FROM = "loveziyou1234@sina.com"
msg = MIMEText("""
<table width="800" border="0" cellspacing="0" cellpadding="4">
    <tr>
        <td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网数据  <a href="monitor.domain.com">更多>></a></td>
    </tr>
    <tr>
         <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
            1)日访问量:<font color=red>152433</font>  访问次数:23651 页面浏览量:45123 点击数:545122  数据流量:504Mb<br>
            2)状态码信息<br>
               ; ;500:105  404:3264  503:214<br>
            3)访客浏览器信息<br>
               ; ;IE:50%  firefox:10% chrome:30% other:10%<br>
            4)页面信息<br>
               ; ;/index.php 42153<br>
               ; ;/view.php 21451<br>
               ; ;/login.php 5112<br>
        </td>
    </tr>
</table>""", "html", "utf-8")
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

