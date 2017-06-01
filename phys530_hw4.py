# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:08:26 2017

@author: David
"""

# PHYS 530 HW 4
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

sv = 1
kv = 1

Iv = sv/kv*(1-e**(-kv*L))

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
# WI = (1/(4*pi*eps0))^2*m*e^4/(2*hbar^2)
#
# fprintf('WI = %d\n',WI)