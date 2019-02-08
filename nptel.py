# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:20:06 2019

@author: Malavika  Sreekumar
"""

def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/4,d+1)
    return(d)
    
print(f(255))




def h(n):
    s = 0
    for i in range(1,n):
        if n%i == 0:
           s = s+i
    return(s)
    
print(h(28)-h(27))



def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m-n)
    return(res)
    
print(58/4)