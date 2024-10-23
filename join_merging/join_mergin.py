# https://www.w3resource.com/python-exercises/pandas/joining-and-merging/index.php
import pandas as pd
import numpy as np

data_1 = {
    'student_id' : ['s1','s2','s3','s4','s5'],
    'name' : ['Daniella Feton','Ryder Storey','Bryce jensen',
              'Ed Bernal','Kwame Morin'],
    'marks' :[200,210,190,222,199],
    }
data_2 = {
    'student_id' : ['s4','s5','s6','s7','s8'],
    'name' : ['Scarlette Fisher','Carla Williamson','Dante Morse',
              'Kaiser William','Maddeha Preston'],
    'marks' :[201,200,198,219,201],
    }
dataframe1 = pd.DataFrame(data=data_1)
dataframe2 = pd.DataFrame(data=data_2)

"""#1
Write a Pandas program to join the two given dataframes along rows 
and assign all data.
"""
df1 =  pd.concat([dataframe1,dataframe2])
#print(df1)

"""#2
Write a Pandas program to join the two given dataframes along 
columns and assign all data.
"""
df2 = pd.concat([dataframe1,dataframe2],axis=1)
#print(df2)
"""#3
Write a Pandas program to append rows to an existing DataFrame and 
display the combined data.
"""
ds3 = pd.Series(['s6','Scarlette Fisher', 205], index = ['student_id','name','marks'])
df3 = dataframe1.copy()
data3_comb = df3._append(ds3, ignore_index=True)
# print(data3_comb)
"""#4
Write a Pandas program to append a list of dictioneries or series to a 
existing DataFrame and display the combined data.
"""
dic =[
    {'student_id':'s6','name': 'Bruno','marks':100 },
    {'student_id':'s7','name': 'Breno','marks':200 },
    {'student_id':'s8','name': 'carol','marks':300 },
    ]
ds4=pd.Series(['s6','Rosa Juana',400],index=['student_id','name','marks'])

df4= dataframe1.copy()
df4 = df4._append(dic,ignore_index=True)
df4= df4._append(ds4,ignore_index=True)
# print(df4)

"""#5
Write a Pandas program to join the two given dataframes along rows 
and merge with another dataframe along the common column id.
"""
exam_data= pd.DataFrame({
    'student_id':['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10'],
    'exam_id':[23, 45, 12, 67, 21, 55, 33, 14, 56, 83],                  
    })

df5 = pd.concat([dataframe1,dataframe2]).copy()
merge5 = pd.merge(df5, exam_data,on='student_id')
# print(merge5)

"""#6
Write a Pandas program to join the two dataframes using the 
common column of both dataframes.
"""
df6 = pd.merge(dataframe1,dataframe2,on='student_id')
# print(df6)

"""#7
Write a Pandas program to join the two dataframes with 
matching records from both sides where available.
"""
df7= pd.merge(dataframe1,dataframe2,on='student_id',how='outer')
# print(df7)
"""#8
Write a Pandas program to join (left join) the two dataframes using 
keys from left dataframe only.
"""
data_1=pd.DataFrame({
    'K1':['k0','k0','k1','k2'],
    'K2':['k0','k1','k0','k1'],
    'P':['p0','p1','p2','p3'],
    'Q':['q0','q1','q2','q3'],
})
data_2=pd.DataFrame({
    'K1':['k0','k1','k1','k2'],
    'K2':['k0','k0','k0','k0'],
    'R':['r0','r1','r2','r3'],
    'S':['s0','s1','s2','s3'],
})
df8 = pd.merge(data_1, data_2, how='left',on=['K1','K2'])
# print(df8)

"""#9
Write a Pandas program to join two dataframes using 
keys from right dataframe only.
"""
df9=pd.merge(data_1,data_2,how='right',on=['K1','K2'])
# print(df9)

"""#10
Write a Pandas program to merge two given datasets 
using multiple join keys.
"""
df10 = pd.merge(data_1,data_2,on=['K1','K2'])
# print(df10)

"""#11
Write a Pandas program to create a new DataFrame 
based on existing series, using specified argument and 
override the existing columns names.
"""
s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5], name='col3')
df11 = pd.concat([s1, s2, s3], axis=1, keys=['column1', 'column2', 'column3'])
# print(df11)

"""#12
Write a Pandas program to create a combination from two dataframes 
where a column id combination appears more than once in both dataframes.
"""
df12 = pd.merge(data_1,data_2,how='inner',on='K1')
# print(df12)
"""#13
Write a Pandas program to combine the columns of two potentially 
differently-indexed DataFrames into a single result DataFrame.
"""
data13_a=pd.DataFrame({
    'A':['A0','A1','A2'],
    'B':['B0','B1','B2'],
    },index=['K0','K1','K2'])
    
data13_B=pd.DataFrame({
    'C':['C0','C2','C3'],
    'D':['D0','D2','D3'],
    },index=['K0','K1','K2'])
df13 = data13_a.join(data13_B)
# print(df13)

"""#14
Write a Pandas program to merge two given dataframes
 with different columns.
"""
df14 = pd.concat([data_1,data_2],axis=0,ignore_index=True)
print(df14)
