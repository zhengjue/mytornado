# _*_ coding:utf-8 _*_
from base import AdminBaseHandler
from common.utils import md5, make_card_id
from admin import dao
from auth import dao as auth_dao
import json


class LoginHandler(AdminBaseHandler):

    def get(self):
        admin_user = self.get_current_user()
        err_msg = ""
        username = ""
        if not admin_user:
            self.render("admin/login.html", err_msg=err_msg, username=username)  # 相对于templater_pat  # 相对于templater_pat
        else:
            self.redirect("/admin/")

    def post(self):
        err_msg = ""
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")

        admin_user = dao.get_admin_user(username)
        if not admin_user or admin_user.password != md5(password):
            err_msg = "user do not match password"
            self.render("admin/login.html", err_msg=err_msg, username=username)  # 相对于templater_pat
            return

        self.set_secure_cookie("admin_user", admin_user.username)
        self.redirect("/admin/")


class LogoutHandler(AdminBaseHandler):
    def get(self):
        pass

    def post(self):
        pass


class AdminHandler(AdminBaseHandler):
    def get(self):
        admin_user = self.get_secure_cookie("admin_user")
        if not admin_user:
            self.redirect("/admin/login/")
            return
        user_list = auth_dao.get_user_list()
        self.render("admin/userlist.html", user_list=user_list)

    def post(self):
        pass
