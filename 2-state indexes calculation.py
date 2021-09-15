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
A=np.array([a1j,a2j,a3j,a4j,a5j]) #Build a preliminary matrix based on the results of the experts’ development











Rstate = [] #The ranking index ri that defines the ranking importance of each row element

i = 0
for i in range (5):
    R=np.sum(A[i,:])
    i=i+1
    Rstate.append(R)
Rstate #Calculate ri with a loop statement and assign it to the array

Bcompare = np.c_[A,Rstate] #Converge the preliminary matrix and the ranking index matrix to form a comparison matrix Ai of state indicators
Bcompare

rstatemax = np.max(Rstate)
rstatemin = np.min(Rstate)
rmax_min= rstatemax - rstatemin
rmax_min #Range method

#Range Method Constructing Judgment Matrix
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
Cstate #Return the cij value in the judgment matrix to the matrix

#Count Mi
#Count Wi
#Count Wibar
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
SegamWstatej = np.sum(Wstate) #Cumulative sum of one-dimensional arrays
Wstatebar = Wstate/SegamWstatej
Wstatebar = np.around(Wstatebar,2) #Reserve two decimal places for a one-dimensional array, similar to the round() function
Wstatebar #Change the array to the desired weight, and then perform the consistency check

#Carry out consistency check λmax (umax instead)
#Operation between Cexposure matrix and Weexporsurebar
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


































