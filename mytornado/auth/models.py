# _*_ coding:utf-8 _*_
import mongoengine as models
from auth import enums
import datetime


class User(models.Document):  # 用户模型(普通，管理员)
    card_id = models.StringField(max_length=20, required=False)  # 工号
    username = models.StringField(max_length=20, required=False)  # 用户名
    password = models.StringField(required=True)   # 登录密码
    age = models.IntField(required=False)  # 年龄
    sex = models.IntField(choices=enums.SEX_LIST, required=False)  # 性别
    department = models.StringField(max_length=30, required=False)  # 部门
    position = models.StringField(max_length=30, required=False)  # 职位
    mobile = models.StringField(required=False)  # 手机
    emergency_contact = models.StringField(required=False)  # 紧急联系人
    create_time = models.DateTimeField(default=datetime.datetime.now)  # 创建时间
    email = models.EmailField()  # email
    custom_attr = models.DictField()  # 用户其他信息
    perm = models.StringField(choices=enums.ADMIN_USER_PERMISSION_LIST, required=False)  # 权限
    # 1，False | 2，True default=enums.NORMAL


class Transaction(models.Document):  # 事物模型(请假，加薪等)
    user_id = models.StringField()  # 创建者
    ttype = models.StringField(choices=enums.TRANSACTION_TYPE_LIST)  # 事物类型
    create_time = models.DateTimeField(default=datetime.datetime.now)  # 创建时间
    title = models.StringField()  # 标题
    content = models.StringField()  # 内容

