#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-09-30'
"""
from flask import Flask, current_app

app = Flask(__name__)

# 2 ####
# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']

#  1 ######
ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']
ctx.pop()