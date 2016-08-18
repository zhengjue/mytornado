from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    gender = models.BooleanField(default = False)
    age = models.IntegerField(default = 19)
    memo = models.TextField(default = 'xxxx')
    createDate = models.DateTimeField(default = '2016-08-09 16:20')
    type_id = models.ForeignKey("UserType")


class UserType(models.Model):
    name = models.CharField(max_length=50)


class Group(models.Model):
    name = models.CharField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    group_relation = models.ManyToManyField("Group")
