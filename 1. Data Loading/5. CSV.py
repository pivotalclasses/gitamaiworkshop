import pandas as pd
data = pd.read_csv('input.csv')
print(data)
# Read specific columns
print (data.loc[:,['salary','name']])
# Read specific rows all columns
print (data.loc[[1,3,5],:])
# Read specific columns with in row range
print (data.loc[2:6,['salary','name']])