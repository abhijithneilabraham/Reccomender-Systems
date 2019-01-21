#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 22:41:05 2019

@author: abhijithneilabraham
"""
q1=''
q2=''
q3=''
q4=''
q5=''
q6=''
q7=''
id1=input()
id2=input()
id3=input()
id4=input()
id5=input()
def customer_details():
    
customer={1:id1,2:id2a,3:id3,4:id4,5:id5}
import random
questions={q1:random.randint(1,10),q2:random.randint(1,10),q3:random.randint(1,10),q4:random.randint(1,10),q5:random.randint(1,10),q6:random.randint(1,10),q7:random.randint(1,10)}
M_F=random.randint(0,1)
customer_data={}
import csv
csv_columns={'number','id','rating','M/F'}
with open('customer.csv','w') as writeFile:
     writer = csv.DictWriter()
     writer.writerows(lines)