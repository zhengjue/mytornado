#!/bin/env python
# _*_ coding:utf-8 _*_
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
import time

env.user = "root"
env.hosts=['192.168.1.146','192.168.1.147']
#  env.password="centos"
env.passwords = {
    'root@192.168.1.146:22': "centos",
    'root@192.168.1.147:22': "centos",
}


env.project_dev_source = '/tmp/dev/web/'  # 开发机主机目录
env.project_tar_source = '/tmp/dev/releases/' # 开发机项目压缩目录
env.project_pack_name = "relaese" # 项目压缩包前缀 文件名为 release.tar.gz

env.deploy_project_root = "/tmp/dev/web/" #生产环境主目录
env.deploy_release_dir = "releases" # 项目发表目录位于主目录下
env.deploy_current_dir = "current" # 对外服务的当前版本软连接
env.deploy_version=time.strftime("%y%m%d")+"v2" # 版本号

def get_dir_list():
    env.deploy_base_path=env.deploy_project_root+env.deploy_release_dir
    print "##############dir list################"
    run("ls %s" % env.deploy_base_path)


@runs_once
def input_versionid(): # 获得用户输入的版本号，以便做版本回滚操作
    get_dir_list()
    return prompt("please input project rollback version ID:", default="")

@task
@runs_once
def tar_source(): # 打包本地项目主目录，并压缩到本地压缩目录
    print yellow("Createing source package...")
    with lcd(env.project_dev_source):
        local("tar -zcf %s.tar.gz ." %(env.project_tar_source+env.project_pack_name))
    print green("Create source package success!")

@task
def put_package(): # 上传任务
    print yellow("Start put package...")
    with settings(warn_only=True):
        with cd(env.deploy_project_root+env.deploy_release_dir):
            run("mkdir %s" %(env.deploy_version)) # 创建版本目录
    env.deploy_full_path=env.deploy_project_root+env.deploy_release_dir+"/"+env.deploy_version
    #  生产环境下版本目录 /tmp/dev/web/releases/20161202/

    with settings(warn_only=True): # 上传项目压缩包至此目录
        result = put(env.project_tar_source + env.project_pack_name + ".tar.gz", env.deploy_full_path)
        # put("/tmp/dev/releases/release.tar.gz", /tmp/dev/web/releases/20161202/)
    if result.failed and not confirm("put file failed , Continue[Y/N]?"):
        abort("Aborting file put task!")

    with cd(env.deploy_full_path): # 成功解压后删除压缩包
        run("tar -zxvf %s.tar.gz" % (env.project_pack_name))
        run("rm -rf %s.tar.gz" % (env.project_pack_name))

    print green("Put & untar package success!")


@task
def make_symlink(): # 为当前旧版本做软连接
    print yellow("update current symlink ")
    env.deploy_full_path=env.deploy_project_root+env.deploy_release_dir+"/"+env.deploy_version
    #  生产环境下版本目录 /tmp/dev/web/releases/20161202/
    with settings(warn_only=True): # 删除软连接，重新创建并制定软连接源目录，新版本才能生效
        run("rm -rf %s" %(env.deploy_project_root + env.deploy_current_dir))
        run("ln -s %s %s" %(env.deploy_full_path,env.deploy_project_root + env.deploy_current_dir))
    print green("make symlink success!")


@task
def rollback(): # 版本回滚任务函数
    print yellow("rollback project version")
    versionid=input_versionid() #获得用户输入回滚版本号

    if versionid=="":
        abort("Project version ID error,abort! ")

    env.deploy_full_path=env.deploy_project_root+env.deploy_release_dir+"/"+versionid
    if run("test -d %s" % env.deploy_full_path).failed:
        abort("dir is error")


    run("rm -f %s" % env.deploy_project_root+env.deploy_current_dir)
    run("ln -s %s %s" %(env.deploy_full_path, env.deploy_project_root+env.deploy_current_dir))
    print green("rollback success!")

@task
def go(): # 自动化程序版本发布入口函数
    tar_source()
    put_package()
    make_symlink()



