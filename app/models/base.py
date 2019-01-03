#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-11-16'
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,SmallInteger
db = SQLAlchemy()

# 软删除 用于子类继承
class Base(db.Model):
    __abstract__ = True    # Base没有主键，只是作为基类存在 若是没有主键就不能创建
    create_time = Column('create_time',Integer)
    status = Column(SmallInteger,default=1)

    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                # 跟踪下 password
                setattr(self,key,value)