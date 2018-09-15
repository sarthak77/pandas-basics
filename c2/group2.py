import pandas as pd
import matplotlib.pyplot as plt

c=pd.read_csv('cast.csv',index_col=None)

cf=c[c['name']=='Aaron Abrams']
a=cf.groupby(['year']).size()
print(a)

b=cf.groupby(['year','title']).size()
print(b)

print(c.groupby(['year']).n.max())#similarly min and mean


#group by custom filter
decade=c['year']//10#// is used for int division
print(decade)
x=c.groupby(decade).n.size()
print(x)