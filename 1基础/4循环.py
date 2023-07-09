# python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for item in names:
    print(item)

# range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print(f'range(5):{list(range(5))}')
# 计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
i = 1;
while i <= 10:
    sum += i
    i += 1
print(f'计算1-10的整数之和:{sum}')

# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for item in L:
    print(f'Hello, {item}!')