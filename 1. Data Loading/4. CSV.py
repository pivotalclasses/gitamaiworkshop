import pandas as pd
data = pd.read_csv('input.csv')
#Sorting data
data1 = data.sort_values('salary', ascending=False)
print(data1)
#Filtering data
filter1 = data['salary']<600
filter2 = data['dept']=='IT'
data2 = data1.where(filter1&filter2)
print(data2)