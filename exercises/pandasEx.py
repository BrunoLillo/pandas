
import pandas as pd
#1
"""
Write a Pandas program to create and 
display a one-dimensional array-like object containing an array of 
data using Pandas module.
"""
ds = pd.Series(['1','2','3','4','5','6'])
#print(df)
"""
#2
Write a Pandas program to convert a Panda module 
Series to Python list and it's type."""
lista= ds.tolist()
#print(type(lista))

""" #3
Write a Pandas program to add, subtract, multiple and divide two Pandas
Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])
soma = s1+s2
sub = s1-s2
mul = s1*s2
div = s1/s2
#print(f'SOMA:{soma} SUB:{sub} Multi{mul} DIV:{div}')

""" #4
Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
"""
ss1= pd.Series([2, 4, 6, 8, 10])
ss2= pd.Series([1, 3, 5, 7, 10])

compare = ss1==ss2
#print(f'Compare:{compare}')

""" #5
Write a Pandas program to convert a dictionary to a Pandas series.
"""
dic ={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
convert_dic = pd.Series(dic)
#print(convert_dic)

""" #6
Write a Pandas program to convert a NumPy array to a Pandas series.
[10 20 30 40 50]
"""
import numpy as np
numpyArray = np.array([10, 20, 30, 40, 50])
convert_Array = pd.Series(numpyArray)
#print(convert_Array)

""" #7
Write a Pandas program to change the data type of 
given a column or a Series.
"""
os = pd.Series([100,200,'python',300.12,400])

numeric = pd.to_numeric(os,errors='coerce')
#print(numeric)

""" #8
Write a Pandas program to convert the first column of a 
DataFrame as a Series.
"""
df = pd.DataFrame({
    'col1':[1,2,3,4,7,11],
    'col2':[4,5,6,9,5,0],
    'col3':[7,5,8,12,1,11],
})
df_toSeries = pd.Series(df['col1'])
#print(df_toSeries)

""" #9
Write a Pandas program to convert a given Series to an array.
"""
#print(type(os.values))

""" #10
Write a Pandas program to convert Series of lists to one Series.
"""
list_Series = pd.Series([
    ['red','green','white'],
    ['red','black'],
    ['yellow']
])
list_Series=list_Series.apply(pd.Series).stack().reset_index(drop=True)
print(list_Series)