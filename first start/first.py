#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#print("Hello Word 你好世界")

# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)

# 不同得输出形式
# print(10_000_000_000)
# print(0xff00)
# print('\n\nI\'m \"OK\"!')

# 字符串的问题
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print('\u4e2d\u6587')

# 编码问题
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
# print(b'ABC')
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))

# 解码问题
# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 计算字符串长度
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len("中文".encode("utf-8")))

# 格式化输出
