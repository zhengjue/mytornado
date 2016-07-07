#!/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="centos",db="mysql",charset="utf8")

cur = conn.cursor()
result = cur.execute("select * from user")
print cur.fetchmany(2)

cur.close()
conn.close()

