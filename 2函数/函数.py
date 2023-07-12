# -*- config:utf-8 -*-

import math

# 调用函数
print(f'255的十六进制：{hex(255)}')
print(f'1000的十六进制：{hex(1000)}')

# 定义函数
#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(val):
    if not isinstance(val,(int,float)):
        return TypeError('operand type in int or float')
    #三目运算符的两种写法，
    #[expression] and [on_true] or [on_false]，这种做法并不保险，因为当 on_true 为布尔值“假”时，结果将会出错
    #return val > 0 and val or -val
    
    #[on_true] if [expression] else [on_false]，python2.5之后才有的写法
    return val if val > 0 else -val

print(f'自定义函数：my_abs(100)={my_abs(100)}')

print(f'自定义函数：my_abs(100)={my_abs("100")}')

#空函数，如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

## pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，由于python无需花括号包裹函数，所以空语句需要pass来占位

# 返回多个值&默认值，返回值是一个tuple
# 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(f'返回多个值：x={x},y={y}')
print(f'返回多个值实际上是返回的一个tuple：{move(100,100,60,math.pi/6)}')