# _*_ coding:utf-8 _*_
from base import BaseHandler
import tornado


class IndexHandler(BaseHandler):
    # 在需要验证用户的地方，首先判断用户是否已经登陆，如果不是就跳回登陆网页处理
    @tornado.web.authenticated
    def get(self):
        self.render("index.html")

