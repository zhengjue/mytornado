# _*_ coding:utf-8 _*_
from base import BaseHandler
from common.utils import md5, make_card_id
from auth import dao
import json


class RegisterHandler(BaseHandler):

    def get(self):
        err_msg = ""
        username = ""
        password = ""
        password1 = ""
        age = ""
        sex = ""
        mobile = ""
        emergency_contact = ""
        email = ""
        department = ""
        position = ""
        params = locals()
        params.pop("self")
        self.render("auth/register.html", **params)

    def post(self):
        card_id = self.get_argument("card_id", "")
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        password1 = self.get_argument("password1", "")
        age = self.get_argument("age", "")
        sex = int(self.get_argument("sex", 1))
        mobile = self.get_argument("mobile", "")
        emergency_contact = self.get_argument("emergency_contact", "")
        email = self.get_argument("email", "")
        department = self.get_argument("department", "")
        position = self.get_argument("position", "")

        if not (username and password and sex and age and department and position and mobile \
                and emergency_contact and email):
            err_msg = "lack of arguments"
            params = locals()
            params.pop("self")
            self.render("auth/register.html", **params)
            return

        if password != password1:
            err_msg = "two times input password no match"
            params = locals()
            params.pop("self")
            self.render("auth/register.html", **params)
            return

        user = dao.get_user(username=username)
        if user:
            err_msg = "user alreay exist"
            params = locals()
            params.pop("self")
            self.render("auth/register.html", **params)
            return

        dao.add_user(username, password, age, sex, department, position, mobile, emergency_contact, email)
        self.redirect("/login/")


class LoginHandler(BaseHandler):

    def get(self):
        user = self.get_current_user()
        err_msg = ""
        username = ""
        if not user:
            self.render("auth/login.html", err_msg=err_msg, username=username)  # 相对于templater_pat  # 相对于templater_pat
        else:
            self.redirect("/")

    def post(self):
        err_msg = ""
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")

        user = dao.get_user(username)
        if not user or user.password != md5(password):
            err_msg = "user do not match password"
            self.render("auth/login.html", err_msg=err_msg, username=username)  # 相对于templater_pat
            return

        self.set_secure_cookie("user", user.username)
        self.redirect("/")


class JsLoginHandler(BaseHandler):

    def get(self):
        user = self.get_current_user()
        err_msg = ""
        if not user:
            self.render("auth/jslogin.html", err_msg=err_msg)
        else:
            self.redirect("/")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        print username, password
        user = dao.get_user(username)
        if not user or user.password != md5(password):
            self.write(json.dumps({"status": "fail"}))
            return

        self.set_secure_cookie("user", "888")
        self.write(json.dumps({"status": "ok"}))

    def check_xsrf_cookie(self):
        return


class LogoutHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        pass
