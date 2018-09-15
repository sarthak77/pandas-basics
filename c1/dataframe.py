"""
DataFrame is the widely used data structure of pandas. Note that, Series are used to work with one dimensional
array, whereas DataFrame can be used with two dimensional arrays.  DataFrame has two different index i.e.
column-index and row-index.
"""
import pandas as pd

data={'name':['AA','ibm','efede'],
      'date':['2001-12-1','2012-2-12','2010-04-09'],
      'shares':[100,30,90] }
df=pd.DataFrame(data)
print(df)
df['owner']='unknown'
print(df)
#Currently, the row index are set to 0, 1 and 2. These can be changed using ‘index’ attribute as below
df.index=['one','two','three']
print(df)
#Further, any column of the DataFrame can be set as index using ‘set_index()’ attribute, as shown below
df=df.set_index(['name'])
print(df)

#Accessing data
print(df['shares'])#column index
print(df.ix['AA'])#row index
print(df.ix[1][0])#index

#Any column can be deleted using ‘del’ or ‘drop’ commands,
del df['owner']
print(df)