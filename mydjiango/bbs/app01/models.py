#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: models.py
# Author: lza
# Created Time: 2016-08-16 14:47:21
############################

from __future__ import unicode_literals

from django.db import models


class UserType(models.Model):
    display = models.CharField(max_length=50)

    def __unicode__(self):
        return self.display


class Admin(models.Model):  # 用户表
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    user_type = models.ForeignKey("UserType")

    def __unicode__(self):
        return self.username


class Chat(models.Model):
    content = models.TextField()
    user = models.ForeignKey("Admin")
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content


class NewsType(models.Model):  # 用户表
    display = models.CharField(max_length=50)

    def __unicode__(self):
        return self.display


class News(models.Model):  # 用户表
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=256)
    url = models.URLField()
    favor_count = models.IntegerField(default=0)  # 点赞
    reply_count = models.IntegerField(default=0)  # 评论
    news_type = models.ForeignKey("NewsType")  # 新闻类型
    user = models.ForeignKey("Admin")  # 发布人
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Reply(models.Model):
    content = models.TextField()  # 回复内容
    user = models.ForeignKey("Admin")  # 回复者
    new = models.ForeignKey("News")  # 回复的那个新闻
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

