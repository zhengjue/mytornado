#!/bin/env python
# _*_  coding:utf-8 _*_
import os
import logging

DEBUG = True

DB_ADDRESS = "127.0.0.1"
DB_NAME = "office"
DB_PORT = 27017

PORT = "8000"
SECRET_KEY = "MOlWqkvsfsBilrQQWdr/dttN16SX1cL+5KJXaOj9"

settings = dict(
    cookie_secret=SECRET_KEY,
    login_url="login/",
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    root_path=os.path.dirname(__file__),
    xsrf_cookies=True,
    autoescape="xhtml_escape",
    debug=DEBUG,
    xheaders=True,
)

LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO
