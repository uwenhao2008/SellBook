#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-11-16'
"""
from app.models.base import Base
from sqlalchemy import String,Column,Integer,Boolean,Float,ForeignKey
from sqlalchemy.orm import relationship

class Gift(Base):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False)
    launched = Column(Boolean,default=False)