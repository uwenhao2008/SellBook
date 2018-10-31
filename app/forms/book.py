#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-09-29'
"""

from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange

class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30,message='+++q不在指定范围+++')])
    page = IntegerField(validators=[NumberRange(min=1, max=99,message='考虑一下，page是否错误？')], default=1)
