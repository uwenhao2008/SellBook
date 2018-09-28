#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
业务逻辑代码
'''
from httper import HTTP
from flask import jsonify

class ShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        # 初步判断 是HTTP.get没有成功传递 url参数
        print('--->>>定位专用<<<---')
        print(url)
        result = HTTP.get(url)   # result是dict格式的 result会被转化为字典 这里没有传递第二个参数，就会采用默认的
        print(result)   #---OK 有数据的
        return jsonify(result)
        # 纠结这么就的问题终于解决了，我做个总结，22行这里我以前生成的是dict 必须要解析会json然后返回给

    @classmethod
    def search_by_keyword(cls,keyword,count=15,start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return jsonify(result)