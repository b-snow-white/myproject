# -*- coding: utf-8 -*-
"""
@time:2018/7/29 17:34

@author: BX
"""
#数据有73个属性，首先剔除掉冗余属性和不相关属性,剩余6种证型得分，TNM分期的属性值
from __future__ import print_function
import os
import pandas as pd
from sklearn.cluster import KMeans #导入k均值算法
datafile=os.path.join(os.getcwd(),'data')
inputfile=os.path.join(datafile,'data.xls')#待聚类的数据文件
disresultfile=os.path.join(datafile,'disresult.xls')#离散化数据
centerresultfile=os.path.join(datafile,'cenresult.xls')#离散化中心结果数据
aprioridatafile=os.path.join(datafile,'apriori_data.xls')
typelabel={'肝气郁结证型系数':'A','热毒蕴结证型系数':'B','冲任失调证型系数':'C','气血两虚证型系数':'D',
           '脾胃虚弱证型系数':'E','肝肾阴虚证型系数':'F'}
#对6种证型进行离散化
k=4#需要聚成4个类别
#读取数据进行聚类分析
data=pd.read_excel(inputfile)#读取数据
keys=list(typelabel.keys())
result=pd.DataFrame()
center=pd.DataFrame()
model_data=pd.DataFrame()
if __name__=='__main__':#当作主窗口运行
    for i in range(len(keys)):
        #调用k均值算法，进行聚类离散化
        print('正在进行%s的聚类'%keys[i])
        kmodel=KMeans(n_clusters=k,n_jobs=1)#n_jobs是并行数，一般等于CPU数比较好
        kmodel.fit(data[[keys[i]]].as_matrix())#训练模型
        r1=pd.DataFrame(kmodel.cluster_centers_,columns=[typelabel[keys[i]]])
        data_apiori=[typelabel[keys[i]] + str(j) for j in kmodel.labels_]
        r3=pd.DataFrame(data_apiori,columns=[keys[i]],index=data.index)
        #print([typelabel[keys[i]]+str(j) for j in r3[typelabel[keys[i]]]])
        #print(r3)
        model_data=model_data.append(r3.T)
        #聚类中心

        center=center.append(r1.T)

        r2=pd.Series(kmodel.labels_).value_counts()#分类统计
        r2=pd.DataFrame(r2,columns=[typelabel[keys[i]]+'n'])
        r=pd.concat([r1,r2],axis=1).sort_values(typelabel[keys[i]])#匹配聚类中心和累呗数目
        r.index=[1,2,3,4]
        r[typelabel[keys[i]]]=pd.rolling_mean(r[typelabel[keys[i]]],2)
        r[typelabel[keys[i]]][1]=0.0
        result=result.append(r.T)
    model_data=pd.concat([model_data.T,data['TNM分期'].T],axis=1)#将TNM分期添加到model_data
    result=result.sort_index()
    result.to_excel(disresultfile)#生成聚类结果
    center.to_excel(centerresultfile)#生成聚类中心数据集
    print(center)
    model_data.to_excel(aprioridatafile)#生成建模数据集
#print(pd.DataFrame(center))
#print(model_data)

#模型构建
import os
from _Apriori import *
datafile=os.path.join(os.getcwd(),'data')
import time#导入时间库用来计算用时
inputfile=os.path.join(datafile,r'data_apriori.xls')
data=pd.read_excel(inputfile)
start=time.clock()#开始计时
print('转换原始数据至0-1矩阵...')
ct=lambda x:pd.Series(1,index=x[pd.notnull(x)])#转换0-1矩阵的过度函数
b=map(ct,data.as_matrix())#用map方式执行
#print(len(list(b)))
data=pd.DataFrame(list(b)).fillna(0)#实现矩阵转换，空值填充为0
end=time.clock()#计时结束
print('转换完毕，用时:%0.2f秒'%(end-start))
del b#删除中间变量，节省内存
support=0.06#最小支持度
confidence=0.75#最小置信度
ms='---'#连接符,默认为--，用来区分不同元素
start=time.clock()#计时开始
print('开始搜索关联规则...')
find_rule(data,support,confidence,ms)
end=time.clock()#计时结束
print('搜索完成，用时：%0.2f秒'%(end-start))










