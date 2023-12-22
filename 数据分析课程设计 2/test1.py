import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data2=pd.read_excel('/Users/zhouyu/PycharmProjects/pythonProject/数据分析课程设计 2/data/quanguoputonggaodengxuexiaomingdan.xls')
plt.rc("font", family='SimHei')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
print(data2.head())
print(data2.info())
#
#1.学校数量及所在地分析
plt.figure(figsize=(10,8))
groupby_province = data2.groupby('所属省份')['学校名称'].agg(数量=('count'))
print('各省大学个数：',groupby_province)
# 各省大学个数饼图
arr = list(groupby_province['数量'].values)
label=np.array([])
label=np.append(label,data2['所属省份'].drop_duplicates().dropna())
print('省份个数：',label.size)
plt.title('各省大学占比')
plt.pie(arr,labels=label,autopct='%1.1f%%')
plt.legend(loc='upper right',fontsize=7,bbox_to_anchor=(1.1, 1.05))
plt.show()

# 2.学校类型比较分析
#
# 所有大学本科，专科数量
# 本科，专科，民办，中外，中外合作办学
school_property_bk =data2[data2['办学层次']=='本科']
school_property_zk =data2[data2['办学层次']=='专科']
# 本科
# 民办
school_property_bk_private = school_property_bk[school_property_bk['备注']=='民办']
school_property_bk_private_count = school_property_bk_private['学校名称'].count()
#合资
school_property_bk_jointly = school_property_bk[school_property_bk['备注']=='中外合作办学']
school_property_bk_jointly_count = school_property_bk_jointly['学校名称'].count()
# 专科
#民办
school_property_zk_private = school_property_zk[school_property_zk['备注']=='民办']
school_property_zk_private_count = school_property_zk_private['学校名称'].count()
# 合资
school_property_zk_jointly = school_property_zk[school_property_zk['备注']=='中外合作办学']
school_property_zk_jointly_count = school_property_zk_jointly['学校名称'].count()
school_property_bk_count = school_property_bk['办学层次'].count()
school_property_zk_count = school_property_zk['办学层次'].count()
#公办本科
school_property_bk_public_count = school_property_bk_count-school_property_bk_private_count-school_property_bk_jointly_count
#公办专科
school_property_zk_public_count = school_property_zk_count-school_property_zk_private_count-school_property_zk_jointly_count
print('本科院校数量：',school_property_bk_count)
print('本科院校中的民办数量：',school_property_bk_private_count)
print('本科院校中的合资数量：',school_property_bk_jointly_count)
print('本科院校中的公办数量：',school_property_bk_public_count)
print('\n')
print('专科院校数量：',school_property_zk_count)
print('专科科院校中的民办数量：',school_property_zk_private_count)
print('专科院校中的合资数量：',school_property_zk_jointly_count)
print('专科院校中的公办数量：',school_property_zk_public_count)

x1=['本科总数量','公办本科','合资本科','民办本科','专科总数量','公办专科','合资专科','民办专科']
y =[school_property_bk_count,(school_property_bk_count-school_property_bk_private_count-school_property_bk_jointly_count),school_property_bk_jointly_count,
    school_property_bk_private_count,school_property_zk_count,(school_property_zk_count-school_property_zk_private_count-school_property_zk_jointly_count),school_property_zk_jointly_count,
    school_property_zk_private_count]
fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].pie(y, labels=x1, autopct='%1.2f%%')
axs[0].legend(x1, loc='upper right', fontsize=7, bbox_to_anchor=(1.1, 1.05))
axs[0].set_title('学校类型占比')

# 学校类型数量
axs[1].bar(x1, y, width=0.8, align="center")
axs[1].plot(x1, y, 'r-')
axs[1].set_xlabel('办学层')
axs[1].set_ylabel('学校数量/个')
axs[1].set_title('学校类型数量')
axs[1].set_xticks(range(len(x1)))  # 设置刻度位置
axs[1].set_xticklabels(x1, rotation=30)
axs[1].legend(['数量'], loc='upper left', fontsize=7)
plt.show()


# 选出各省份大学最多的城市
# groupby_province1 = data2.groupby('所属省份')['所在地'].agg(数量=('count'))

groupby_province1 = data2.groupby('所在地')['学校名称'].agg(数量=('count')).sort_values(by='数量',ascending=False)

print(groupby_province1)
print(groupby_province1.describe())

print(groupby_province1[groupby_province1['数量']>=8])

arr1=list(groupby_province1[groupby_province1['数量']>=8]['数量'])
arr2=list(groupby_province1['数量'].drop_duplicates())
print(len(arr1))
print(len(arr2))
print(groupby_province1['数量'].max())

