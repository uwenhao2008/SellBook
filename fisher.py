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
from flask import Flask,jsonify
from shu_book import ShuBook
from helper import is_isbn_or_key
# from config import DEBUG   #导入配置文件的配置参数
# 实例化
app = Flask(__name__)
# 导入配置文件路径
app.config.from_object('config')

# 视图函数
@app.route('/book/search/<q>/<page>')
def search(q,page):
    '''
    q: 普通搜索  isbn
    page:
    # isbn13 由13个0-9的数字组成
    # isbn10 10个0-9的数字，其中可能有 -
    :return:
    '''
    isbn_or_key = is_isbn_or_key(q)
    print(isbn_or_key)
    # if isbn_or_key == 'isbn':
    #     return ShuBook.search_by_isbn(q)
    # else:
    #     return ShuBook.search_by_keyword(q)
    # return jsonify(result)





if __name__ == '__main__':
    app.run(debug = app.config['DEBUG'])