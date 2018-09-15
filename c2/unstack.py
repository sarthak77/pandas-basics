import pandas as pd
import matplotlib.pyplot as plt

c=pd.read_csv('cast.csv',index_col=None)

cd=c.groupby(['type',c['year']//10]).size()
print(cd)
print(cd.unstack())
cd.unstack(0).plot(kind='bar')#default is unstack(-1)
plt.show()


