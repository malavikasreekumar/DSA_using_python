# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:56:25 2019

@author: Malavika  Sreekumar
"""

sum=0
a=int(input("Enter lower range:"))
b=int(input("Enter upper range:"))

for i in range(a,b+1):
    sum=sum+i
    
print("The sum of nos from {} to {} is {}:".format(a,b,sum))    