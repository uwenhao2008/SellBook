#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-09-14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from flask import Flask
# from config import DEBUG   #导入配置文件的配置参数
# 实例化
app = Flask(__name__)
# 导入配置文件路径
app.config.from_object('config')

# 视图函数
@app.route('/hello')
def hello():
    headers = {
        'content-type':'text/plane',
        'location':'http://www.bing.com'   # 这里没有http前缀的话，bing就不会被当作域名的一部分，出现 127.0.0.1:5000/www.bing.com这种情况
    }
    return '<html><h1>Hello World</h1></html>',8788,headers   # 301是页面重定向，此处只是作为状态码显示而已

# 另外一种路由注册的方式
# app.add_url_rule('/hello',view_func=hello)

if __name__ == '__main__':
    app.run(debug = app.config['DEBUG'])