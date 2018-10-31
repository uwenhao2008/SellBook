#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import jsonify,request,render_template,flash

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.shu_book import ShuBook

# 蓝图 替换到 __init__里注册了
# web = Blueprint('web',__name__)  # 参数：蓝图名称，所在的包
from app.view_models.book import BookViewModel, BookCollection

from . import web
# app = create_app()   ----------
print('id为'+str(id(web))+'的app路由实例化')

@web.route('/hello')  # @app-->@web
def hello():
    headers = {
        'content-type':'text/html;charset=utf-8',
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
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()  # 去除前后的空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        shubook = ShuBook()
        print(isbn_or_key)
        if isbn_or_key == 'isbn':
            shubook.search_by_isbn(q)
            # result = ShuBook.search_by_isbn(q).json     # 得到的是json数据，因为已经把dict --> json
            # result = BookViewModel.package_single(result, q)
        else:
            shubook.search_by_keyword(q, page)
            # result = ShuBook.search_by_keyword(q).json
            # result = BookViewModel.package_collection(result, q)
        books.fill(shubook, q)
        # return render_template('search_result.html', books=books)
        # return json.dumps(books,default= lambda o: o.__dict__)      # ----》》》》  dict迭代dict都顺便解析位json
        # return jsonify(books)   # TypeError: Object of type 'BookCollection' is not JSON serializable
        # return jsonify(result)
    else:
        flash('搜索的关键字不符合要求，请重新输入')
        # return jsonify({'msg':'Wrong,Error!!!'})
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)

@web.route('/test')
def test():
    r = {
        'name' : '文浩',
        'age' : 32
    }
    # 消息闪现
    flash('test函数的消息闪现1',category='mm1')
    flash('test函数的消息闪现2')
    # data_r 传给模板的数据
    return render_template('test.html', data_r = r)
    # return render_template('layout.html', data_r = r)

@web.route('/layout')
def layout():
    r = {
        'name' : '文浩',
        'age' : 32
    }
    # data_r 传给模板的数据
    return render_template('layout.html', data_r = r)

@web.route('/book/<isbn>/detail')
def book_detail():
    pass

@web.route('/index')
def index():
    headers = {
        'content-type': 'text/html;charset=utf-8',
    }
    return '<html><h1>HelloIndex+我是谁</h1></html>', 200, headers

@web.route('/my_gift')
def my_gifts():
    pass

@web.route('/my_wish')
def my_wish():
    pass

@web.route('/pending')
def pending():
    pass

@web.route('/login')
def login():
    pass

@web.route('/personal_center')
def personal_center():
    pass

@web.route('/logout')
def logout():
    pass

