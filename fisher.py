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
from app import create_app
# from shu_book import ShuBook
# from helper import is_isbn_or_key
# from config import DEBUG,JSON_AS_ASCII   #导入配置文件的配置参数

app = create_app()
from app.web import book   # 强行导入book.py  此时仍然成功注册了路由，但是依然是404

if __name__ == '__main__':
    print('id为' + str(id(app)) + '启动')
    app.config['JSON_AS_ASCII'] = False
    app.run(debug = app.config['DEBUG'])
else:
    print('fisher不是作为__main__文件执行的')