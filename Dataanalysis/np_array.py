import numpy as np

# array()函数，括号内可以是列表、元组、数组、迭代对象、生成器
# 列表
a=np.array([1,2,3,4,5])
# 元组
b=np.array((1,2,3,4,5))
# 迭代对象
c=np.array(range(10))
print(c)
print("-"*30)
# 生成器
d=np.array([i**2 for i in range(10)])
print(d)
