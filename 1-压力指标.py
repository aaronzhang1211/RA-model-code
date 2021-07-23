# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:11:19 2021

@author: Aaron
"""


import numpy
from numpy import *
import numpy as np

a1j = [1,2,2,1,0,0,0]
a2j = [0,1,0,2,1,1,2]
a3j = [0,2,1,1,0,0,2]
a4j = [1,0,1,1,0,0,1]
a5j = [2,1,2,2,1,1,2]
a6j = [2,1,2,2,1,1,2]
a7j = [2,0,0,1,0,0,1]









A=np.array([a1j,a2j,a3j,a4j,a5j,a6j,a7j]) #把专家发达分结果建立初步的矩阵

Rexposure = [] #定义各行元素排序重要性的排序指数ri

i = 0
for i in range (7):
    R=np.sum(A[i,:])
    i=i+1
    Rexposure.append(R)
Rexposure #用循环语句计算出ri，并赋予到数组内

Acompare = np.c_[A,Rexposure] #对初步的矩阵和排序指数矩阵进行汇合，形成暴露度指标的的比较矩阵Ai
Acompare

rexposuremax = np.max(Rexposure)
rexposuremin = np.min(Rexposure)
rmax_min= rexposuremax - rexposuremin
rmax_min #极差法

#极差法构造判断矩阵
Cprevious = []

i = 0
for i in range (7):
    j = 0
    for j in range (7):
        c = 9**((Rexposure[i]-Rexposure[j])/rmax_min) 
        c= round(c,2)
        j = j+1
        Cprevious.append(c)
    i = i+1
Cexposure = np.array(
    [Cprevious[0:7],
     Cprevious[7:14],
     Cprevious[14:21],
     Cprevious[21:28],
     Cprevious[28:35],
     Cprevious[35:42],
     Cprevious[42:49]])
Cexposure #将判断矩阵中的cij值返回到矩阵中

#算Mi
#计算Wi
#计算Wibar
Mexposure = []
Wexposure = []
Wexposurebar = []
i = 0
for i in range (7):
    M = np.prod(Cexposure[i,:])
    W = M**(1/7)
    M = round(M,4)
    W = round(W,2)
    i = i+1
    Mexposure.append(M)
    Wexposure.append(W)
Mexposure
Wexposure
SegamWexposurej = np.sum(Wexposure) #一维数组累计求和
Wexposurebar = Wexposure/SegamWexposurej
Wexposurebar = np.around(Wexposurebar,2) #给一维数组保留两位小数，类似于round（）函数
Wexposurebar #改数组既为所求的权重，后续进行一致性检验

#进行一致性检验λmax(umax代替)
#Cexposure矩阵和Wexporsurebar之间的运算
i = 0
cc = []
for i in range (7):
    aa = Wexposurebar*Cexposure[i,:]
    bb = np.sum(aa)
    cc.append(bb)
    i = i+1
cc = np.around(cc,2)
cc
umax = (1/7)*np.sum(cc/Wexposurebar)
umax = round(umax,4)
umax

Ci = (umax-7)/6
Ci

Ri = 1.32

Cr = Ci/Ri

print('Wi(压力指标Pressindex)=',Wexposurebar)


































