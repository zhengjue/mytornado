#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: wsgiref_server_urls_template_jinja2.py
# Author: lza
# Created Time: 2016-08-08 15:26:54
############################


from wsgiref.simple_server import make_server
from jinja2 import Template


def index():
    # return 'index'

    # template = Template('Hello {{ name }}!')
    # result = template.render(name='John Doe')

    f = open('index.html')
    result = f.read()
    template = Template(result)
    data = template.render(name='John Doe', user_list=['alex', 'eric'])
    return data.encode('utf-8')


def login():
    # return 'login'
    f = open('login.html')
    data = f.read()
    return data


def routers():

    urlpatterns = (
        ('/index/', index),
        ('/login/', login),
    )

    return urlpatterns


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func()
    else:
        return '404 not found'


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()
if __name__ == "__main__":
    pass

