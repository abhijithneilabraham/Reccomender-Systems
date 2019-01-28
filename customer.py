#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:13:07 2019

@author: abhijithneilabraham
"""

import random


x=[]

def get_id(n):
    print('enter all the customer ids')
    for i in range (n):
        x.append(input())
    return x

'''
print(get_id(m))  
'''
rating=[]
r=int(input('enter the number of ratings'))

'''
print('enter the ratings in range 1 to 10')#Let this print statement stay here for future uses when I dont use random numbers
'''
for i in range(r):
    '''
    print('enter the rating for question%d'%(i))
    '''
    a=random.randint(1,10) #generating random values for ratings for testing purposes
    if a<=10 and a>0:           
        rating.append(a)
    else:
        raise Exception('invalid rating.enter a value between 1 and 10')

'''
print(get_rating())
'''
print('enter the number of customers')
m=int(input())

id=get_id(m)
mf=[]
rat=[]
id_cust=[]
for customer in range(m):
     #for getting array of customer id.mulitplied by 10 to match with the column of ratings
    
    rat.append(rating) #for getting a full array of ratings with number of elements=10*number of customers
    mf.append([random.randint(0,1)]*10) #male or female random generator
print(id_cust,mf,rat)

import csv
'''
with open("customerdataset.csv","w+") as my_csv:
    csvWriter=csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(details)

'''
    

with open('names.csv', 'w') as csvfile:
    fieldnames = ['id', 'male_or_female']
    for _ in range(r):
        fieldnames.append('question'+str(_+1))
        
            
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in range(m):
        for v in range(r):
            dic={'id':id[i],'male_or_female':random.randint(0,1)}
            dic['question'+str(v+1)]=random.randint(1,10)
        
        writer.writerow(dic)
'''
wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')
for x in id_cust : wtr.writerow ([x])   
for x in id_cust : wtr.writerow ([x])  
'''
        
    