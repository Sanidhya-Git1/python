import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Series
# s1 = pd.Series([11,21,31,5])
# print(s1)
# print(type(s1))

# print(s1.index) #RangeIndex(start=0, stop=4, step=1)
# print(s1.values)

# s2 = pd.Series([11,21,31,5], index = ['a','b','c','d'])
# print(s2)
# print(s2.index) #Index(['a', 'b', 'c', 'd'], dtype='str')
# print(s2.values) # [11 21 31  5]
# print(type(s2.values)) # <class 'numpy.ndarray'>

#Dataframe
# data = {
#     'City' : ['San Fransisco','San Jose','Seattle'],
#     'Population' : [1000000,200000,500000]
# }
#creating a dataframe from the given data
#df = pd.DataFrame(data)
# print(df)

#creating a dataframe from the given data
# df = pd.DataFrame.from_dict(data, orient = 'columns')
# #df = pd.DataFrame.from_dict(data, orient = 'index')
# print(df)

data = [
    {'City' : 'San Fransisco', 'Population' : 100000},
    {'City' : 'San Jose', 'Population' : 200000},
    {'City' : 'Seattle', 'Population' : 500000}
]
df = pd.DataFrame(data)
print(df)
print("----------------------------")  
data = [
    ('San Fransisco', 100000),
    ('San Jose',200000),
    ('Seattle',500000)
]

df = pd.DataFrame.from_records(data, columns=['City', 'Population'])
print(df)
print("----------------------------")  

cities = ['San Fransisco','San Jose','Seattle']
populations = [100000,200000,500000]

data = list(zip(cities,populations))
print(data) # [('San Fransisco', 100000), ('San Jose', 200000), ('Seattle', 500000)]
df = pd.DataFrame(data, columns=['City','Population'])
print(df)
print("----------------------------")  

city_series = pd.Series(['San Fransisco','San Jose','Seattle'] , name = 'City')
population_series = pd.Series([100000,200000,500000], name = 'Population')
df = pd.concat([city_series, population_series], axis = 1) # horizontal concatenation
print(df)
print("----------------------------")  