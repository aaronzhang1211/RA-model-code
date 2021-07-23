# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:11:19 2021

@author: Aaron
"""


import numpy
from numpy import *
import numpy as np

a1j = [1,0,1,2,0]
a2j = [2,1,1,2,1]
a3j = [1,1,1,2,1]
a4j = [0,0,0,1,0]
a5j = [2,1,1,2,1]
A=np.array([a1j,a2j,a3j,a4j,a5j]) #把专家发达分结果建立初步的矩阵











Rstate = [] #定义各行元素排序重要性的排序指数ri

i = 0
for i in range (5):
    R=np.sum(A[i,:])
    i=i+1
    Rstate.append(R)
Rstate #用循环语句计算出ri，并赋予到数组内

Bcompare = np.c_[A,Rstate] #对初步的矩阵和排序指数矩阵进行汇合，形成暴露度指标的的比较矩阵Ai
Bcompare

rstatemax = np.max(Rstate)
rstatemin = np.min(Rstate)
rmax_min= rstatemax - rstatemin
rmax_min #极差法

#极差法构造判断矩阵
Cprevious = []

i = 0
for i in range (5):
    j = 0
    for j in range (5):
        c = 9**((Rstate[i]-Rstate[j])/rmax_min) 
        #c= round(c,2)
        j = j+1
        Cprevious.append(c)
    i = i+1
Cstate = np.array(
    [Cprevious[0:5],
     Cprevious[5:10],
     Cprevious[10:15],
     Cprevious[15:20],
     Cprevious[20:26]])
Cstate #将判断矩阵中的cij值返回到矩阵中

#算Mi
#计算Wi
#计算Wibar
Mstate = []
Wstate = []
Wstatebar = []
i = 0
for i in range (5):
    M = np.prod(Cstate[i,:])
    W = M**(1/5)
    #M = round(M,4)
    #W = round(W,2)
    i = i+1
    Mstate.append(M)
    Wstate.append(W)
Mstate
Wstate
SegamWstatej = np.sum(Wstate) #一维数组累计求和
Wstatebar = Wstate/SegamWstatej
Wstatebar = np.around(Wstatebar,2) #给一维数组保留两位小数，类似于round（）函数
Wstatebar #改数组既为所求的权重，后续进行一致性检验

#进行一致性检验λmax(umax代替)
#Cexposure矩阵和Wexporsurebar之间的运算
i = 0
cc = []
for i in range (5):
    aa = Wstatebar*Cstate[i,:]
    bb = np.sum(aa)
    cc.append(bb)
    i = i+1
cc = np.around(cc,2)
cc
umax = (1/5)*np.sum(cc/Wstatebar)
umax = round(umax,4)
umax

Ci = (umax-5)/4
Ci

Ri = 1.32

Cr = Ci/Ri

print('Wi(状态指标Stateindex)=',Wstatebar)


































