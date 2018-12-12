import pandas as pd
import numpy as np
import os

#Create dataframe
df = pd.read_csv('../Datasets/raw.csv')
#append bwt to end and delete logistic class
bwt = df['bwt']
del df['bwt']
del df['low']
del df['Unnamed: 0']
#Set datatypes to int
df['bwt'] = bwt
df['white'] = df['white'].astype(int)
df['black'] = df['black'].astype(int)
df['smoke'] = df['smoke'].astype(int)
df['ftv1'] = df['ftv1'].astype(int)
df['ftv2'] = df['ftv2'].astype(int)
df['ftv3m'] = df['ftv3m'].astype(int)
df['ptl1'] = df['ptl1'].astype(int)
df['ptl2m'] = df['ptl2m'].astype(int)
#Save processed dataframe as a pickle object
df.to_csv('../Datasets/dataframe_raw.csv')
