#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-11-29'
"""
class Person:
    def __init__(self, name):
        self.name = name

    @property #getter方法
    def name(self):
        return self._name

    @name.setter  #在setter方法中可以约束属性,非str将捕获一个type错误
    def name(self,name):
        if not isinstance(name, str):
            raise TypeError("Expected a string")
        self._name = name


p = Person('tom')
print(p.name)

p2 = Person('123')
print(p2.name)

p1 = Person(123)

