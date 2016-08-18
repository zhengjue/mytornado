#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: wapp_test.py
# Author: lza
# Created Time: 2016-08-16 13:23:08
############################


# 没有参数的装饰器

def fun1(main_fun):
    def _wrapper(*args, **kwargs):
        return main_fun(*args, **kwargs)

    return _wrapper


def Filter(before_fun, after_fun):
    def Fun(main_fun):
        def _wrapper(*args, **kwargs):

            before_result = before_fun(*args, **kwargs)
            if(before_result is not None):
                return before_result

            main_result = main_fun(*args, **kwargs)
            if(main_result is not None):
                return main_result

            after_result = after_fun(*args, **kwargs)
            if(after_result is not None):
                return after_result
        return _wrapper
    return Fun


if __name__ == "__main__":
    pass

