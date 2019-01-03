#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = False   # 断点调试的时候，改为False
JSON_AS_ASCII = False

# mysql配置
USERNAME = 'root'
PASSWORD = 'wen4632022'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'yushu'
DB_URI = 'mysql+cymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:wen4632022@localhost:3306/yushu'
SECRET_KEY='wen4632022'
