import pandas as pd
import numpy as np
# Define the headers since the data does not have any
headers = ["sno","name","grade","section"]
# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("test.data",header=None, names=headers, na_values="?" )
print(df.head())
#print(df.dtypes)
obj_df = df.select_dtypes(include=['object']).copy()#Filter non-numeric cols
cleanup_nums = {"grade":     {"four": 4, "two": 2, "three": 3, "one": 1},
                "section":  {"cse": 1, "it": 2, "ece": 3, "eee": 4}}
obj_df.replace(cleanup_nums, inplace=True)
print(obj_df.head())
