from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

x_length = [random.randint(85, 140) for i in range(224)]

# 设置组距
g = 4
num_bins = (max(x_length)-min(x_length))//g
# 设置x轴的刻度
plt.xticks(range(min(x_length),max(x_length)+g,g))

# 添加网格
plt.grid()
# 使用柱状图
plt.hist(x_length,num_bins,density=True)
plt.show()