#各城市大学数量频率直方图 && 各城市大学数量的众数柱状图&&折线图
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14,8))
ax1.set_title('各城市大学数量频率直方图')
ax1.hist(arr1,bins=65,color="green",edgecolor="black")
ax1.set_xlabel('区间(学校个数)')
ax1.set_ylabel('频数/频率')
ax2.set_title('各城市大学数量的众数柱状图')
ax2.bar(groupby_province1['数量'].drop_duplicates().index,arr2,color="red",edgecolor="black")
ax2.plot(groupby_province1['数量'].drop_duplicates().index,arr2,"b-.")
ax2.set_xlabel('学校')
ax2.set_ylabel('单位/个')
plt.xticks(rotation=90,fontsize=6)
plt.show()

# 3.主管部门和办学层级分析
groupby_department = data2.groupby('主管部门')['学校名称'].agg(数量=('count'))


print(groupby_department)
print(groupby_department.describe())


arr3 = list(groupby_department.index)
arr4 = list(groupby_department['数量'])
# 多于平均值
arr5 = list(groupby_department[groupby_department['数量']>=40].index)
arr6 = list(groupby_department[groupby_department['数量']>=40]['数量'])

plt.figure(figsize=(10,6))
x_t = range(len(arr5))
plt.yticks(x_t,arr5)
plt.barh(arr5,arr6,height=0.5)
plt.title('主管部门学校数量（仅显示大于平均值的）')
plt.ylabel("主管部门名称")
plt.xlabel('学校数量/个')
plt.xticks(rotation=90)
plt.show()

# 4.省份间办学层次的对比分析
arr1=list(data2['所属省份'].drop_duplicates().dropna())
print(arr1)

# 按数量从大到小排列
groupby_sf_all =data2.groupby('所属省份')['学校名称'].agg(数量=('count')).sort_values(by='数量',ascending=False)
print(groupby_sf_all)

groupby_sf_bk =data2[data2['办学层次']=='本科'].groupby('所属省份')['学校名称'].agg(数量=('count'))
print(groupby_sf_bk)

groupby_sf_zk =data2[data2['办学层次']=='专科'].groupby('所属省份')['学校名称'].agg(数量=('count'))
print(groupby_sf_zk)

plt.figure(figsize=(10,6))
# 绘制全部学校
plt.scatter(list(groupby_sf_all.index),list(groupby_sf_all['数量']),label='全部学校',c='r',marker='o')

#绘制本科学校
plt.scatter(list(groupby_sf_bk.index),list(groupby_sf_bk['数量']),label='本科学校',c='g',marker='x')

#绘制专科学校
plt.scatter(list(groupby_sf_zk.index),list(groupby_sf_zk['数量']),label='专科学校',c='b',marker='v')
plt.xticks(rotation=90)
# plt.tight_layout()
plt.title('省份间办学层次的对比分析')
plt.legend()
plt.xlabel('省份')
plt.ylabel('数量/个')
plt.show()
# 主管部门和办学层级的联合分析（交叉分布）
df1 = data2[data2['办学层次']=='本科'].groupby('主管部门')['学校名称'].agg(本科=('count'))

df1['专科'] = data2[data2['办学层次']=='专科'].groupby('主管部门')['学校名称'].agg(专科=('count'))
print(df1)

data3 = groupby_department.sort_values(by='数量',ascending=False).head(15)
print(df1)

count_bin =[0,10,20,30,40,50,60,70,80]
count_labels = ['0-9个','10-19','20-29','30-39','40-49','50-59','60-69','70-79']
df1['数量分层'] = pd.cut(df1['本科'], count_bin, right=False, labels=count_labels)
df1['专科数量分层'] = pd.cut(df1['专科'], count_bin, right=False, labels=count_labels)

ptResult1=df1.pivot_table(
    values=['本科'],
    index=['数量分层'],
    columns=[],
    aggfunc=[np.size]
)
ptResult2=df1.pivot_table(
 values=['专科'],
 index=['专科数量分层'],
 columns=[],
 aggfunc=[np.size]
)
# # 各部门本科，专科数量分层，例如：0-9，本科数量在0-9的的主管部门有36个，专业数量在0-9的主管部门有18个
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# 学校数量分层和办学层级分布热力图
data = np.array([[36, 18], [15, 16], [22, 11], [8, 5], [1, 5],[0,4],[0,3],[1,0]])
axs[0].imshow(data)
axs[0].set_xticks(np.arange(len(["本科", "专科"])))
axs[0].set_yticks(np.arange(len(count_labels)))
axs[0].set_xticklabels(["本科", "专科"])
axs[0].set_yticklabels(count_labels)
plt.setp(axs[0].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
for i in range(len(count_labels)):
    for j in range(len(["本科", "专科"])):
        text = axs[0].text(j, i, data[i, j], ha="center", va="center", color="w")
axs[0].set_title("数量分层和办学层级分布热力图")

# 学校数量分层和办学层级分布气泡图
axs[1].scatter(data[:, 0], data[:, 1], s=data[:, 1] * 10)
axs[1].set_xlabel('专科')
axs[1].set_ylabel('本科')
axs[1].set_title("数量分层和办学层级分布气泡图")

plt.tight_layout()
plt.show()