# -*- config:utf-8 -*-

import sys

# 需要添加路径，否则找不到函数
sys.path.append('./2函数')
# from {module} import {function_name} #导入指定方法
# import {module_name} #全导入
from 函数 import my_abs

print(f'导入函数：my_abs(100)={my_abs(100)}')