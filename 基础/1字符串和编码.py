#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

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
#print(len('ABC'))
#print(len('中文'))
#print(len(b'ABC'))
#print(len("中文".encode("utf-8")))

# 格式化输出,print中 % 前面是控制样式，后面是变量，如只有一个变量，可以不用括号
# %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数,转义：%%表示一个%
print('%2d - %02d %%' % (3, 1))
print('%.2f' % 3.1415926)

# format()函数，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#f-string,以f开头，字符串中的表达式用大括号{}表示,{}内部可以直接写python表达式
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

s1 = 72
s2 = 85
print(f'原成绩：{s1:.1f}，现成绩{s2:.1f}，成绩提升了{((s2 - s1) / s1 * 100):.1f} %')
print('原成绩：%.1f，现成绩%.1f，成绩提升了:%.1f %%' % (s1,s2,(s2 - s1) / s1 * 100))
