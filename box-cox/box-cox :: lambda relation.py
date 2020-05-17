import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df_trans = pd.DataFrame({'x':np.arange(0.1, 5.1, 0.1)})

print(df_trans)

list_lambda = [-2, -1, -0.5, 0, 0.5, 1, 2]
for i, i_lambda in enumerate(list_lambda):
    df_trans[ 'y'+str(i) ] = stats.boxcox( df_trans.x, lmbda = i_lambda )

fig, ax = plt.subplots()
ax.plot(df_trans.x, df_trans.y0, color='darkblue',  label="lambda="+str(list_lambda[0]))
ax.plot(df_trans.x, df_trans.y1, color='mediumblue',label="lambda="+str(list_lambda[1]))
ax.plot(df_trans.x, df_trans.y2, color='skyblue',   label="lambda="+str(list_lambda[2]))
ax.plot(df_trans.x, df_trans.y3, color='green',label="lambda="+str(list_lambda[3]))
ax.plot(df_trans.x, df_trans.y4, color='salmon',    label="lambda="+str(list_lambda[4]))
ax.plot(df_trans.x, df_trans.y5, color='red',       label="lambda="+str(list_lambda[5]))
ax.plot(df_trans.x, df_trans.y6, color='darkred',   label="lambda="+str(list_lambda[6]))
ax.legend()
ax.set_title('y = Box-Cox( x, labmda )')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.ylim(-10, 10)
plt.grid()
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.1, top=0.9)
plt.show()
fig.savefig('lambda.png')