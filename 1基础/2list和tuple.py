# -*- codeing: utf-8 -*-

## list 列表，是一种有序的集合，可以随时添加和删除其中的元素
classname = ['Michael', 'Bob', 'Tracy']
print(f'数组：{classname}，长度：{len(classname)}')
# 取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素,以此类推，可以获取倒数第2个、倒数第3个
print(f'第一个元素：{classname[0]}，最后一个元素：{classname[-1]}')

# 添加元素
classname.append('Adam')
print(f'添加元素后：{classname}')
# 插入元素
classname.insert(1, 'Jack')
print(f'插入元素后：{classname}')

# 删除末尾元素
classname.pop()
print(f'删除末尾元素后：{classname}')
# 删除指定位置元素，pop(i)，i为索引位置
classname.pop(1)
print(f'删除指定位置元素后：{classname}')

# 元素替换，直接赋值
classname[1] = 'Sarah'  
print(f'元素替换后：{classname}')

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(f'list里面的元素的数据类型也可以不同：{L}')

## tuple 元组，tuple和list非常类似，但是tuple一旦初始化就不能修改
# tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
# 如果要定义一个空的tuple，可以写成()
# 但是，要定义一个只有1个元素的tuple，如果你这么定义：t = (1)，定义的不是tuple，是1这个数！
tupleTest = ('Michael', 'Bob', 'Tracy')
print(f'tupleTest:{tupleTest}')
tupleOne = ('single') # 定义一个只有1个元素的tuple，必须加一个逗号,，来消除歧义
print(f'tupleOne:{tupleOne}')


# “可变的”tuple
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变，tuple指向的list对象不变，但list本身是可变的
t = ('a', 'b', ['A', 'B'])
print(f'改变tuple前的值:{t}')
t[2][0] = 'A1'
t[2][1] = 'B1'
print(f'改变tuple后的值:{t}')


# 练习
# 请用索引取出下面list的指定元素：
L = [ 
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa'] 
    ]
# 打印Apple:
print(f'练习,打印Apple:{L[0][0]}')
# 打印Python:
print(f'练习,打印Python:{L[1][1]}')
# 打印Lisa:
print(f'练习,打印Lisa:{L[2][2]}')