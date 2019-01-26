# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 10:26:30 2019

@author: Malavika  Sreekumar
"""
def checkprime(num):
    print(num)
    
a=int(input("Enter no1:"))
b=int(input("Enter no2:"))

                
def checkingprime(a,b):             
        for num in range(a,b+1):
            for i in range(2,num):
                if (num%i==0):
                    break
            else:
                    checkprime(num)
                                 
                
checkingprime(a,b)                
                
