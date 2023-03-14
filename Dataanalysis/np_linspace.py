import numpy as np

"""linspace()等差数列
start,开始；
stop,结束 
num=50,分成多少等分
endpoint=True,是否包含最后一位，默认为Ture
retstep=False,是否显示等差值，默认为False
dtype=None, 类型
axis=0，0(默认)或-1
"""
y = np.linspace(1, 10, num=10, retstep=True)
print(y)
