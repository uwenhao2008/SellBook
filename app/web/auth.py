#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-10-31'
"""
from app.forms.auth import RegisterForm, LoginForm, ModifyPasswordForm, ResetPasswordForm
from app.models.base import db
from app.models.user import User
# from werkzeug.security import generate_password_hash
from . import web
from flask import render_template, request, redirect, url_for, make_response, flash


@web.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # 服务器端进行密码验证，两者一样才进入数据库，应该是前端做的事
        if request.form['password'] != request.form['password2']:
            flash('输入的密码不一致，请确认')
        else:
            user = User(nickname = request.form['nickname'],
                        email = request.form['email'],
                        _password = request.form['password']
            )
            user.set_attrs(form.data)
            # user.password = generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('web.login'))
    return render_template('auth/register.html',form=form)


@web.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):    # 为什么hash密码一样，确验证不通过？  因为数据库字段长度不够，截断了我的密码~~~~~~~~~
            print("登录成功XXX")
        else:
            flash('账户不存在或密码错误')
    return render_template('auth/login.html',form=form)


# cookie过期验证
@web.route('/set/cookie')
def set_cookie():
    response = make_response('Make response MR.7')
    response.set_cookie('name','MR.7',100)
    return response


@web.route('/forget_password_request', methods=['GET','POST'])
def forget_password_request():
    form = ModifyPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash("账户存在，请修改密码")
            # return redirect(url_for('change_password'))
            return render_template('auth/change_password.html')
        else:
            flash('账户不存在，请确认好')
    return render_template('auth/forget_password_request.html')


@web.route('/change_password/<email>', methods=['GET', 'POST'])
def change_password(email):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        print(email)
    return render_template('auth/forget_password.html')
