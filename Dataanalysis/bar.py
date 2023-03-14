import matplotlib.pyplot as plt
from matplotlib import font_manager
import pandas as pd
from sqlalchemy import create_engine

"""
查看系统字体
fc-list
查看系统中文字体(list与:之间有空格)
fc-list :lang=zh
"""

# 兼容显示中文
my_zh_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

# 连接数据库
engine = create_engine('mysql+pymysql://weiqian:1@127.0.0.1:3306/films', echo=True)
# 查询数据库中的数据
sql = '''
select release_date,film_name,box_office from film rdfnbo;
'''
# 以DataFrame格式读取显示
df = pd.read_sql(sql, engine)

# 将从数据库中获取到的数据定义到变量中
release_date = df['release_date']
film_name = df['film_name']
box_office = df['box_office']
print(release_date, film_name, box_office)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=60)

# 设置标题和x、y轴的名称
plt.xlabel('片名', fontsize=15, fontproperties=my_zh_font)
plt.ylabel('票房',fontsize=15, fontproperties=my_zh_font)
plt.title('电影票房排名', fontsize=30, fontproperties=my_zh_font,color='blue')
# 绘制图像，以下显示的柱状图是竖着的，如想使用横着的柱状图，使用barh()方法，同时width需要调整为height,xticks调整为yticks
plt.bar(range(len(film_name)), box_office, width=0.3)

# 设置字符串到x轴
plt.xticks(range(len(film_name)), film_name, fontsize=15, rotation=45, fontproperties=my_zh_font)


plt.show()
