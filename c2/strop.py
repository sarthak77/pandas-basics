import pandas as pd
t=pd.read_csv('titles.csv',index_col=None)

#search
print(t[t['title']=='Maa'])
print(t[t['title'].str.startswith("Maa")])

#count
print(t['year'].value_counts())

#plot
import matplotlib.pyplot as plt
x=t['year'].value_counts()
x=x.sort_index()
x.plot()
plt.show()