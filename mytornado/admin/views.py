# _*_ coding:utf-8 _*_
from base import AdminBaseHandler
from common.utils import md5, make_card_id
from admin import dao
from auth import dao as auth_dao
from auth import enums as auth_enums
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

        admin_user = auth_dao.get_user(username)
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
        user_status_dict = auth_enums.USER_STATUS_DICT
        sex_dict = auth_enums.SEX_DICT
        params = locals()
        params.pop("self")
        self.render("admin/userlist.html", **params)


class AddUserHandler(AdminBaseHandler):

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
        perm_list = auth_enums.ADMIN_USER_PERMISSION_LIST
        params = locals()
        params.pop("self")
        self.render("admin/adduser.html", **params)

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
        perm = self.get_argument("perm", "")
        #  perm_list = auth_enums.ADMIN_USER_PERMISSION_LIST

        if not (username and password and sex and age and department and position and mobile
                and emergency_contact and email and perm):
            err_msg = "lack of arguments"
            params = locals()
            params.pop("self")
            self.render("admin/adduser.html", **params)
            return

        if password != password1:
            err_msg = "two times input password no match"
            params = locals()
            params.pop("self")
            self.render("admin/adduser.html", **params)
            return

        admin_user = auth_dao.get_user(username=username)
        if admin_user:
            err_msg = "user alreay exist"
            params = locals()
            params.pop("self")
            self.render("admin/adduser.html", **params)
            return

        auth_dao.add_user(username, password, age, sex, department, position, mobile, emergency_contact,
                          email, perm=perm)
        self.redirect("/admin/")


class CheckUserHandler(AdminBaseHandler):
    def post(self):
        check_user = self.get_argument("check_user", "")
        card_id = self.get_argument("card_id", "")
        print card_id
        if check_user == "pass":
            auth_dao.update_user_by_card_id(card_id, {'status': auth_enums.USER_STATUS_NORMAL})
            self.write(json.dumps({"status": "ok"}))
            return

        if check_user == "nopass":
            self.write(json.dumps({"status": "fail"}))
            return

    def check_xsrf_cookie(self):
        return
