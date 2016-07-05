#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tornado.ioloop
import tornado.web
from tornado.web import url
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello ,world!")
        self.write('<a href="%s">link to story 1</a>' % self.reverse_url("story","1"))


class StoryHandler(tornado.web.RequestHandler):
    def initalize(self,db):
        self.db=db

    def get(self,story_id):
        self.write("this is story %s" % story_id)

application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/story/([0-9]+)",StoryHandler,dict(db="db"),name="story")
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
