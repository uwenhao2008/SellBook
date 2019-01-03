#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-11-16'
"""
from wtforms import Form,StringField,IntegerField,PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'),Length(6,32),])
    nickname = StringField(validators=[DataRequired(),Length(2,10,message='昵称最少需要2个字符，不能超过10个字符')])

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已被占用')

    def validate_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被占用')

class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'),Length(6,32),])

class ModifyPasswordForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='电子邮箱不符合规范')])
    # password = PasswordField(validators=[DataRequired(message='密码不能为空'),Length(6,32),])

class ResetPasswordForm(Form):
    password = PasswordField(validators=[DataRequired(message='密码不能为空'),Length(6,32),])
