#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tornado.ioloop
import tornado.web
from tornado import httpclient
import os

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"templetes"),#for self.render("temple.html") find path
    static_path=os.path.join(os.path.dirname(__file__),"static"),#for static_url("js/xx.js") find path
    debug=True,
)
class MainHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return "hello python"

    def get_error_html(self,status_code):
        if status_code == "404":
            self.write("page  not found")

        if status_code == "500":
            self.write("interval server error")

    @tornado.web.asynchronous#开启长链接
    def get(self):
        http=tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://127.0.0.1:8000",callback=self.on_response)

    def on_response(self,response):
        self.write(response.body)
        self.finish()

        #name1="python"
        #name_list=['python','c++','java','c']
        ##self.render("main.html",name_list=name_list)
        #params=locals()
        #params.pop("self")
        #self.render("main.html",**params)

        #result=httpclient.AsyncHTTPClient("http://www.baidu.com").fetch()
        #print result
        #self.write(result)
        #self.write("Hello ,world!")
        #self.write('<html><body><form action="/" method="post">'
        #            '<input type="text" name="message">'
        #            '<input type="submit" value="Submit">'
        #            '</form></body></html>')

        #URL?story_id=100
        #xx = self.get_argument("story_id","1000")
        #story_id is null ,value is 1000
        #self.write(xx)

        #render_string="""
        #            <html><body>
        #            <form action="/"  method="post" enctype="multipart/form-data">
        #            <input type="file" name="upfile">
        #            <input type="submit" value="Submit">
        #            </form>
        #            </body></html>
        #            """
        #self.write(render_string)

    def post(self):
        #self.set_header("Content-Type","text/plain")
        #self.write("you write " + self.get_argument("message"))
        print "enter MainHandler post"
        #print self.request.files["upfile"] #name="file"
        print self.request.files
        #print self.request

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
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
