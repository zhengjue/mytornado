# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class ServerFunCateg(models.Model):
    id = models.IntegerField(verbose_name="服务功能分类ID", primary_key=True, db_column='ID')
    server_categ_name = models.CharField(verbose_name=u'服务功能分类名称', max_length=90)
    def __unicode__(self):
        return self.server_categ_name
    class Meta:
        db_table = u'server_fun_categ'
        verbose_name=u'服务功能'


class ServerAppCateg(models.Model):
    id = models.IntegerField(verbose_name="服务应用分类ID",primary_key=True, db_column='ID')
    server_categ_id = models.ForeignKey(ServerFunCateg,verbose_name="服务功能列表", db_column="server_categ_id")
    app_categ_name = models.CharField(verbose_name=u'服务应用分类名称', max_length=60)
    def __unicode__(self):
        return self.app_categ_name
    class Meta:
        db_table = u'server_app_categ'
        verbose_name=u'系统集成'


class ServerList(models.Model):
    server_name = models.CharField(verbose_name=u'主机名称', max_length=39,primary_key=True)
    server_wip = models.GenericIPAddressField(verbose_name=u'主机外网ip')
    server_lip = models.GenericIPAddressField(verbose_name=u'主机内网ip', unique=True)
    server_op = models.CharField(verbose_name=u'主机操作系统', max_length=30)
    server_app_id = models.ForeignKey(ServerAppCateg, verbose_name="服务应用列表",db_column="server_app_id")
    def __unicode__(self):
        return self.server_name
    class Meta:
        db_table = u'server_list'
        verbose_name=u'服务主机'


class ModuleList(models.Model):
    id = models.IntegerField(verbose_name="模块ID",primary_key=True, db_column='ID')
    module_name = models.CharField(verbose_name=u'模块名称', max_length=60)
    module_caption = models.CharField(verbose_name=u'模块功能描述', max_length=765)
    module_extend = models.CharField(verbose_name=u'模块前端扩展', max_length=6000)
    def __unicode__(self):
        return self.module_name
    class Meta:
        db_table = u'module_list'
        verbose_name=u'功能模块'
