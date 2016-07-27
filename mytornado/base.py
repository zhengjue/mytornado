# _*_ coding:utf-8 _*_
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """
    当用户登陆每一个网页路径的时候，我们都需要为它判断，用户浏览器里面是否存在我们为它设定的cookie,
    如果存在就返回给后端服务器做判断，从而进行下一步跳转,因为每一个路径都需要在处理请求前作验证，所以
    把它作为一个基类给每个处理调用
    """

    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if user:
            return user


class AdminBaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("admin_user")
        if user:
            return user
