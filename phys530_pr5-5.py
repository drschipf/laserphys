# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:11:00 2017

@author: drschipf
"""
from matplotlib import pyplot
import numpy as np
s= 0.04
t = np.linspace(0,1,10)
gol = [0.1, 1.0, 30.0]
fig = pyplot.figure()
# pyplot.legend(loc='lower right')

for i in range(len(gol)):
    Ivo_div_Ivsat = gol[i]*t/(t+s) - t/2
    pyplot.plot(t,Ivo_div_Ivsat)
    
pyplot.xlabel('Output Coupling t')
pyplot.ylabel('Ivout/Ivsat')

