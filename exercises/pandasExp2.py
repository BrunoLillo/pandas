import pandas as pd
import numpy as np
"""https://www.w3resource.com/python-exercises/pandas/index-data-series.php"""
""" #11
    Write a Pandas program to sort a given Series.
"""
sample=['100','200','python','300.12','400']
sort = pd.Series(sample).sort_values()
#print(sort)

"""#12
Write a Pandas program to add some data to an existing Series.
"""
sample_plus= pd.concat([pd.Series(sample), pd.Series(['500','php'])],ignore_index=True)
print(sample_plus)