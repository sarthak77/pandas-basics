import pandas as pd
titles=pd.read_csv('titles.csv',index_col=None)

after85=titles[titles['year']>1985]
print(after85)
movies90=titles[(titles['year']>=1990) & (titles['year']<2000)]
print(movies90)