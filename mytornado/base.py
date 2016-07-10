# _*_ coding:utf-8 _*_
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_cookie("user")
        if user:
            return "user"
