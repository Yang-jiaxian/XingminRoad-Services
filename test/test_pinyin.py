# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
import pypinyin

s = ''
for i in pypinyin.pinyin("word", style=pypinyin.NORMAL):
    s += ''.join(i)

print(s)

