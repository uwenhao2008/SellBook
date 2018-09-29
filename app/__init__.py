#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-09-20'
"""
from flask import Flask

def create_app():
    # 实例化
    app = Flask(__name__)
    print('id为' + str(id(app)) + '的路由注册')
    # 导入配置文件路径
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)    # 蓝图注册到app核心对象上
    return app   #这里之所以报错 return outside function 是因为我上面写的是class create_app  return返回的是def

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)