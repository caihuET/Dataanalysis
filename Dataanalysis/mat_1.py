import matplotlib.pyplot as plt

# import matplotlib as plt

x = range(2, 26, 2)
y = [12, 22, 3, 14, 25, 33, 22, 12, 11, 24, 32, 43]

# 设置图片大小
plt.figure(figsize=(10, 6), dpi = 60)
# 设置x轴的刻度
xtick = [i/2 for i in range(4, 49)]
# 刻度太密集时，可以通过步长进行调整
plt.xticks(xtick[::3])
# 设置y轴刻度
plt.yticks(range(min(y), max(y)+2)[::3])
# 绘图
plt.plot(x, y)
# 保存
plt.savefig("./t1.svg")
# 展示图形
plt.show()
