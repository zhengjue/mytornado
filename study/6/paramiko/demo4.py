#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import paramiko
import os,sys,time


blhostname = '192.168.1.146'
blusername = 'root'
blpassword = "centos"

hostname = '192.168.1.147'
username = 'root'
password = "centos"

tmpdir = "/tmp"
remotedir="/tmp"
localpath="/tmp/boot.log.tar.gz"
tmppath=tmpdir+"/bl.boot.tar.gz"
remotepath=remotedir+"/boot.tar.gz"
port = 22
paramiko.util.log_to_file("syslogin.log")
passinfo = '\'s password: '

t = paramiko.Transport((blhostname,port))
t.connect(username=blusername, password=blpassword)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, tmppath)
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blhostname,username=blusername, password=blpassword)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
channel.send('scp '+tmppath+" "+username+'@'+hostname+':'+remotepath+'\n')
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception,e:
        print 'Error info:%s connection time.' %(str(e))
        channel.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:
        channel.send('yes\n')
        buff=''


channel.send(password+'\n')

buff =''
while not buff.endswith("# "):
    resp = channel.recv(9999)
    if not resp.find(passinfo)==-1:
        print 'Error info: Authrntication failed.'
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
print buff
channel.close()
ssh.close()
