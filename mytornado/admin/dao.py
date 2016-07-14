# _*_ coding:utf-8 _*_
from admin.models import Admin_User
from common.utils import md5, make_card_id


def add_user(username, password, age, sex, department, position, mobile, emergency_contact, email):
    user = Admin_User(
        card_id=str(make_card_id()),
        username=username,
        password=md5(password),
        age=age,
        sex=sex,
        department=department,
        position=position,
        mobile=mobile,
        emergency_contact=emergency_contact,
        email=email
    )
    user.save()


# 返回含有查询用户名的那条记录
def get_admin_user(username):
    try:
        user = Admin_User.objects.get(username=username)
    except:
        user = None
    return user

