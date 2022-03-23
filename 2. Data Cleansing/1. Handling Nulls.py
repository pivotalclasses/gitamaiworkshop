import pandas as pd
#Cleansing - Handling Nulls
df = pd.read_csv('myincome.csv')
print(df)
print("NaN removed unconditionally:")
print(df.dropna())
print("NaN repalced by '0':")
print(df.fillna(0))
print("NaN repalced by next neighbour values:")
print(df.fillna(method='bfill'))
print("NaN repalced by previous neighbour values:")
print(df.fillna(method='ffill'))
mean_values = df.mean()
print(df.fillna(mean_values))