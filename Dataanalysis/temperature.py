from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

# 设置中文字体
my_zh_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
# 生成最高气温和最低气温两组数据
max_temp = [np.random.randint(16, 23) for i in range(31)]
min_temp = [np.random.randint(2, 15) for i in range(31)]

# 绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
dates = range(1, 32)
ax.plot(dates, max_temp, c='#FF69B4', alpha=0.5)
ax.plot(dates, min_temp, c='g', alpha=0.5)
ax.fill_between(dates,max_temp,min_temp,facecolor='b',alpha=0.1)

# 设置图形的格式
# 设置标题
ax.set_title('2022年3月每日气温', fontsize=14, fontproperties=my_zh_font)
# 设置x轴
ax.set_xlabel('', fontsize=11)
# 设置y轴
ax.set_ylabel('温度(F)', fontsize=11, fontproperties=my_zh_font)
ax.tick_params(axis='both', which='major', labelsize=11)
datetick = ["3月{}日".format(i) for i in range(1, 32)]
plt.xticks(list(dates)[::2], datetick[::2], rotation=45, fontproperties=my_zh_font)

plt.show()
