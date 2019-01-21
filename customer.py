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
rating=[]

def get_rating():
    print('enter the ratings in range 1 to 10')
    for i in range(1,10):
        
        print('enter the rating for question%d'%(i))
        a=int(input())
        if a<=10 and a>0:           
            rating.append(a)
        else:
            raise Exception('invalid rating.enter a value between 1 and 10')
    return rating

print(get_rating())