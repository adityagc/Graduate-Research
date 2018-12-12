#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:20:37 2018
Generate arrays of min and max values from dataframe for alm file.
@author: adityagc
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
#File path management
cwd = os.getcwd()
rel_inpath = os.path.join(cwd, '../Datasets/dataframe_raw.csv')
inpath = os.path.normpath(rel_inpath)
rel_outpath_max = os.path.join(cwd, '../Datasets/maxarr.csv')
maxpath = os.path.normpath(rel_outpath_max)
rel_outpath_min = os.path.join(cwd, '../Datasets/minarr.csv')
minpath = os.path.normpath(rel_outpath_min)

with open(inpath,'rb') as f:
    df = pd.read_csv(f)
    del df['Unnamed: 0']
    maxvals = df.max()
    maxarr = maxvals.values
    np.savetxt(maxpath, maxarr, newline=" ")
    minvals = df.min()
    minarr = minvals.values
    np.savetxt(minpath, minarr, newline=" ")
