import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc("font", family='SimHei')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


data=pd.read_csv(r'/Users/zhouyu/PycharmProjects/pythonProject/数据分析课程设计 3/data/高考录取分数数据集.csv')


print(data.head())

df=data.rename(columns={'录取分数1':'2020录取分数','录取分数2':'2019录取分数',
                          '录取分数3':'2018录取分数','录取分数4':'2017录取分数','录取分数5':'2016录取分数','平均分数':'近五年平均录取分数'})

data.info()

# 查看重复值个数
print('重复值个数：\n',df.duplicated().sum())

# 查看缺失值个数
print('缺失值情况：\n',df.isnull().sum())

describe = df.describe()
print(describe)

# 统计北京大学、清华大学、浙江大学、上海交通大学、南京大学、西安交通大学、中国科学技术大学、武汉大学、华中科技大学近五年在鄂招生分数变化
from matplotlib.pyplot import MultipleLocator

universityPart =['北京大学', '清华大学', '浙江大学', '上海交通大学', '南京大学', '西安交通大学', '中国科学技术大学', '武汉大学', '华中科技大学']
universityPartZh = ['北京大学', '清华大学', '浙江大学', '上海交通大学', '南京大学', '西安交通大学', '中国科学技术大学', '武汉大学', '华中科技大学']
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
for i in range(len(universityPartZh)):
    print(universityPartZh[i], ':', scores[i])

for i in range(2):
    plt.plot(year, scores[i].tolist(), 'o--', label=universityPart[i])
    # 设置数字标签
    for a, b in zip(year, scores[i].tolist()):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
plt.legend()
plt.title('中国顶尖的两所大学')
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(10)  # 把y轴的刻度间隔设置为20，并存在变量里
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
plt.show()

for i in range(7, 9):
    plt.plot(year, scores[i].tolist(), 'o--', label=universityPart[i])
    for a, b in zip(year, scores[i].tolist()):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
plt.legend()
plt.title('武汉顶尖的两所大学')
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(10)  # 把y轴的刻度间隔设置为20，并存在变量里
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
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

