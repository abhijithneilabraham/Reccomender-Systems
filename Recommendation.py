#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 00:08:44 2019

@author: abhijithneilabraham
"""

from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise import Reader
import pandas as pd
customer=pd.read_csv('names.csv')

reader = Reader(line_format='user item rating',rating_scale=(1, 5),sep=',')
fieldnames = ['id', 'male_or_female']

for i in range(25):
    fieldnames.insert(2,'question'+str(i+1))

    data = Dataset.load_from_df(customer[fieldnames], reader)
    del fieldnames[2]
    
   
    algo=SVD() #using the SVD algorithm
    cross_validate(algo,data,measures=['RMSE','MAE'],cv=5,verbose=True)
