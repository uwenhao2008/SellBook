#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify,request

from app.forms.book import SearchForm
from helper import is_isbn_or_key
from shu_book import ShuBook

# 蓝图 替换到 __init__里注册了
# web = Blueprint('web',__name__)  # 参数：蓝图名称，所在的包

from . import web
# app = create_app()   ----------
print('id为'+str(id(web))+'的app路由实例化')

@web.route('/hello')  # @app-->@web
def hello():
    headers = {
        'content-type':'text/html',
    }
    return '<html><h1>HelloWorld！~~！！~！哈1哈2哈3</h1></html>',200,headers

# 视图函数
# @web.route('/book/search/<q>/<page>')
@web.route('/book/search')   # 采用http://127.0.0.1:5000/book/search?q=9787501524044&page=1 形式访问
def search():
    '''
    q: 普通搜索  isbn
    page:
    # isbn13 由13个0-9的数字组成
    # isbn10 10个0-9的数字，其中可能有 -
    :return:
    '''
    # q = request.args['q']
    # page = request.args['page']

    # 验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()  # 去除前后的空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        print(isbn_or_key)
        if isbn_or_key == 'isbn':
            return ShuBook.search_by_isbn(q)     # 得到的是json数据，因为已经把dict --> json
        else:
            return ShuBook.search_by_keyword(q)
    else:
        # return jsonify({'msg':'Wrong,Error!!!'})
        return jsonify(form.errors)
