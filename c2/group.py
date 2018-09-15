import pandas as pd
import matplotlib.pyplot as plt

t=pd.read_csv('titles.csv',index_col=None)

a=t.groupby(['year']).size()
print(a)
a.plot()
plt.show()