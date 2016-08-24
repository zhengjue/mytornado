# _*_ coding:utf-8 _*_


from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ServerFunCateg(models.Model):
    server_categ_name = models.CharField(u'服务功能分类名称', max_length=20)

    def __unicode__(self):
        return self.server_categ_name


class ServerAppCateg(models.Model):
    server_categ_id = models.ForeignKey(ServerFunCateg)
    app_categ_name = models.CharField(u'服务应用分类名称', max_length=30)

    def __unicode__(self):
        return self.app_categ_name


class ServerList(models.Model):
    server_name = models.CharField(u'主机名称', max_length=13)
    server_wip = models.CharField(u'主机外网ip', max_length=15)
    server_lip = models.CharField(u'主机内网ip', max_length=12)
    server_op = models.CharField(u'主机操作系统', max_length=10)
    server_app_id = models.ForeignKey(ServerAppCateg)

    def __unicode__(self):
        return self.server_name


class ModuleList(models.Model):
    module_name = models.CharField(u'模块名称', max_length=20)
    module_caption = models.CharField(u'模块功能描述', max_length=255)
    module_extend = models.CharField(u'模块前端扩展', max_length=2000)

    def __unicode__(self):
        return self.module_name
