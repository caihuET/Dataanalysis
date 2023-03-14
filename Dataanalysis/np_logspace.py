import numpy as np

"""
logspace(),等比数列
start：代表序列的起始值。
stop：代表序列的终止值。
num：生成的序列数个数。
endpoint：布尔类型值，默认是true。如果为true, 'stop'是最后一个样本；否则，它不包括在内。
base：代表序列空间的底数，默认基底为10。
dtype：代表序列数组项的数据类型。

"""

y = np.logspace(1, 10, base=5,num=2)
print(y)