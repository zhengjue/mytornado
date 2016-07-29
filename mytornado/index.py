# _*_ coding:utf-8 _*_
from base import BaseHandler
from auth import enums as auth_enums
from auth import dao as auth_dao
import tornado


class IndexHandler(BaseHandler):
    # 在需要验证用户的地方，首先判断用户是否已经登陆，如果不是就跳回登陆网页处理
    @tornado.web.authenticated
    def get(self):
        login_user = self.get_current_user()
        user = auth_dao.get_user(login_user)
        if user.status != auth_enums.USER_STATUS_NORMAL:
            self.write("<h1>you account is checking!!!!</h1>")
            return

        perm = ""
        if user.perm == auth_enums.ACADEMY:
            perm = auth_enums.ACADEMY
        if user.perm == auth_enums.BUSINESS:
            perm = auth_enums.BUSINESS
        if user.perm == auth_enums.CLUSTER:
            perm = auth_enums.CLUSTER

        self.render("index.html", perm=perm)

