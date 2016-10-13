# -*- coding: UTF-8 -*-
#迁移时，能使python2的语法运用在python3上
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Node(models.Model):

    #线路的类型选择，作为node_type的选项
    type = (
        (U'总部','总部'),
        (U'分部','分部'),
    )
    #verbose_name可以让admin后台显示自定义的中文名字，而非字段
    node_name = models.CharField(verbose_name='节点名称',max_length=255)
    #choices找到type元组，并调用相关内容
    node_type = models.CharField(verbose_name='节点类型',max_length=50,choices=type)
    node_address = models.CharField(verbose_name='节点地址',max_length=255)
    #blank为空，代表在form中可以允许不填
    node_contact = models.CharField(verbose_name='节点联系人',max_length=255,blank=True)
    #default表示默认值
    node_signer = models.CharField(verbose_name='登记人',max_length=50, default='system')
    node_remarks = models.CharField(verbose_name='备注',max_length=255,blank=True)
    #登记时间设置为自动记录，不会出现在选项中
    node_signtime = models.DateField(auto_now_add= True)

    #返回相应的值
    def __unicode__(self):
        return self.node_name


#建立线路信息表
class Line(models.Model):

    #与node形成一对多的关系，在删除node的同时，如果有线路信息依附在该节点上，那么删除失败
    node = models.ForeignKey(Node,on_delete=models.PROTECT)

    #运营商分类
    spname = (
        (u'中国电信','中国电信'),
        (u'中国联通','中国联通'),
        (u'中国移动','中国移动'),
        (u'中国铁通','中国铁通'),
        (u'其他','其他')
    )
    #线路速率
    speed = (
        ('2M','2M'),
        ('4M','4M'),
        ('6M','6M'),
        ('10M','10M'),
        (u'其他','其他'),
    )
    #线路类型
    type = (
        ('MSTP','MSTP'),
        ('MSAP','MASP'),
        ('SDH','SDH'),
        ('DIAL','DIAL'),
        (u'其他','其他'),
    )

    line_code = models.CharField(verbose_name='线路编号',max_length=100)
    line_local = models.CharField(verbose_name='所在机房',max_length=50,default='上海数据中心')
    line_speed = models.CharField(verbose_name='线路速率',max_length=10,choices=speed,default='6M')
    line_spname = models.CharField(verbose_name='运营商',max_length=10,choices=spname,default='信网公司')
    line_type = models.CharField(verbose_name='线路类型',max_length=50,choices=type,default='MSTP')
    line_status = models.BooleanField(verbose_name='线路启用',default=True)
    line_open = models.DateField(verbose_name='开通时间')
    line_closed = models.DateField(verbose_name='关闭时间',blank=True,null=True)
    line_signer = models.CharField(verbose_name='登记人',max_length=30,default='system')
    line_signtime = models.DateField(auto_now_add=True)
    line_remarks = models.CharField(verbose_name='备注',max_length=255,blank=True)

    def __unicode__(self):
        return self.line_code

#建立设备信息表
class Device(models.Model):

    node = models.ForeignKey(Node, on_delete=models.PROTECT)

    vendor = (
        ('CISCO', 'CISCO'),
        ('JUNIPER','JUNIPER'),
        ('TOPSEC','TOPSEC'),
        ('HUAWEI','HUAWEI'),
        ('H3C','H3C'),
    )

    device_caption = models.CharField(verbose_name='设备名称',max_length=100)
    device_serial = models.CharField(verbose_name='设备序列号',max_length=100)
    device_type = models.CharField(verbose_name='设备型号',max_length=50)
    device_vendor = models.CharField(verbose_name='设备厂商',max_length=50,choices=vendor)
    device_remark = models.CharField(verbose_name='备注',max_length=50,blank=True)
    device_ip = models.GenericIPAddressField(verbose_name='管理IP')
    device_status = models.CharField(verbose_name='设备状态',max_length=10,default='启用')
    device_signer = models.CharField(verbose_name='登记人',max_length=30,default='system')
    device_signtime = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.device_caption
