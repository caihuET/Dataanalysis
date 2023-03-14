import pandas as pd
import numpy as np

# file = open('./write','a')
# a=np.random.rand(5)
# b=np.random.randn(4,3,3,2)
# print(a)
# print(b)
s = pd.Series([1, 2, 3, np.nan, 44, 11])
print(s)
data=np.arange(12).reshape((3,4))
# print(data)
# file.write(s)
# file.close()
np.savetxt('./write',data,fmt='%d', delimiter=',')