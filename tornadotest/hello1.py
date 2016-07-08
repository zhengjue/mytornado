#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tornado.ioloop
import tornado.web
from tornado import httpclient


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #result=httpclient.AsyncHTTPClient("http://www.baidu.com").fetch()
        #print result
        #self.write(result)
        #self.write("Hello ,world!")
        self.write('<html><body><form action="/" method="post">'
                    '<input type="text" name="message">'
                    '<input type="submit" value="Submit">'
                    '</form></body></html>')
    def post(self):
        self.set_header("Content-Type","text/plain")
        self.write("you write " + self.get_argument("message"))


application = tornado.web.Application([
    (r"/",MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
