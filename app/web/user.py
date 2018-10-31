#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-09-28'
"""
from . import web
@web.route('/login')
def login():
    headers = {
        'content-type': 'text/html;charset=utf-8',
    }
    return '<html><h1>HelloWorld！~~！！~！哈1哈2哈3</h1></html>', 200, headers