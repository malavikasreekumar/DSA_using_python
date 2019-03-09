# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:15:25 2019

@author: Malavika  Sreekumar
"""

def valley(l):
    for i in range(1,len(l)):
        if l[i]<l[i-1] and l[i]>l[i+1]:
            continue
        elif l[i]<l[i-1] and i==len(l):
            return False
            
        elif l[i]<l[i+1] and l[i]<l[i-1]:
            #min=l[i]
            j=i
            
            for m in range(j,len(l)):
                if l[m]<l[m+1]:
                    return True
                else:
                    return False
            
        else:
            return False
        
l = [int(x) for x in input().split()]
v=valley(l)
print(len(l))
print(v)
                
            