# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:06:49 2019

@author: Malavika  Sreekumar
"""
fact=1

a=int(input("Enter a no:"))

if a<0:
    print("No facorial for -ve nos")
if a==0:
    print("Factorial of 0 is 1") 
else:    

    for i in range(1,a+1):
        fact=fact*i
        
    print("The Factorial of {} is {}".format(a,fact))
    
    