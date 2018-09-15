import pandas as pd
titles=pd.read_csv('titles.csv',index_col=None)

a=titles.sort_index()#sort by index default
print(a)

b=titles.sort_values('year')#sort by value
print(b)