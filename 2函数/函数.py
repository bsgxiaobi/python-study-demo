# -*- config:utf-8 -*-

# 调用函数
print(f'255的十六进制：{hex(255)}')
print(f'1000的十六进制：{hex(1000)}')

# 定义函数
#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(val):
    #三目运算符的两种写法，
    #[expression] and [on_true] or [on_false]，这种做法并不保险，因为当 on_true 为布尔值“假”时，结果将会出错
    #return val > 0 and val or -val
    
    #[on_true] if [expression] else [on_false]，python2.5之后才有的写法
    return val if val > 0 else -val

print(f'自定义函数：my_abs(100)={my_abs(100)}')