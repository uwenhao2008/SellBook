#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-11-28'
"""
# 测试 class  @func.setter用法
class func(object):

    def __init__(self, id, key):
        self.id = id
        self.key = key

    @property
    def summary(self):
        print(self.s+1)

    @summary.setter
    def summary(self, value):
        if not isinstance(value,int):
            raise TypeError("请输入数字")
        self.s = value

a = func(1,2)
print(a.id)
print(a.key)

b = func(3,4)
b.summary = 30
b.summary
b.summary = '30'
b.summary

c = func(5,6)
# 貌似func的setter只能通过 等号 赋值，不能把变量写在括号里当参数赋值
c.summary(44)
c.summary







