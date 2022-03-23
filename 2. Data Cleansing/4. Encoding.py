import pandas as pd
import numpy as np
# Define the headers since the data does not have any
headers = ["num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "horsepower", "peak_rpm","price"]
# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("imports-85.data",header=None, names=headers, na_values="?" )
print(df.head())
print(df.dtypes)
obj_df = df.select_dtypes(include=['object']).copy()#Filter non-numeric cols
cleanup_nums = {"num_doors":     {"four": 4, "two": 2},
                "num_cylinders": {"four": 4, "six": 6, "five": 5, "eight": 8,
                                  "two": 2, "twelve": 12, "three":3 }}
obj_df.replace(cleanup_nums, inplace=True)
print(obj_df.head())
