#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-10-10'
"""
class A(object):
    def foo1(self):
        print("func is func")

    @staticmethod
    def foo2():
        print("static_func is static_func")

    @classmethod
    def foo3(cls):
        print("func_cls is func_cls"),cls

a = A()
a.foo1()  # func is func

A.foo1(a) # func is func
A.foo2() # static_func is static_func
A.foo3() # func_cls is func_cls