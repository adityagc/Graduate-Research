#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:20:37 2018
Generate weights for linear regression
@author: adityagc
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection

#File path management
cwd = os.getcwd()
rel_inpath = os.path.join(cwd, '../Datasets/dataframe_raw.csv')
inpath = os.path.normpath(rel_inpath)
rel_outpath = os.path.join(cwd, '../Exploration/weights.png')
outpath = os.path.normpath(rel_outpath)
