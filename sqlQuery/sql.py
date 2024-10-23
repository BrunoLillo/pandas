import pandas as pd 
import numpy as np

employees = pd.read_csv("./csvs/EMPLOYEES.csv")
departments = pd.read_csv("./csvs/DEPARTMENTS.csv")
job_history = pd.read_csv("./csvs/JOB_HISTORY.csv")
jobs = pd.read_csv("./csvs/JOBS.csv")
countries = pd.read_csv("./csvs/COUNTRIES.csv")
regions = pd.read_csv("./csvs/REGIONS.csv")
locations = pd.read_csv("./csvs/LOCATIONS.csv")
"""#1
Write a Pandas program to display all the records
 of REGIONS file.
"""
# print(regions)

"""#2
Write a Pandas program to display all the location id
 from locations file.
"""
result2 = locations[['location_id']]
# print(result2)
"""#3
Write a Pandas program to extract first 7 records from employees file.
"""
result3=employees.head(7)
# print(result3)

"""#4
Write a Pandas program to select distinct department id from 
employees file.
"""
result4 =employees.department_id.unique()
# print(result4)

"""#5
Write a Pandas program to display the first and last name, and
 department number for all employees whose last name is "McEwen".
"""
result5 = employees[employees.last_name =='McEwen']
# for index, row in result5.iterrows():
    # print(row['last_name'], row['first_name'],row['department_id'])

"""#6
Write a Pandas program to display the first, last name, salary and 
department number for those employees whose first name starts with the 
letter 'S
"""
result6 = employees[employees['first_name'].str[:1]=='S' ]
# for index, row in result6.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#7
Write a Pandas program to display the first, last name, salary and 
department number for those employees whose first name does not contain 
the letter 'M
"""
result7 = employees[employees['first_name']!='M']
# for index, row in result7.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#8
Write a Pandas program to display the first name, last name, salary and department 
number in ascending order by department number.
"""
result8 = employees.sort_values('department_id',ascending=True)
# for index, row in result8.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#9
Write a Pandas program to display the first name, last name, salary 
and department number in descending order by first name.
"""
result9= employees.sort_values('first_name',ascending=False)
# for index, row in result9.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#10
Write a Pandas program to display the first name, last name, salary and manger id
where manager ids are null.
"""
result10 = employees[employees['manager_id'].isnull()]
# for index, row in result10.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['manager_id'])

"""#11
Write a Pandas program to display the first name, last name, salary and manger 
id where manager ids are not null.
"""
result11 = employees[employees['manager_id'].notnull()]
# for index, row in result11.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['manager_id'])

"""#12
Write a Pandas program to create and display a boolean series, where True
for not null and False for null values or missing values in 
state_province column of locations file.
"""
result12=locations.state_province.notnull()
# print(result12)

"""#13
Write a Pandas program to create a boolean series selecting rows with one 
or more nulls from locations file.
"""
result13=locations.isnull()
# print(result13)

"""#14
Write a Pandas program to count the NaN values of all the columns 
of locations file.
"""
result14 = locations.isna().sum()
# print(result14)

"""#15
Write a Pandas program to display the first name, last name, salary 
and department number for those employees whose first name ends with 
the letter 'm'.
"""
result15=employees[employees['first_name'].str.endswith('m')]
# for index, row in result15.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#16
Write a Pandas program to display the first name, last name, salary 
and department number for those employees whose first name ends with 
the letter 'd' or 'n' or 's' and also arrange the result in descending 
order by department id.
"""
result16 = employees[employees['first_name'].str[-1].isin(['d','n','s'])].sort_values('department_id',ascending=True)
# print(result16)
"""#17
Write a Pandas program to display the first name, last name, salary and 
department number for employees who works either in department 70 or 90
"""
result17 =employees[employees['department_id'].isin([90,70])]
# for index, row in result17.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#18
Write a Pandas program to display the first name, last name, salary 
and department numberfor those employees whose managers are hold the
 ID 120, 103 or 145.
"""
result18 = employees[employees['manager_id'].isin([120,103,143])]
# for index, row in result18.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#19
Write a Pandas program to display the first, last name, salary and 
department number for those employees who holds a letter n as a 3rd
character in their first name.
"""
result19 = employees[employees['first_name'].str[2:3]=='n']
# for index, row in result19.iterrows():
    # print(row['first_name'],row['last_name'],row['salary'],row['department_id'])

"""#20
Write a Pandas program to display the first name, job id, salary
and department for those employees not working in the departments 
50,30 and 80.
"""
result20 = employees[employees['department_id'].isin([50,30,80])]
# for index, row in result20.iterrows():
    # print(row['first_name'],' ',row['job_id'],row['salary'],' ',row['department_id'])

"""#21
Write a Pandas program to display the ID for 
those employees who did two or more jobs in the past.
"""
result21 =job_history.groupby(['employee_id'])
# print(result21.filter(lambda x:len(x) >1).groupby('employee_id').size().sort_values(ascending=False))

"""#22
Write a Pandas program to calculate minimum, maximum
 and mean salary from employees file.
"""
            
# print(employees.agg({'salary':['min','max','mean','median']}))

"""#23
Write a Pandas program to display the details of jobs in 
descending sequence on job title.
"""
result23 = jobs.sort_values('job_title',ascending=False)
# print(result23)

"""#24
Write a Pandas program to display the first and last name 
and date of joining of the employees who is either Sales Representative
or Sales Man.
"""
result24 = employees[
    (employees['job_id']=='SA_REP')|(employees['job_id']=='SA_MAN')
    ]
for index, row in result24.iterrows():
    print(row['first_name'],' ',row['last_name'],' ',row['job_id'],' ',row['hire_date'])

