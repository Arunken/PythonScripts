#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:49:06 2018

@author: arken
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the dataset
fpath = "/mnt/Soft/Documents/SourceCodes/Python Advanced/10_scikit-learn/datasets/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data.csv"
dataset = pd.read_csv(fpath)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)# 20% observations in the testset and 80% observations in the training set

'''
# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''












