#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-10-10'
"""
class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']
        self.isbn = book['isbn']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)

    # 定义需要的数据类型--关键字查询  data为API回调数据
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': '',
            'keyword': keyword
        }
        # 按关键字查询的时候只有一条数据
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            # r1 = returned['total']
            # r2 = returned['books']
            # d1 = data['total']
            returned['total'] = data['total']  #有错误需要修改！！len(data['books'])
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]  #好好理解这句话  循环推倒式 循环执行裁剪一本书数据的方法
        return returned

    # 进行数据裁剪
    @classmethod
    def __cut_book_data(cls, data):
        # print(data)
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']), #   '、'.join(data['author'])  把序列author转换字符串显示
            'price': data['price'],
            'summary': data['summary'] or '',  # 杜绝页面出现null
            'image': data['image']
        }
        return book

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, shu_book, keyword):
        self.total = shu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in shu_book.books]

