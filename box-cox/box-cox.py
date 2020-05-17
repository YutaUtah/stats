import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

fig = plt.figure(figsize=(6.0, 6.0))

list_lambda = [-2, -1, -0.5, 0, 0.5, 1, 2]
for i, i_lambda in enumerate(list_lambda):
    df[ 'val_'+str(i) ] = stats.boxcox( df.val, lmbda = i_lambda )
    fig.add_subplot(4, 2, i+1).hist(df['val_'+str(i)], bins=20, color='r', alpha=0.5, density=True)
    plt.title("lambda="+str(list_lambda[i]))
    plt.xlabel('val')
    plt.ylabel('density')

df[ 'val_auto' ], best_lambda = stats.boxcox( df.val )
fig.add_subplot(4, 2, 8).hist(df['val_auto'], bins=20, color='r', alpha=0.5, density=True)
plt.title("lambda="+str(round(best_lambda, 2)))
plt.xlabel('val')
plt.ylabel('density')

fig.tight_layout()
fig.show()
plt.show()