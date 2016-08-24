from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserType(models.Model):
    caption = models.CharField(max_length=32)

    def __uncode__(self):
        return self.caption


class UserProfile(models.Model):
    user_type = models.ForeignKey(UserType)
    name = models.CharField(u'名字', max_length=30)
    email = models.EmailField(u'邮件')
    phone = models.CharField(u'座机', max_length=20)
    mobile = models.CharField(u'手机', max_length=20)

    memo = models.TextField(u'备注', blank=True)
    create_at = models.DateTimeField(blank=True)
    update_at = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

    def __uncode__(self):
        return self.name


class AdminInfo(models.Model):
    user_info = models.OneToOneField(UserProfile)
    username = models.CharField(u'用户名', max_length=50)
    password = models.CharField(u'密码', max_length=50)


class UserGroup(models.Model):
    caption = models.CharField('用户组', max_length=32)
    users = models.ManyToManyField(UserProfile)


class HsotStatus(models.Model):
    name = models.CharField(max_length=64)
    memo = models.TextField(u'备注', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Host(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    ip = models.IPAddressField(unique=True)
    status = models.ForeignKey(HsotStatus)

    def __unicode__(self):
        return self.hostname


class TaskTemplate(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    content = models.TextField()

    def __unicode__(self):
        return self.name


class TaskType(models.Model):
    caption = models.CharField(u'任务类型', max_length=256)
    code = models.CharField(max_length=256)

    def __unicode__(self):
        return self.caption


class ExcuteType(models.Model):
    caption = models.CharField(u'执行方法', max_length=256)
    code = models.CharField(max_length=256)

    def __unicode__(self):
        return self.caption


class Task(models.Model):
    task_type = models.ForeignKey(TaskType)
    excute_type = models.ForeignKey(ExcuteType)
    name = models.CharField(u'任务名称', max_length=128)
    content = models.TextField(u'任务内容')
    kick_off_at = models.DateTimeField(u'执行时间', blank=True)
    is_template = models.BooleanField(u'存为任务模板')
    description = models.TextField(u'描述', blank=True)
    create_by = models.ForeignKey(UserProfile)
    hosts = models.ManyToManyField(Host)
    status = models.IntegerField(u'任务状态')

    def __unicode__(self):
        return self.name


class TaskHostStatus(models.Model):
    status = models.IntegerField()
    log = models.TextField(null=True, blank=True)

    task = models.ForeignKey(Task)
    host = models.ForeignKey(Host)

    def __unicode__(self):
        return self.status


class TaskLog(models.Model):
    task = models.ForeignKey(Task)
    result_choices = (
        ('success', u'成功'),
        ('failed', u'失败'),
        ('unknown', u'未知'))

    log = models.TextField(u'任务日志')
    host_id = models.IntegerField(u'回报主机id')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.task.name
