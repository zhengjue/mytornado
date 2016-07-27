# _*_ coding:utf-8 _*_
from auth.models import User
from common.utils import md5, make_card_id


def add_user(username, password, age, sex, department, position, mobile, emergency_contact, email):
    user = User(
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


def get_user(username):
    try:
        user = User.objects.get(username=username)
    except:
        user = None
    return user


def get_user_list():
    try:
        user_list = User.objects.all()
    except:
        user_list = None
    return user_list
