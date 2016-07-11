# _*_ coding:utf-8 _*_
from base import BaseHandler
from auth.models import User
from common.utils import md5
from auth import dao


class RegisterHandler(BaseHandler):
    def get(self):
        self.render("auth/register.html")

    def post(self):
        self.write("hello")
        card_id=self.get_argument("card_id", "")
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        password1 = self.get_argument("password1", "")
        age = self.get_argument("age", "")
        sex = int(self.get_argument("sex", 0))
        mobile = self.get_argument("mobile", "")
        emergency_contact = self.get_argument("emergency_contact", "")
        email = self.get_argument("email", "")
        department = self.get_argument("department", "")
        position = self.get_argument("position", "")
        # print card_id,username,password,age,sex,mobile,emergency_contact,email,position,department
        if password != password1:
            self.write("two times input password no match")
            return

        user = dao.get_user(username=username)
        if user:
            self.write("user alreay exist")
            return

        dao.add_user(card_id, username, password, age, sex, department, position, mobile, emergency_contact, email)
        self.redirect("/login/")


class LoginHandler(BaseHandler):
    def get(self):
        self.render("auth/login.html")  # 相对于templater_pat

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")

        user = dao.get_user(username)
        if not user:
            self.write("user is not exist")
            self.render("auth/login.html")  # 相对于templater_pat
            return

        if user.password != md5(password):
            self.write("passwd is incorrect")
            self.render("auth/login.html")  # 相对于templater_pat
            return

        self.set_cookie("user", user.username)
        self.redirect("/")


class LogoutHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        pass
