import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc("font", family='SimHei')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

data=pd.read_csv('/Users/zhouyu/PycharmProjects/pythonProject/数据分析课程设计/data/高考录取分数数据集.csv')
print(data.head())

# 对录取分数1-5,平均分数进行重新命名
df=data.rename(columns={'录取分数1':'2020录取分数','录取分数2':'2019录取分数',
                          '录取分数3':'2018录取分数','录取分数4':'2017录取分数','录取分数5':'2016录取分数','平均分数':'近五年平均录取分数'})

print('\n重新命名后的前5行：')
print('\n',df.head())

# 可以发现有些录取分数是用异常值'------'代替的
# 将'------'用NULL代替
df = df.replace('------',np.nan)

# 检测空值
null_data = df.isnull()

# 查看缺失值个数
print('缺失值情况：\n',null_data.sum())

# 对缺失值使用平均值填充
df['2020录取分数'] = df['2020录取分数'].fillna(df['近五年平均录取分数'])
df['2019录取分数'] = df['2019录取分数'].fillna(df['近五年平均录取分数'])
df['2018录取分数'] = df['2018录取分数'].fillna(df['近五年平均录取分数'])
df['2017录取分数'] = df['2017录取分数'].fillna(df['近五年平均录取分数'])
df['2016录取分数'] = df['2016录取分数'].fillna(df['近五年平均录取分数'])

# 查看重复值个数
print('重复值个数：\n',df.duplicated().sum())

df.info()
print(df.head())


#
describe = df.describe()
print(describe)


# # 分组分析：按照学校编号或招生省份对数据进行分组，比较不同学校或不同省份的录取分数情况
# g1 = df.groupby("学校编号") # 按照学校编号分组
# g2 = df.groupby("招生省份") # 按照招生省份分组
# gd1 = g1.agg({"近五年平均录取分数": np.mean}) # 求每个学校的近五年平均录取分数
# gd2 = g2.agg({"近五年平均录取分数": np.mean}) # 求每个省份的近五年平均录取分数
# gd1.plot.bar() # 用柱状图显示不同学校的近五年平均录取分数
# plt.show()
# gd2.plot.bar() # 用柱状图显示不同省份的近五年平均录取分数
# plt.show()

# # 分布分析：对录取分数进行分布分析，查看其频数、频率、累计频率等指标
# bins = [0, 500, 550, 600, 650, 700, 750] # 定义分数区间
# labels = ["0-500", "500-550", "550-600", "600-650", "650-700", "700-750"] # 定义区间标签
# df["score_bin"] = pd.cut(df["近五年平均录取分数"], bins=bins, labels=labels) # 对近五年平均录取分数进行分析
# freq = df["score_bin"].value_counts() # 计算每个区间的频数
# freq_rel = freq / freq.sum() # 计算每个区间的频率
# freq_cum = freq_rel.cumsum() # 计算每个区间的累计频率
# dist = pd.DataFrame({"频数": freq, "频率": freq_rel, "累计频率": freq_cum}) # 构建分布表
# dist.plot.bar() # 用柱状图显示各区间的频数和频率
# plt.show()

# # 交叉分析：按照文理科和招生省份对数据进行交叉分析，查看不同类别之间的关系和差异
# cross = pd.crosstab(df["文/理"], df["招生省份"]) # 构建交叉表
# cross_rel = cross / cross.sum() # 计算相对频数表
# cross.plot.bar(stacked=True) # 用堆叠柱状图显示各类别的绝对频数
# plt.show()
# cross_rel.plot.bar(stacked=True) # 用堆叠柱状图显示各类别的相对频数
# plt.show()

# # 结构分析：对数据进行结构分析，查看各部分在整体中所占的比例和地位
# struct1 = df["文/理"].value_counts() # 计算文理科的数量
# struct2 = df["招生省份"].value_counts() # 计算招生省份的数量
# struct1.plot.pie(autopct="%.2f%%") # 用饼图显示文理科在总体中的比例
# plt.show()
# struct2.plot.pie(autopct="%.2f%%") # 用饼图显示招生省份在总体中的比例
# plt.show()

# # 相关分析：对数据进行相关分析，查看不同变量之间的相关性和影响程度
# corr = df.corr() # 计算各变量之间的相关系数矩阵
# corr.style.background_gradient(cmap="Blues") # 用颜色渐变显示相关系数的大小
# plt.show()