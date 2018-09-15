import pandas as pd

casts=pd.read_csv('cast.csv',index_col=None)
print(casts.head())

titles=pd.read_csv('titles.csv',index_col=None)
print(titles.tail())#print(titles.tail(20))#mention number of lines
print(titles)#first 30 and last 30

pd.set_option('max_rows',10,'max_columns',10)
print(titles)
print(len(titles))

"""
•
read_csv
: read the data from the csv file.
•
index_col = None
: there is no index i.e. first column is data
•
head()
: show only first five elements of the DataFrame
•
tail()
: show only last five elements of the DataFrame


If there is some error while reading the file due to encoding, then try for following option as well,
titles = pd.read_csv('titles.csv', index_col=None, encoding='utf-8')

"""