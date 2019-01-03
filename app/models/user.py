#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-11-16'
"""
from app.models.base import Base
from sqlalchemy import String,Column,Integer,Boolean,Float
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24),nullable=False)
    phone_number = Column(String(18),unique=True)
    _password = Column('password',String(200))
    email = Column(String(50),unique=True,nullable=True)
    confirmed = Column(Boolean,default=False)
    beans = Column(Float,default=0)
    send_counter = Column(Integer,default=0)
    receive_counter = Column(Integer,default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

