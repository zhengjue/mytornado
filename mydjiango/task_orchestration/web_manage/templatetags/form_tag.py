#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: form_tag.py
# Author: lza
# Created Time: 2016-08-23 15:03:31
############################

from django import template

register = template.Library()


@register.simple_tag
def error_message(arg):
    if arg:
        return arg[0][0]
    else:
        return ''

if __name__ == "__main__":
    pass

