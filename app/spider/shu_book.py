#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
业务逻辑代码
'''
from app.libs.httper import HTTP
from flask import jsonify, current_app


class ShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    # isbn查询
    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    # keywords 查询
    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    # @classmethod   cls->self
    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        # 初步判断 是HTTP.get没有成功传递 url参数
        print('--->>>定位专用--search_by_isbn<<<---')
        print(url)
        result = HTTP.get(url)   # result是dict格式的 result会被转化为字典 这里没有传递第二个参数，就会采用默认的
        print(result)   #---OK 有数据的
        self.__fill_single(result)  # 保留数据在类内部
        # return jsonify(result)
        # 纠结这么就的问题终于解决了，我做个总结，22行这里我以前生成的是dict 必须要解析会json然后返回给

    # @classmethod  cls->self
    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        print('--->>>定位专用--search_by_keyword<<<---')
        result = HTTP.get(url)
        self.__fill_collection(result)
        # return jsonify(result)

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']