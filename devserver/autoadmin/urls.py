#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.conf.urls import url
from autoadmin.views import *
urlpatterns = [
    url(r'index/$', index),
    url(r'server_list/$', server_list),
    url(r'module_list/$', module_list),
    url(r'module_add/$', module_add),
    url(r'module_add_post/$', module_add_post),
    url(r'module_info/$', module_info),
    url(r'module_run/$', module_run),
    url(r'server_fun_categ/$', server_fun_categ),
    url(r'server_app_categ/$', server_app_categ),
]

