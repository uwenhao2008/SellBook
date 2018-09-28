#!/usr/bin/env python
# -*- coding: utf-8 -*-

# urllib   自带的   from urllib import request
# requests  第三方库
'''
http请求类
'''
import requests

class HTTP:
    @staticmethod
    def get(url, return_json = True):   # 没有 self 参数~~~~~~~~~
        r = requests.get(url)
        # restful API
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:    # 找不到isbn的时候，状态码是404
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''