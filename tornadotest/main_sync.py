#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tornado.ioloop
import tornado.web
from tornado import httpclient
import os
import time

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"templetes"),#for self.render("temple.html") find path
    static_path=os.path.join(os.path.dirname(__file__),"static"),#for static_url("js/xx.js") find path
    debug=True,
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
)
class MainHandler(tornado.web.RequestHandler):
    #def get(self):
    #    time.sleep(3)
    #    self.write("after 3 second ")
    def get(self):
        name=self.get_secure_cookie("name")
        if name == "zhangsan":
            self.write("you name is zhangsan")
        else:
            self.set_secure_cookie("name","zhangsan")
            self.set_secure_cookie("age","19")
            self.write("you first access")

class StoryHandler(tornado.web.RequestHandler):
    def initializew(self):
        print "initializew"

    def prepare(self):
        print "prepare"

    def get(self,story_id):
        print self.request.arguments
        print self.request.path
        print self.request.headers
        self.write("you requested the story" + story_id)
        self.redirect("/")


class RedirectHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("you have already redirect")




application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/story/([0-9]+)/?",StoryHandler),
    (r"/aaa/bbb/?",RedirectHandler),
    (r"/redirect/",tornado.web.RedirectHandler,dict(url="/aaa/bbb/")),
],**setting)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
