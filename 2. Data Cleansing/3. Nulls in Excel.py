import pandas as pd
import numpy as np
df = pd.read_excel("ctest.xlsx", sheet_name='Sheet1'
	,usecols=['c','java','python'])
print(df)
print("NaN replaced with '0':")
print(df.fillna(0))