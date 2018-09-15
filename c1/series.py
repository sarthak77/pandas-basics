"""
The Series is a one-dimensional array that can store various data types, including mix data types. The row labels
in a Series are called the index. Any list, tuple and dictionary can be converted in to Series using ‘series’ method
as shown below
"""
import pandas as pd
#tuple
h=('ds',100,23,'wdwd21212')#default indedx 0,1,2..
s=pd.Series(h)
print(s)

#provide index in tuples
#f=('eer',23,'wdwd')
#f=pd.Series(f,index=['ddde','eededd','ededed'])

#dict
d={'name':'ibm','date':'2010-09-08'}
ds=pd.Series(d)
print()
print(ds)

"""
Elements of the Series can be accessed using index name e.g. f[‘shares’] or f[0] in below code. Further, specific
elements can be selected by providing the index in the list,
"""