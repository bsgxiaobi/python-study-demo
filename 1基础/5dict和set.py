# -*- coding: utf-8 -*-

## dictinary 字典,key-value存储的一种映射关系,在其他语言中也称为map
# 添加数据：初始化
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(f'd:{d};\nd["Michael"]:{d["Michael"]};\nd["Bob"]:{d['Bob']}')

# 添加数据：通过key放入
d['Adam'] = 67
print(f'd:{d};\nd["Adam"]:{d["Adam"]}')

# 判断key是否存在：通过in
print(f'判断key是否存在：{"bsg" in d}')

# 获取值，get()方法，如果key不存在，可以返回None，或者自己指定的value
print(f'获取值：{d.get("bsg")}')
print(f'获取值：{d.get("bsg","bsg is not in d")}')

# 删除值，pop(key)方法，对应的value也会从dict中删除,key不存在会报错
print(f'删除前：{d}')
d.pop('Michael')
print(f'删除后：{d}')


## set 集合,无序和无重复元素的集合
# set和dict类似，也是一组key的集合，但不存储value，由于key不能重复，所以，在set中，没有重复的key
# 添加数据：初始化
s = set([1, 2, 3, 3])
print(f's:{s}')

# 添加数据：通过add(key)方法,重复添加无效果
s.add('bishugui')
print(f's:{s}')

# 判断是否存在
print(f'判断是否存在"bishugui" in s：{"bishugui" in s}')

# 删除数据：通过remove(key)方法
s.remove('bishugui')
print(f'set删除数据后:{s}')
