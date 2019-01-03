#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018-11-28'
"""
'''
发现问题所在，并不是说相同密码hash以后的结果就是相同的，貌似不同程序相同密码hash的值不一定一样，但是同一套程序，经过hash的密码可以相互比较
和程序有关，我不能用yushu的hash密码wen123 得到的结果来检查对比这里的程序hash化wen123的结果
我这里理解错了，是可以用同一个密码生成的hash进行对比的

我犯错的原因是，这里的密码没有经过数据库，所以就不存在截断的可能
'''
from werkzeug.security import generate_password_hash, check_password_hash

p = 'wen001'   # 原始密码wen321  解析后的结果 pbkdf2:sha256:50000$XglMA6bH$5d3437abf4707056cf16975ab09d98c9b1a9080547406e6629a3f63a96bd63f0
_p = generate_password_hash(p)
print(_p)
# pbkdf2:sha256:50000$MB5wMhIP$fab1254a62cef04294a2b15c5bc654bd48d434a4299f7224d4f7c0267514d8bc   OK   wen321
# pbkdf2:sha256:50000$f1s1Uc4o$048f94975786d8de7fa229b9fdcc1d57481cc3a3793b6b1cd2cd3be66b22d2aa   OK
# pbkdf2:sha256:50000$XglMA6bH$5d3437abf4707056cf16975ab09d98c9b1a9080547406e6629a3f63a96bd63f0   错误的hash 不是对应的 wen321
if check_password_hash(_p,p):
    print("解码成功")
else:
    print("失败了，请查找原因")

# if check_password_hash('pbkdf2:sha256:50000$XglMA6bH$5d3437abf4707056cf16975ab09d98c9b1a9080547406e6629a3f63a96bd63f0','wen321'):
# pbkdf2:sha256:50000$pAft51b8$d9a49a5f335914ccf00ed552a398dc87d77
# pbkdf2:sha256:50000$9dSGDKnj$b1293022fb21ccecbd8523a4de7d3c154cf4f7b3a7f2a5da8b5511dec0c1c64f
if check_password_hash('pbkdf2:sha256:50000$pAft51b8$d9a49a5f335914ccf00ed552a398dc87d77','wen001'):
    print("居然是True")
else:
    print("Wrong")


