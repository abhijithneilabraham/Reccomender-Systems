#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:13:07 2019

@author: abhijithneilabraham
"""
x=[]

def get_id(n):
    print('enter all the customer ids')
    for i in range (n):
        x.append(input())
    return x
print('enter the number of customers')
m=int(input())
'''
print(get_id(m))  
'''
