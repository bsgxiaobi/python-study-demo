# -*- codeing: utf-8 -*-

# list是一种有序的集合，可以随时添加和删除其中的元素
classname = ['Michael', 'Bob', 'Tracy']
print(f'数组：{classname}，长度：{len(classname)}')
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


