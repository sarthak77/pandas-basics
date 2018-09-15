import pandas as pd
import matplotlib.pyplot as plt

c=pd.read_csv('cast.csv',index_col=None)
r=pd.read_csv('release_dates.csv',index_col=None)

ca=c[c['title']=='Amelia']
print(ca)
print(ca.merge(r))