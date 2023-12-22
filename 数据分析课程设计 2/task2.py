import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

plt.rc("font", family='SimHei')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

data=pd.read_csv('/Users/zhouyu/PycharmProjects/pythonProject/数据分析课程设计 2/data/高考录取分数数据集.csv')
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


bins = [0, 500, 550, 600, 650, 700, 750] # 定义分数区间
labels = ["0-500", "500-550", "550-600", "600-650", "650-700", "700-750"] # 定义区间标签

df["score_bin"] = pd.cut(df["近五年平均录取分数"], bins=bins, labels=labels) # 对近五年平均录取分数进行分析

dist = df["score_bin"].value_counts(normalize=True).sort_index() # 构建分布表
dist.plot(kind="bar",figsize=(8,6)) # 用柱状图显示各区间的频数和频率
plt.xticks(rotation=30)
plt.title("录取分数分布")
plt.xlabel("分数范围")
plt.ylabel("频率")
plt.show()

# 结构分析：对数据进行结构分析，查看各部分在整体中所占的比例和地位
# struct1 = df["文/理"].value_counts() # 计算文理科的数量
struct1 = df["招生省份"].value_counts() # 计算招生省份的数量
# struct1.plot.pie(autopct="%.2f%%") # 用饼图显示文理科在总体中的比例
# plt.title('文理科在总体中的比例')
# plt.show()

struct1.plot.pie(autopct="%.1f%%") # 用饼图显示招生省份在总体中的比例
plt.title('招生省份在总体中的比例')
plt.tight_layout()
plt.show()

# 2.分布分析
# 箱线图
plt.boxplot(df['近五年平均录取分数'], vert=False)
plt.title('录取分数箱形图')
plt.xlabel('录取分数')
plt.show()

# 分组分析
grouped_df = df.groupby("招生省份")["近五年平均录取分数"].mean().reset_index()
grouped_df = grouped_df.sort_values("近五年平均录取分数", ascending=False)

# 分布分析
data_counts = data["招生省份"].value_counts()
data_counts = data_counts[data_counts>0] # 去掉数量为0的省份
data_counts_sorted = data_counts.sort_values(ascending=False)

fig, axs = plt.subplots(2, 2, figsize=(16, 12))

# 柱状图1
axs[0, 0].bar(grouped_df["招生省份"], grouped_df["近五年平均录取分数"], width=0.5)
axs[0, 0].set_xticklabels(grouped_df["招生省份"], rotation=45, ha="right")
axs[0, 0].set_xlabel("招生省份")
axs[0, 0].set_ylabel("近五年平均录取分数")
axs[0, 0].set_title("最近五年内招生省份的录取平均分数")

# 柱状图2
axs[0, 1].bar(data_counts_sorted.index, data_counts_sorted.values, width=0.5)
axs[0, 1].set_xticklabels(data_counts_sorted.index, rotation=45, ha="right")
axs[0, 1].set_xlabel("招生省份")
axs[0, 1].set_ylabel("数量/所")
axs[0, 1].set_title("各省份招生分布情况")

# 柱状图3
cross_df = pd.crosstab(df["招生省份"], df["文/理"])
cross_df.plot(kind="bar", stacked=True, ax=axs[1, 0])
axs[1, 0].set_xticklabels(cross_df.index, rotation=45, ha="right")
axs[1, 0].set_xlabel("招生省份")
axs[1, 0].set_ylabel("数量")
axs[1, 0].set_title("各省份文科和理科录取情况")

# 柱状图4
std_df = df.groupby("招生省份")["2020录取分数"].std().reset_index()

axs[1, 1].bar(std_df["招生省份"], std_df["2020录取分数"], width=0.5)
axs[1, 1].set_xticklabels(std_df["招生省份"], rotation=45, ha="right")
axs[1, 1].set_xlabel("招生省份")
axs[1, 1].set_ylabel("录取分数标准差")
axs[1, 1].set_title("不同省份的录取分数标准差")

plt.subplots_adjust(hspace=0.4) # 调整子图之间的间距
plt.show()


# 统计在每个省份招生的学校数目
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False


numCollegeEnrollPerProvince = df['招生省份'].value_counts()
print(numCollegeEnrollPerProvince)
province = ['河南', '安徽', '甘肃', '山西', '四川', '山东', '河北', '贵州', '内蒙古', '云南', '湖北', '广西', '广东', '湖南', '重庆', '辽宁', '陕西', '江西',
            '新疆', '福建', '黑龙江', '吉林', '浙江', '宁夏', '江苏', '青海', '海南', '天津', '西藏', '上海', '北京']
plt.plot(range(1, len(province) + 1), numCollegeEnrollPerProvince, 'ro-')
plt.title('各省入学的大学总数')
plt.xticks(range(1, len(province) + 1), province, rotation=90)
plt.ylabel('Counts')
plt.show()

from matplotlib.pyplot import MultipleLocator

universityPartZh = ['北京大学', '清华大学', '浙江大学', '上海交通大学', '南京大学', '西安交通大学', '中国科学技术大学',
                    '武汉大学', '华中科技大学']
year = [2020, 2019, 2018, 2017, 2016]
scores = np.zeros([len(universityPartZh), 5], dtype=int, order='C')
for i in range(len(universityPartZh)):
    for j in range(46927):
        if (df['学校'][j] == universityPartZh[i]) & (df['招生省份'][j] == '湖北'):
            for k in range(5, 10):
                if df.iloc[j, k] == '------':  # 处理异常值
                    scores[i, k - 5] = df.iloc[j, 10]
                else:
                    scores[i, k - 5] = df.iloc[j, k]

fig, axs = plt.subplots(1, 2, figsize=(16, 5))

# 北京大学和清华大学的变化
axs[0].plot(year, scores[0].tolist(), 'o--', label='北京大学')
axs[0].plot(year, scores[1].tolist(), 'x--', label='清华大学')
for a, b in zip(year, scores[0].tolist()):
    axs[0].text(a, b, b, ha='center', va='bottom', fontsize=8)
for a, b in zip(year, scores[1].tolist()):
    axs[0].text(a, b, b, ha='center', va='bottom', fontsize=8)
axs[0].legend()
axs[0].set_title('北京大学和清华大学近五年的在鄂招生分数变化')
axs[0].set_xlabel('年份')
axs[0].set_ylabel('录取分数')

# 武汉大学和华中科技大学的变化
axs[1].plot(year, scores[7].tolist(), 'o--', label='武汉大学')
axs[1].plot(year, scores[8].tolist(), 'x--', label='华中科技大学')
for a, b in zip(year, scores[7].tolist()):
    axs[1].text(a, b, b, ha='center', va='bottom', fontsize=8)
for a, b in zip(year, scores[8].tolist()):
    axs[1].text(a, b, b, ha='center', va='bottom', fontsize=8)
axs[1].legend()
axs[1].set_title('武汉大学和华中科技大学近五年的在鄂招生分数变化')
axs[1].set_xlabel('年份')
axs[1].set_ylabel('录取分数')

# 设置刻度间隔
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(10)
for ax in axs:
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)

plt.show()

# 统计武汉大学在每个省份招生的录取平均分数
averageScores = []
for i in range(len(province)):
    for j in range(46927):
        if (df['学校'][j] == '武汉大学') & (df['招生省份'][j] == province[i]):
            averageScores.append(df['近五年平均录取分数'][j])
plt.plot(list(range(1, len(province) + 1)), averageScores, 'o-')
plt.title('武汉大学各省平均录取分数线')
plt.xticks(range(1, len(province) + 1), province, rotation=90)
plt.ylabel('score')
plt.show()

