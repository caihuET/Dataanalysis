import numpy as np

"""
ndarray.ndim,返回数组的纬度（秩）：轴的数量，或者纬度的数量，是一个标量，
一维数组的秩为1，二维数组的秩为2
"""
a=np.array([1,2,3,4,5,6])
b=a.reshape((2,3))
c=np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [11,22,33],
        [44,55,66]
    ]
])
print("a的ndim",a.ndim)
print("b的ndim",b.ndim)
print("c的ndim",c.ndim)

# ndarray.size,数组元素中的总个数
a=np.array([1,2,3,4,5,6])
print(a.size)

# ndarray.dtype
print(a.dtype)

# astype(),强制改变数据类型
a=np.array([1.1,2.1,3.1])
b=a.astype("int")
print(b)