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
from sklearn import preprocessing, model_selection, linear_model as lm, metrics as ms

#File path management
cwd = os.getcwd()
rel_inpath = os.path.join(cwd, './Datasets/dataframe_raw.csv')
inpath = os.path.normpath(rel_inpath)
rel_outpath = os.path.join(cwd, './Models/Ridge/ridge-reg-metrics.txt')
outpath = os.path.normpath(rel_outpath)
#Number of cross-validations:
num_cv = 4
#Linear model
with open(inpath,'rb') as f:
    df = pd.read_csv(f)
    del df['Unnamed: 0']
    data = df.values
    X = data[:,0:-1]
    Y = data[:,16]
    alphas = [0.001, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    wts = []
    mse_out = []
    for alpha in alphas:
        mse_arr = []
        weights_arr = []
        for i in range(num_cv):
            X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.25)
            regr = lm.Ridge(alpha=alpha)
            regr.fit(X_train, Y_train)
            Y_pred = regr.predict(X_test)
            mse = ms.mean_squared_error(Y_test, Y_pred)
            weights = np.append(np.asarray(regr.coef_), regr.intercept_)
            mse_arr.append(mse)
            weights_arr.append(weights)
        mean_mse = np.mean(mse_arr)
        wts_arr = np.asarray(weights_arr)
        mean_weights = np.mean(wts_arr, axis=0)
        wts.append(list(mean_weights))
        mse_out.append(mean_mse)
    wts_out = np.asarray(wts).T
    with open(outpath, 'w') as f1:
        f1.write('Alphas: '+'\n')
        f1.write( str(alphas) + '\n')
        f1.write('Weights \n')
        np.savetxt(f1, wts_out)
        f1.write('MSE \n')
        f1.write(str(mse_out))
