#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 01:06:10 2019

@author: abhijithneilabraham
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
dataset = pd.read_csv("ml-100k/u.data",sep='\t',names="user_id,item_id,rating,timestamp".split(","))
print(dataset.head(5)) 
dataset.user_id=dataset.user_id.astype('category').cat.codes.values
dataset.item_id = dataset.item_id.astype('category').cat.codes.values
from sklearn.model_selection import train_test_split
train, test = train_test_split(dataset, test_size=0.2)
print(train.head())
'''
Matrix factorisation
One popular recommender systems approach is called Matrix Factorisation.
 It works on the principle that we can learn a low-dimensional representation (embedding) of user and movie.
 For example, for each movie, we can have how much action it has, how long it is, and so on.
 For each user, we can encode how much they like action, or how much they like long movies, etc.
 Thus, we can combine the user and the movie embeddings to estimate the ratings on unseen movies. 
 This approach can also be viewed as: given a matrix (A [M X N]) containing users and movies, 
we want to estimate low dimensional matrices (W [M X k] and H [M X k]), such that: A≈W.HT
'''

import keras
from IPython.display import SVG
from keras.optimizers import Adam