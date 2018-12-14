import pandas as pd
import os
import matplotlib.pyplot as plt
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 15
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': 18})
from matplotlib.font_manager import FontProperties
from matplotlib import pylab
fontP = FontProperties()
fontP.set_size('small')

cwd = os.getcwd()
rel_inpath = os.path.join(cwd, './Models/Elastic Net/elastic_net.csv')
inpath = os.path.normpath(rel_inpath)
rel_outpath = os.path.join(cwd, './Models/Elastic Net/mse-lambda-elastic_net.png')
outpath = os.path.normpath(rel_outpath)

import pandas as pd
import matplotlib.pyplot as plt
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 15
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': 18})
from matplotlib.font_manager import FontProperties
from matplotlib import pylab
fontP = FontProperties()
fontP.set_size('small')
df = pd.read_csv(inpath)
x = df['log-penalty']
y = df['mse']
plt.plot(x,y)
plt.legend(loc='upper right',bbox_to_anchor=(1.2,1))
plt.ylabel('Mean squared error')
plt.xlabel('log-penalizing coefficient')
plt.savefig(outpath,papertype='ledger', bbox_inches='tight',orientation='landscape')
