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

reader = Reader(line_format='user item rating', sep=' ', skip_lines=3, rating_scale=(1, 5))

data=Dataset.load_from_file('names.csv',reader=reader)
algo=SVD() #using the SVD algorithm
cross_validate(algo,data,measures=['RMSE','MAE'],cv=5,verbose=True)
