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









A=np.array([a1j,a2j,a3j,a4j,a5j,a6j,a7j]) #Build a preliminary matrix based on the results of the experts’ development

Rexposure = [] #The ranking index ri that defines the ranking importance of each row element

i = 0
for i in range (7):
    R=np.sum(A[i,:])
    i=i+1
    Rexposure.append(R)
Rexposure #Calculate ri with a loop statement and assign it to the array

Acompare = np.c_[A,Rexposure] #Converge the preliminary matrix and the ranking index matrix to form a comparison matrix Ai of exposure indicators
Acompare

rexposuremax = np.max(Rexposure)
rexposuremin = np.min(Rexposure)
rmax_min= rexposuremax - rexposuremin
rmax_min #Range method

#Range Method Constructing Judgment Matrix
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
Cexposure #Return the cij value in the judgment matrix to the matrix

#Count Mi
#Count Wi
#Count Wibar
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
SegamWexposurej = np.sum(Wexposure) #Cumulative sum of one-dimensional arrays
Wexposurebar = Wexposure/SegamWexposurej
Wexposurebar = np.around(Wexposurebar,2) #Reserve two decimal places for a one-dimensional array, similar to the round() function
Wexposurebar #Change the array to the desired weight, and then perform the consistency check

#Carry out consistency check λmax (umax instead)
#Operation between Cexposure matrix and Weexporsurebar
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


































