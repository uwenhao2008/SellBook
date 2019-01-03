#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-09-28'
"""
# 由于初始化里就没有user。所以这里不需要的，直接删除这个文件  ！！！！！！！！！！
from . import web
@web.route('/login')
def login():
    headers = {
        'content-type': 'text/html;charset=utf-8',
    }
    return '<html><h1>HelloWorld！~~！！~！哈1哈2哈3</h1></html>', 200, headers
