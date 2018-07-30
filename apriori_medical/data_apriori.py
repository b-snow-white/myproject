# -*- coding: utf-8 -*-
"""
@time:2018/7/29 23:54

@author: BX
"""

#将离散化的数据变换成模型数据集
import os
import pandas as pd
#import numpy as np
datafile=os.path.join(os.getcwd(),'data')
inputfile=os.path.join(datafile,'data.xls')#待聚类的数据文件
outputfile=os.path.join(datafile,'data_apriori.xls')
data=pd.read_excel(inputfile)
d=data[data.columns[0]].astype(str)
for i in range(len(data)):
    if d[i]>str(0) and d[i]<=str(0.179):
        d[i]='A1'
    elif d[i]>str(0.179) and d[i]<=str(0.258):
        d[i]='A2'
    elif d[i]>str(0.258) and d[i]<=str(0.35):
        d[i]='A3'
    else:
        d[i]='A4'
d1=data[data.columns[1]].astype(str)
for i in range(len(data)):
    if d1[i]>str(0) and d1[i]<=str(0.15):
        d1[i]='B1'
    elif d1[i]>str(0.15) and d1[i]<=str(0.296):
        d1[i]='B2'
    elif d1[i]>str(0.296) and d1[i]<=str(0.485):
        d1[i]='B3'
    else:
        d1[i]='B4'
d2=data[data.columns[2]].astype(str)
for i in range(len(data)):
    if d2[i]>str(0) and d2[i]<=str(0.201):
        d2[i]='C1'
    elif d2[i]>str(0.201) and d2[i]<=str(0.288):
        d2[i]='C2'
    elif d2[i]>str(0.288) and d2[i]<=str(0.415):
        d2[i]='C3'
    else:
        d2[i]='C4'
d3=data[data.columns[3]].astype(str)
for i in range(len(data)):
    if d3[i]>str(0) and d3[i]<=str(0.172):
        d3[i]='D1'
    elif d3[i]>str(0.172) and d3[i]<=str(0.251):
        d3[i]='D2'
    elif d3[i]>str(0.251) and d3[i]<=str(0.357):
        d3[i]='D3'
    else:
        d3[i]='D4'
d4=data[data.columns[4]].astype(str)
for i in range(len(data)):
    if d4[i]>str(0) and d4[i]<=str(0.154):
        d4[i]='E1'
    elif d4[i]>str(0.154) and d4[i]<=str(0.256):
        d4[i]='E2'
    elif d4[i]>str(0.256) and d4[i]<=str(0.375):
        d4[i]='E3'
    else:
        d4[i]='E4'

d5=data[data.columns[5]].astype(str)
for i in range(len(data)):
    if d5[i]>str(0) and d5[i]<=str(0.178):
        d5[i]='F1'
    elif d5[i]>str(0.178) and d5[i]<=str(0.261):
        d5[i]='F2'
    elif d5[i]>str(0.261) and d5[i]<=str(0.353):
        d5[i]='F3'
    else:
        d5[i]='F4'
d6=data['TNM分期']
r=pd.concat((d,d1,d2,d3,d4,d5,d6),axis=1)#将各列数据连接
r.to_excel(outputfile)
#print(r)




