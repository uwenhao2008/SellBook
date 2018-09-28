#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
# 蓝图
web = Blueprint('web',__name__)  # 参数：蓝图名称，所在的包

# 导入视图函数 实现蓝图的注册  放最后，如果在web前面，则会报错 ，而且这个文件和book间不是循环导入的情况，book只会被导入一次
from app.web import book   # app初始化时候的 from app.web.book import web 去掉了，所以这里需要指定，否则book，user没有被导入，所以无法识别
from app.web import user
