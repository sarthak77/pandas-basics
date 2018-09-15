import pandas as pd
titles=pd.read_csv('titles.csv',index_col=None)
print(titles)
print(titles['title'])#column selecting
print(titles.ix[2])#row selecting