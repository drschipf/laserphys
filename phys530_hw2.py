#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:15:09 2017

@author: drschipf
"""
# PHYS 530 HW 1
import numpy as np
import math
import matplotlib
matplotlib.use('GTK')
import matplotlib.pyplot as plt

h = 6.625*10**(-34)
pi=3.1416
hbar = h/(2*pi)
eps0 = 8.854e-12
c= 2.998e8
e= 1.602e-19
m= 9.10938356e-31


plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
# WI = (1/(4*pi*eps0))^2*m*e^4/(2*hbar^2)
#
# fprintf('WI = %d\n',WI)
# Problem 2.1
#s = (4,7)
#lam = np.zeros(s)
#np.zeros(3,6)
#for npr in range(1,4):
#    for n in range(2,7):
#        if npr!=n:
#            lam[npr,n] = (4*pi*eps0)**2*(4*pi*hbar**3*c/(m*e**4))*(n**2*npr**2/(n**2-npr**2))

#print('np=2, n=3 gives lambda = ',lam[2,3])



