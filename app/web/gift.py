#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-10-31'
"""
from . import web

@web.route('/my/gifts')
def my_gifts():
    return 'My_gifts'

@web.route('/gifts/book/<isbn>')
def save_to_gifts():
    pass

@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts():
    pass