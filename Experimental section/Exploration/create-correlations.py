#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:20:37 2018
Generate correlation plots
@author: adityagc
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
#File path management
cwd = os.getcwd()
rel_inpath = os.path.join(cwd, '../Datasets/dataframe_raw.csv')
inpath = os.path.normpath(rel_inpath)
rel_outpath = os.path.join(cwd, '../Exploration/correlations.png')
outpath = os.path.normpath(rel_outpath)

#Plot config
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 18
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': 18})

with open(inpath,'rb') as f:
    df = pd.read_csv(f)
    del df['Unnamed: 0']
    out = df.corr()
    corrs = []
    for col in df:
        corrs.append(df[col].corr(df['bwt']))
    items = list(df.columns)
    plt.bar(items[:-1], corrs[:-1])
    plt.savefig(outpath)
