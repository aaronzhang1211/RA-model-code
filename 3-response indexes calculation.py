# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:11:19 2021

@author: Aaron
"""


import numpy
from numpy import *
import numpy as np

a1j = [1,1,2]
a2j = [1,1,0]
a3j = [0,1,2]
A=np.array([a1j,a2j,a3j]) #Build a preliminary matrix based on the results of the experts’ development

Rresponse = [] #The ranking index ri that defines the ranking importance of each row element

i = 0
for i in range (3):
    R=np.sum(A[i,:])
    i=i+1
    Rresponse.append(R)
Rresponse #Calculate ri with a loop statement and assign it to the array

Bcompare = np.c_[A,Rresponse] #Converge the preliminary matrix and the ranking index matrix to form a comparison matrix Ai of response indicators
Bcompare

rresponsemax = np.max(Rresponse)
rresponsemin = np.min(Rresponse)
rmax_min= rresponsemax - rresponsemin
rmax_min #Range method

#Range Method Constructing Judgment Matrix
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
Cresponse #Return the cij value in the judgment matrix to the matrix

#Count Mi
#Count Wi
#Count Wibar
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
SegamWresponsej = np.sum(Wresponse) #Cumulative sum of one-dimensional arrays
Wresponsebar = Wresponse/SegamWresponsej
Wresponsebar = np.around(Wresponsebar,2) #Reserve two decimal places for a one-dimensional array, similar to the round() function
Wresponsebar #Change the array to the desired weight, and then perform the consistency check

#Carry out consistency check λmax (umax instead)
#Operation between Cexposure matrix and Weexporsurebar
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

print('Wi(响应指标responseindex)=',Wresponsebar)


































