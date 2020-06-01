import pandas
'''
#Creating a Series using ndarray
import numpy as np
arr = np.array([1,2,3,4,5])
series = pandas.Series(arr)
print(series)


#Creating a Series using a dict
data = {'a':1, 'b':2, 'c':3}
series = pandas.Series(data)
print(series)
'''

#Accessing data from series using slicing
s = pandas.Series([1,2,3,4,5])
print(s[1:4])