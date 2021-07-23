# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:11:19 2021

@author: Aaron
"""


import numpy
from numpy import *
import numpy as np

a1j = [1,0,2]
a2j = [2,1,2]
a3j = [0,0,1]
A=np.array([a1j,a2j,a3j]) #把专家发达分结果建立初步的矩阵

Rresponse = [] #定义各行元素排序重要性的排序指数ri

i = 0
for i in range (3):
    R=np.sum(A[i,:])
    i=i+1
    Rresponse.append(R)
Rresponse #用循环语句计算出ri，并赋予到数组内

Bcompare = np.c_[A,Rresponse] #对初步的矩阵和排序指数矩阵进行汇合，形成暴露度指标的的比较矩阵Ai
Bcompare

rresponsemax = np.max(Rresponse)
rresponsemin = np.min(Rresponse)
rmax_min= rresponsemax - rresponsemin
rmax_min #极差法

#极差法构造判断矩阵
Cprevious = []

i = 0
for i in range (3):
    j = 0
    for j in range (3):
        c = 9**((Rresponse[i]-Rresponse[j])/rmax_min) 
        c= round(c,2)
        j = j+1
        Cprevious.append(c)
    i = i+1
Cresponse = np.array(
    [Cprevious[0:3],
     Cprevious[3:6],
     Cprevious[6:10]])
Cresponse #将判断矩阵中的cij值返回到矩阵中

#算Mi
#计算Wi
#计算Wibar
Mresponse = []
Wresponse = []
Wresponsebar = []
i = 0
for i in range (3):
    M = np.prod(Cresponse[i,:])
    W = M**(1/3)
    M = round(M,4)
    W = round(W,2)
    i = i+1
    Mresponse.append(M)
    Wresponse.append(W)
Mresponse
Wresponse
SegamWresponsej = np.sum(Wresponse) #一维数组累计求和
Wresponsebar = Wresponse/SegamWresponsej
Wresponsebar = np.around(Wresponsebar,2) #给一维数组保留两位小数，类似于round（）函数
Wresponsebar #改数组既为所求的权重，后续进行一致性检验

#进行一致性检验λmax(umax代替)
#Cexposure矩阵和Wexporsurebar之间的运算
i = 0
cc = []
for i in range (3):
    aa = Wresponsebar*Cresponse[i,:]
    bb = np.sum(aa)
    cc.append(bb)
    i = i+1
cc = np.around(cc,2)
cc
umax = (1/3)*np.sum(cc/Wresponsebar)
umax = round(umax,4)
umax

Ci = (umax-3)/2
Ci

Ri = 1.32

Cr = Ci/Ri

print('Wi(准则层对目标层的权重)=',Wresponsebar)


































