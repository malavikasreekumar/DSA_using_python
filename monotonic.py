# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:27:59 2019

@author: Malavika  Sreekumar
"""

values=input()

def monotonic(values):
    for i in range(0,len(values)-1):
        if values[i]>=values[i+1] or values[i]<=values[i+1]:
            return True
        else:
            return False
        
m=monotonic(values)
print(m)