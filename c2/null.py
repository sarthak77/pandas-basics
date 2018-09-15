import pandas as pd
c=pd.read_csv('cast.csv',index_col=None)

print(c.ix[3:4])
print(c['n'].isnull().head())#check null values
#‘notnull’ is opposite of isnull, it returns true for not null values,

print(c[c['n'].isnull()].head(3))

#fill null values
c_fill = c[c['n'].isnull()].fillna('NA')
print(c_fill.head(10))