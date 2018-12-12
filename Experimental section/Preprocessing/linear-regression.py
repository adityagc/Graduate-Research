#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:20:37 2018
Generate weights for linear regression
@author: adityagc
"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection, linear_model as lm

#File path management
cwd = os.getcwd()
rel_inpath = os.path.join(cwd, '../Datasets/dataframe_raw.csv')
inpath = os.path.normpath(rel_inpath)
rel_outpath = os.path.join(cwd, '../Exploration/weights.png')
outpath = os.path.normpath(rel_outpath)

#Linear model
with open(inpath,'rb') as f:
    df = pd.read_csv(f)
    del df['Unnamed: 0']
    data = df.values
    X = preprocessing.MinMaxScaler(feature_range=(-1,+1)).fit_transform(data[:,0:-1])
    Y = preprocessing.MinMaxScaler().fit_transform(data[:,16].reshape(-1,1))
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.25)
    regr = lm.LinearRegression()
    regr.fit(X_train, Y_train)
    Yhat = regr.predict(X_test)
