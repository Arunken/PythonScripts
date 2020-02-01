# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the dataset
fpath = "/mnt/Soft/Documents/SourceCodes/Python Advanced/10_scikit-learn/datasets/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data.csv"
dataset = pd.read_csv(fpath)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
x[:,0] = labelencoder_X.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])# for creating dummy variable
x = onehotencoder.fit_transform(x).toarray()# creating dummy variables for indep categorical variables

labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)

# Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)# 20% observations in the testset and 80% observations in the training set

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)













