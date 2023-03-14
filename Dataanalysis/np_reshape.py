import numpy as np

# reshape(),可调整纬度
a = np.arange(20)
"""
调整为4行5列
"""
print(a.reshape(4, 5))
print("-" * 30)
"""
resize(),如果新数组大于原始数组，则新数组将填充a到重复副本
"""
# a为2行2列
b = np.array([[0, 1], [2, 3]])
# 将a调整为2行3列的新数组
new_b = np.resize(b, (2, 3))
print(new_b)

