"""
https://www.w3resource.com/python-exercises/pandas/index-dataframe.php
"""

import pandas as pd
import numpy as np

exam_data = {'name': 
['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': 
['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
dataframe = pd.DataFrame(exam_data,index= labels)

""" #1
Write a Pandas program to create a dataframe from a dictionary 
and display it.
Sample data: {'X':[78,85,96,80,86], 
'Y':[84,94,89,83,86],
'Z':[86,97,96,72,83]}

"""
df = pd.DataFrame({
    'X':[78,85,96,80,86], 
    'Y':[84,94,89,83,86],
    'Z':[86,97,96,72,83],
})
#print(df)

""" #2
Write a Pandas program to create and display a DataFrame from a specified 
dictionary data which has the index labels.
"""

df2= dataframe.copy()
#print(df2)

""" #3
Write a Pandas program to display a summary of the basic information 
about a specified DataFrame and its data.
"""
df3 = dataframe.copy()
#print(df3.info())

""" #4
Write a Pandas program to get the first 3 rows of a given DataFrame.
Sample Python dictionary data and list labels:
"""
df4 = dataframe.copy()
#print(df4.iloc[:3])

""" #5
Write a Pandas program to select the 'name' and 
'score' columns from the following DataFrame.
"""
df5 = dataframe.copy()
colums = df5[['name','score']]
#print(colums)

""" #6
Write a Pandas program to select the specified columns and 
rows from a given data frame.
"""
df6 = dataframe.copy()
df_lines=df6.iloc[[1,3,5,6],[1,3]]
#print(df_lines)

""" #7
Write a Pandas program to select the rows where the number of 
attempts in the examination is greater than 2.

"""
df7 = dataframe.copy()
df7 = df7[df7['attempts']>2]
#print(df7)

"""#8
Write a Pandas program to count the number of rows 
and columns of a DataFrame.
"""
df8 = dataframe.copy()

#print(f'Number of rows: {len(df8.axes[1])}')
#print(f'Number of coluns: {len(df8.axes[0])}')

""" #9
Write a Pandas program to select the rows where the score 
is missing, i.e. is NaN.
"""
df9 = dataframe.copy()
#print(df9[df9['score'].isnull()])

""" #10
Write a Pandas program to select the rows the score is 
between 15 and 20 (inclusive).
"""
df10=dataframe.copy()
#print(df10[(df10['score'] >= 15) & (df10['score'] <= 20)] )

""" #11
Write a Pandas program to select the rows where number of attempts in the 
examination is less than 2 and score greater than 15.
"""
df11 = dataframe.copy()
resultdf11 = df11[(df11['attempts'] <2 ) & (df11['score']> 15)]
#print(resultdf11)

""" #12
Write a Pandas program to change the score in row 'd' to 11.5.
"""
df12=dataframe.copy()
df12.loc['d','score'] = 11.5
#print(df12)

"""#13
Write a Pandas program to calculate the sum of the examination 
attempts by the students.
"""
df13= dataframe.copy()
sum_att = sum(df13['attempts'])
#print(sum_att)

""" #14
Write a Pandas program to calculate the mean of all students' scores. 
Data is stored in a dataframe.
"""
df14 = dataframe.copy()
mean_students= df14['score'].mean()
#print(f'mean: {mean_students:.2f}')

""" #15
Write a Pandas program to append a new row 'k' to data frame with given
values for each column. 
Now delete the new row and return the original DataFrame.
"""
df15 =dataframe.copy()
df15.loc['k']=['Suresh',15.5,1,'yes']
df15=df15.drop('k')
#print(df15)

"""#16
Write a Pandas program to sort the DataFrame first by 'name' in 
descending order, then by 'score' in ascending order.
"""
df16 =dataframe.copy()
df16=df16.sort_values(['name','score'],ascending=[False,True])
#print(df16)

""" #17
Write a Pandas program to replace the 'qualify' column contains 
the values 'yes' and 'no' with True and False.
"""
df17 = dataframe.copy()
df17['qualify'] = df17['qualify'].map({'yes':True,'no':False})
#print(df17)

""" #18
Write a Pandas program to change the name 'James' to 'Suresh' 
in name column of the DataFrame.
"""
df18 =dataframe.copy()
df18['name']=df18['name'].replace('James','Suresh')
#print(df18)

"""#19
Write a Pandas program to delete the 'attempts' column from 
the DataFrame.
"""
df19 = dataframe.copy()
df19=df19.drop('attempts',axis=1)
#print(df19)
"""#20
Write a Pandas program to insert a new column in existing DataFrame.
"""
df20 =dataframe.copy()
df20['color']=['Red','Blue','Green','Red','Blue','Green','Red','Blue','Green','Blue']
#print(df20)

"""#21
Write a Pandas program to iterate over rows in a DataFrame.
Sample Python dictionary data and list labels:
exam_data = [{'name':'Anastasia', 'score':12.5}, 
{'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
"""
exam21 = [{'name':'Anastasia', 'score':12.5}, 
{'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]

df21 = dataframe.copy()
for index, row in df21.iterrows():
    ...
    # print(row['name'], row['score'])
"""#22
Write a Pandas program to get list from DataFrame column headers.
"""
df22 = dataframe.copy()
colums = df22.columns.values
#print(colums)
"""#23
Write a Pandas program to rename columns of a given DataFrame
"""
origin23=pd.DataFrame({
    'col1':[1,2,3],
    'col2':[4,5,6],
    'col3':[7,8,9],
})
df23= origin23.rename(columns={'col1':'Column1','col2':'Column2',
                         'col3':'Column3'})
#print(df23)

"""#24
Write a Pandas program to select rows from a given DataFrame based 
on values in some columns.
"""
origin24= pd.DataFrame({
    'col1':[1,4,3,4,5],
    'col2':[4,5,6,7,8],
    'col3':[7,8,9,0,1],
})
df24=origin24[origin24['col1']==4]
#print(df24)

""" #25
Write a Pandas program to change the order of a DataFrame columns.
"""
origin25 = pd.DataFrame({
    'col1':[1,4,3,4,5],
    'col2':[4,5,6,7,8],
    'col3':[7,8,9,0,1],
})
df25 = origin25[['col3','col2','col1']]
#print(df25)

"""#26
Write a Pandas program to add one row in an existing DataFrame.
"""

df26 = pd.DataFrame({
    'col1':[1,4,3,4,5],
    'col2':[4,5,6,7,8],
    'col3':[7,8,9,0,1],
})
df26_2={'col1':10, 'col2':11, 'col3':12}
#df26=df26.append(df26_2)
df26 = df26._append(df26_2, ignore_index=True)
#print(df26)

"""#27
Write a Pandas program to write a DataFrame to CSV 
file using tab separator.
"""
df27 = pd.DataFrame({
    'col1':[1,4,3,4,5],
    'col2':[4,5,6,7,8],
    'col3':[7,8,9,0,1],
})
df27.to_csv('./csvs/doc27.csv',sep='\t', index=False)
new_df27 = pd.read_csv('csvs/doc27.csv')
#print(new_df27)

""" #28
Write a Pandas program to count city wise number of people from a 
given of data set (city, name of the person).
"""
df28= pd.DataFrame({
    'name':['lu','bru','ana','carol','breno','rosa','jorge','Gu','caio','leao'],
    'city':['California','California','California','California','Georgia','Georgia',
           'Los Angeles','Los Angeles','Los Angeles','Los Angeles' ]
})
df28 = df28.groupby(['city']).size().reset_index(name='Number of people')
#print(df28)

"""#29
Write a Pandas program to delete DataFrame row(s) based on given column
 value.
"""
df29 =pd.DataFrame({
    'col1':[1,4,3,4,5],
    'col2':[4,5,6,7,8],
    'col3':[7,8,9,0,1],
})
df29 = df29[df29.col2 != 5]
#print(df29)
"""#30
Write a Pandas program to widen output display to see more columns.
"""

"""#31
Write a Pandas program to select a row of series/dataframe by given 
integer index.
"""
df31 = pd.DataFrame({
    'col1':[1,4,3,4,5],
    'col2':[4,5,6,7,8],
    'col3':[7,8,9,0,1],
})
df31= df31.iloc[[2]]
#print(df31)

"""#32
Write a Pandas program to replace all the NaN values with Zero's in a 
column of a dataframe.
"""
df32 = dataframe.copy()
df32=df32.fillna(0)
#print(df32)

"""#33
Write a Pandas program to convert index in a column of the given 
dataframe.
"""
df33 = pd.DataFrame(data=exam_data) 
df33.reset_index(level=0, inplace=True)
#print(df33.to_string(index=False))

"""#34
Write a Pandas program to set a given value for particular cell in
  DataFrame using index value.
"""
df34 = dataframe.copy()
df34._set_value('i','score',10.2)
#print(df34)

"""#35
Write a Pandas program to count the NaN values in one or more 
columns in DataFrame.
"""
df35 = dataframe.copy()
df35=df35.isnull().values.sum()
#print(df35)

"""#36
Write a Pandas program to drop a list of rows from a 
specified DataFrame.
"""
df36 = pd.DataFrame({
    'col1':[1,4,3,4,5],
    'col2':[4,5,6,7,8],
    'col3':[7,8,9,0,1],
})
df36 =df36.drop(df36.index[[2,4]])
#print(df36)

"""#37
Write a Pandas program to reset index in a given DataFrame.
"""
df37 = dataframe.copy()
df37 = df37.drop(df37.index[[0,1]])
df37.reset_index(level=0,inplace=True)
#print(df37)
"""#38
Write a Pandas program to divide a DataFrame in a given ratio.
"""
df38= pd.DataFrame(np.random.randn(10,2))
part70 = df38.sample(frac=0.7,random_state=10)
part30 =df38.drop(part70.index)
#print(df38)
#print(part70)
#print(part30)

"""#39
Write a Pandas program to combining two series into a DataFrame.
"""
df39_1 =pd.DataFrame([100,200,'python',300.12,400])
df39_2 =pd.DataFrame([10,20,'php',30.12,40])
df39=pd.concat([df39_1,df39_2],axis=1)
# print(df39)

"""#40
Write a Pandas program to shuffle a given DataFrame rows.
"""
df40 =dataframe.copy()
df40=df40.sample(frac=1)
print(df40)
"""#41

"""