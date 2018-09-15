import pandas as pd
import matplotlib.pyplot as plt

c=pd.read_csv('cast.csv',index_col=None)

a=c.set_index(['title'])#set tile as index
print(a)#use reset_index for resetting