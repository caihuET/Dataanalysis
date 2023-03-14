# coding = utf-8
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random
import flask,json_test

# 设置中文字体
my_zh_font = font_manager.FontProperties(fname = "/System/Library/Fonts/PingFang.ttc")

"""
绘制一个10点到12点，每一分钟气温变化的折线图
"""
x = range(0, 120)
y = [random.randint(15, 25) for i in range(120)]

# 设置图片大小
plt.figure(figsize=(20, 6), dpi = 60)
# 绘图
plt.plot(x, y)

# 调整x轴的刻度
xtick = ["10点{}分".format(i) for i in range(60)]
xtick += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::6], xtick[::6], rotation = 45, fontproperties = my_zh_font)

# 添加x轴和y轴的描述信息
plt.xlabel("时间", fontproperties = my_zh_font)
plt.ylabel("温度", fontproperties = my_zh_font)
plt.title("10:00到12点的温度情况", fontproperties = my_zh_font)
# 绘制网格 alpha--透明度，0～1；
plt.grid(alpha=0.4)
plt.yticks(range(min(y),max(y)+2))
# 展示图形
plt.show()
