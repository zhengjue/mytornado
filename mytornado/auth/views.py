# _*_ coding:utf-8 _*_
import tornado.web
from base import BaseHandler
from common.utils import md5
from auth import dao
from auth import enums
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

        if not (username and password and sex and age and department and position and mobile
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

        if user.status == enums.USER_STATUS_CHECK:
            self.write("<h1>your acount is checking!!</h1>")
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


class InfoHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login_user = self.get_current_user()
        user = dao.get_user(login_user)
        sex_dict = enums.SEX_DICT
        params = locals()
        params.pop("self")

        self.render("auth/user_info.html", **params)

    @tornado.web.authenticated
    def post(self):
        login_user = self.get_current_user()
        user = dao.get_user(login_user)
        mobile = self.get_argument("mobile", "")
        emergency_contact = self.get_argument("emergency_contact", "")

        dao.update_user_by_card_id(user.card_id, {"mobile": mobile, "emergency_contact": emergency_contact})
        self.redirect("/member/")


class TransactionHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, action):
        if action == "list":
            login_user = self.get_current_user()
            user_id = dao.get_user(login_user).oid
            transaction_list = dao.get_transaction_list_by_user_id(user_id)
            transaction_type_dict = enums.TRANSACTION_TYPE_DICT
            transaction_status_dict = enums.PROGRESS_DICT
            params = locals()
            params.pop("self")
            self.render("auth/transaction.html", **params)
        elif action == "add":
            self.render("auth/add_transaction.html")

    @tornado.web.authenticated
    def post(self, action):
        if action == "update":
            transaction_id = self.get_argument("transaction_id", "")
            title = self.get_argument("title", "")
            content = self.get_argument("content", "")
            status = enums.PROGRESS_CREATE
            attr = {"title": title, "content": content, "status": status}
            dao.update_transaction_by_id(transaction_id, attr)
            self.write({"status": "ok"})
        else:
            login_user = self.get_current_user()
            user_id = dao.get_user(login_user).oid
            ttype = int(self.get_argument("ttype"))
            title = self.get_argument("title")
            content = self.get_argument("content")
            dao.add_transaction(user_id, ttype, title, content)
            self.redirect("/transaction/list/")

    def check_xsrf_cookie(self):
        return


class ReviewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login_user = self.get_current_user()
        user = dao.get_user(login_user)
        transaction_type_dict = enums.TRANSACTION_TYPE_DICT

        if user.perm == enums.ACADEMY:
            status = 1
        if user.perm == enums.BUSINESS:
            status = 2
        if user.perm == enums.CLUSTER:
            status = 3

        transaction_list = dao.get_transaction_list_by_user_status(status)
        result = []
        for transaction in transaction_list:
            tmp = {}
            user = dao.get_user_by_user_id(transaction.user_id)
            tmp['id'] = str(transaction.id)
            tmp["user"] = user.username
            tmp["ttype"] = transaction.ttype
            tmp["title"] = transaction.title
            tmp["content"] = transaction.content
            result.append(tmp)

        transaction_list = result
        params = locals()
        params.pop("self")
        self.render("auth/review_list.html", **params)

    def check_xsrf_cookie(self):
        return

    def post(self):
        transaction_id = self.get_argument("transaction_id", "")
        action = self.get_argument("action", "")
        reason = self.get_argument("reason", "")

        if action == "pass":
            dao.update_transaction_by_id(transaction_id, {"status": 1})
        if action == "nopass":
            dao.update_transaction_by_id(transaction_id, {"status": 0, "reason": reason})
        self.write({"status": "ok"})

