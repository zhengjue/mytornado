# _*_ coding:utf-8 _*_
import mongoengine as models
from admin import enums
import datetime


class Admin_User(models.Document):  # 用户模型(普通，管理员)
    username = models.StringField(max_length=20, required=False)  # 用户名
    password = models.StringField(required=True)   # 登录密码
    create_time = models.DateTimeField(default=datetime.datetime.now)  # 创建时间
    custom_attr = models.DictField()  # 用户其他信息

