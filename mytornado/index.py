# _*_ coding:utf-8 _*_
from base import BaseHandler
import tornado


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("index.html")

