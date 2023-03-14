import pandas as pd
import numpy as np

# 读取源文件
df1 = pd.ExcelFile('./11.xlsx')
df2 = pd.ExcelFile('./store.xlsx')

print(type(df1), type(df2))
# 按顺序获取sheet名称
print(df1.sheet_names, df2.sheet_names)

# 提取表格信息
sheet1 = df1.parse(sheet_name=0)
sheet2 = df2.parse(sheet_name=0)
print(format(sheet1), '\n', format(sheet2))

# 将源数据的复制3次。以下的(3,1),3表示沿着Y轴整体扩展3倍，1表示沿着X轴整体扩展1倍
new_sheet1 = pd.DataFrame(np.tile(sheet1, (3, 1)))
new_sheet2 = pd.DataFrame(np.tile(sheet2, (3, 1)))
# 定义新的数据表的列名称与旧的数据表的列名称相同
new_sheet1.columns = sheet1.columns
new_sheet2.columns = sheet2.columns

writer1 = pd.ExcelWriter('./22.xlsx')
writer2 = pd.ExcelWriter('./33.xlsx')
new_sheet1.to_excel(writer1)
new_sheet2.to_excel(writer2)
# 保存数据
writer1.save()
writer2.save()

# 查看是否有重复行
# re_row = new_sheet1.duplicated()
# print(re_row)
"""
合并表
"""
# 获取两张表
store_num = pd.read_excel('./33.xlsx')
store_info = pd.read_excel('./22.xlsx')
# store_num.head(10)
# store_info.head(10)

# 内连接
df_inner = store_num.merge(store_info, how='inner', left_index=True, right_index=True)
# 删除多余的列
df_inner = df_inner.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)
print(df_inner)
# 写入数据
writer3 = pd.ExcelWriter('./merge_33_22.xlsx')
df_inner.to_excel(writer3)
# 保存数据
writer3.save()
