import pandas as pd
c=pd.read_csv('cast.csv',index_col=None)
c=c[c['name']=='Aaron Abrams']
a=c.merge(c,on=['title','year'])
#a=a[a['name_y']!='Aaron Abrams']
print(a)