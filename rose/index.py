# -*- coding: utf-8 -*-

import base


class IndexHandler(base.BaseHandler):
    def get(self):
        self.write('index')


class TestHandler(base.BaseHandler):
    def get(self):
        self.redirect('/')
        return
