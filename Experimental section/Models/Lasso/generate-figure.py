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
rel_inpath = os.path.join(cwd, './Models/Lasso/lasso.csv')
inpath = os.path.normpath(rel_inpath)
rel_outpath = os.path.join(cwd, './Models/Lasso/lasso-path.png')
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
del df['intercept']
del df['penalty']
ms = df['mse']
del df['mse']
df.head()
x = df['log-penalty']
y = df['age1']
y1 = df['age2']

df.set_index('log-penalty').plot(linewidth=2.0, color=['black','black','black','red','red','red','green','green','blue','yellow','yellow','purple','orange','maroon','maroon','maroon'])
plt.legend(loc='upper right',bbox_to_anchor=(1.2,1))
plt.ylabel('Coefficients')
plt.savefig(outpath,papertype='ledger', bbox_inches='tight',orientation='landscape')
