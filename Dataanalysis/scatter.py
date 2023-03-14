# coding=utf-8
#!/usr/bin/python3

import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_zh_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

# 生成一个3月份和4月份的气温数据
y_3 = random.sample(range(1, 40), 30)
y_4 = random.sample(range(1, 40), 30)
print(y_4, y_3)
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=60)
# 刻画x轴
x_3 = range(1, 31)
x_4 = range(50, 80)
# 绘制散点图
plt.scatter(x_3, y_3,label="3月")
plt.scatter(x_4, y_4,label="4月")

# 调整x轴的刻度
_x = list(x_3) + list(x_4)
xtick = ["3月{}日".format(i) for i in x_3]
xtick += ["4月{}日".format(i - 49) for i in x_4]
plt.xticks(_x[::3], xtick[::3], rotation=45, fontproperties=my_zh_font)

# 添加图例
plt.legend(prop=my_zh_font)
# 添加描叙信息
plt.xlabel("日期", fontproperties=my_zh_font)
plt.ylabel("温度", fontproperties=my_zh_font)
plt.title("温度记录", fontproperties=my_zh_font)

# 保存图形
plt.savefig("./t2.svg")
# 展示图形
plt.show()
