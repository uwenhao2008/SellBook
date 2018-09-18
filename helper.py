#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_isbn_or_key(word):
    '''

    :param word:
    :return:
    '''
    # 默认值为关键字检索
    isbn_or_key = 'key'
    # 进行q是否是isbn13的判断
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
