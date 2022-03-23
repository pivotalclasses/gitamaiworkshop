import pandas as pd
import numpy as np
#1.Load CSV into pandas
df = pd.read_csv('test.csv')
print(df)
#2.Show first 3 rows
print(df.head(3))
#3.Knowing data type of column
print("Cost column type: ", df['cost'].dtypes)
print("Discount column type: ", df['discount'].dtypes)
#4.Apply Padding
print(df.fillna(0))
print(df.fillna(method='bfill'))
#5.Column Operations (Column Level Calculations)
print(df['quantity']*df['cost']*(100-df['discount'])/100)