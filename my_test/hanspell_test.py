#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from hanspell import spell_checker
import time

time1 = time.time()
word = "안녕 하세요. 안녕 하세요. 안녕 하세요. "
result = spell_checker.check(word).as_dict()
# result = spell_checker.check(u'안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.')
# print(result)

print(result["checked"])
print(result["time"])

time2 = time.time()

print(time2 - time1)
# {'checked': '안녕하세요. 저는 한국인입니다. 이 문장은 한글로 작성됐습니다.',
#  'errors': 4,
#  'original': '안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.',
#  'result': True,
#  'time': 0.07065701484680176,
#  'words': {'안녕하세요.': 2,
#            '저는': 0,
#            '한국인입니다.': 2,
#            '이': 2,
#            '문장은': 2,
#            '한글로': 0,
#            '작성됐습니다.': 1}}
