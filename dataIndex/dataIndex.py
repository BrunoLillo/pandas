import pandas as pd
import numpy as np

data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})

""" #1
Write a Pandas program to display the default index and set a column 
as an Index in a given dataframe.
"""
df1 = data.copy()
df1_school = df1.set_index('school_code')
df1_id = df1.set_index('t_id')
# print(df1_school)
# print(df1_id)

"""#2
Write a Pandas program to create a multi Index frame using two columns
 and using an Index and a column.
"""
df2 =data.copy()
df2_2index =df2.set_index(['school_code','t_id'])
df2_index_colum = df2.set_index([pd.Index([0,1,2,3,4,5]),'t_id'])
# print(df2_2index)
# print(df2_index_colum)

"""#3
Write a Pandas program to display the default index and set a column 
as an Index in a given dataframe and then reset the index.
"""
df3 =data.copy()
df3_index = df3.set_index('t_id')
df3_reset = df3_index.reset_index(inplace=False)
#print(df3_reset)

"""#4
Write a Pandas program to create an index labels by using 64-bit 
integers, using floating-point numbers in a given dataframe.
"""
df4 =data.copy()
df4_int= pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']},index=[1,2,3,4,5,6])
df4_float= pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']},index=[.1,.2,.3,.4,.5,.6])
# print(df4_int)
# print(df4_float)

"""#5
Write a Pandas program to create a DataFrame using intervals as 
an index.
"""
df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},
                            index = pd.IntervalIndex.from_breaks(
                            [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5]))    
#print(df_interval)

"""#6
Write a Pandas program to create a dataframe indexing by date and time.
"""
di = data.copy()
di = di.set_index('date_Of_Birth')
print(di)