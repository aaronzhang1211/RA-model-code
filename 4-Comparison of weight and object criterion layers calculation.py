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
A=np.array([a1j,a2j,a3j]) #Build a preliminary matrix based on the results of the experts’ development

Rlayer = [] #The ranking index ri that defines the ranking importance of each row element

i = 0
for i in range (3):
    R=np.sum(A[i,:])
    i=i+1
    Rlayer.append(R)
Rlayer #Calculate ri with a loop statement and assign it to the array

Bcompare = np.c_[A,Rlayer] #Converge the preliminary matrix and the ranking index matrix to form a comparison matrix Ai of layers
Bcompare

rlayermax = np.max(Rlayer)
rlayermin = np.min(Rlayer)
rmax_min= rlayermax - rlayermin
rmax_min #Range method

#Range Method Constructing Judgment Matrix
Cprevious = []

i = 0
for i in range (3):
    j = 0
    for j in range (3):
        c = 9**((Rlayer[i]-Rlayer[j])/rmax_min) 
        c= round(c,2)
        j = j+1
        Cprevious.append(c)
    i = i+1
Clayer = np.array(
    [Cprevious[0:3],
     Cprevious[3:6],
     Cprevious[6:10]])
Clayer #Return the cij value in the judgment matrix to the matrix

#Count Mi
#Count Wi
#Count Wibar
Mlayer = []
Wlayer = []
Wlayerbar = []
i = 0
for i in range (3):
    M = np.prod(Clayer[i,:])
    W = M**(1/3)
    M = round(M,4)
    W = round(W,2)
    i = i+1
    Mlayer.append(M)
    Wlayer.append(W)
Mlayer
Wlayer
SegamWlayerj = np.sum(Wlayer) #Cumulative sum of one-dimensional arrays
Wlayerbar = Wlayer/SegamWlayerj
Wlayerbar = np.around(Wlayerbar,2) #Reserve two decimal places for a one-dimensional array, similar to the round() function
Wlayerbar #Change the array to the desired weight, and then perform the consistency check

#Carry out consistency check λmax (umax instead)
#Operation between Clayer matrix and Wexlayerbar
i = 0
cc = []
for i in range (3):
    aa = Wlayerbar*Clayer[i,:]
    bb = np.sum(aa)
    cc.append(bb)
    i = i+1
cc = np.around(cc,2)
cc
umax = (1/3)*np.sum(cc/Wlayerbar)
umax = round(umax,4)
umax

Ci = (umax-3)/2
Ci

Ri = 1.32

Cr = Ci/Ri

print('Wi(准则层对目标层的权重)=',Wresponsebar)


































