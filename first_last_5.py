# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:34:09 2019

@author: Malavika  Sreekumar
"""

#Write a Python program to generate and print a list except for the first 5 and last 5 elements, 
#where the values are square of numbers between 1 and 30 (both included).

def square_list(a):
    li=[]
    for i in range(6,a-4):
        li.append(i**2)
    print(li)
    
a=int(input("Enter a no greater than 6:"))
square_list(a)
        