import pandas as pd
import numpy as np
data=pd.read_csv("apple_global_sales_dataset.csv")
#print(data.head())
#print(data.shape)
#region=data["region"]
#print(region.unique())
#print(data.columns)
#missing_rows = data[data.isna().any(axis=1)]
#rint(missing_rows)
#print(data.tail(5))
#print(data.shape)
month=data["month"].unique()
#print(month)
##print(sorted(data["customer_age_group"].unique()))
# Har column ke missing values ka total sum dikhayega
#print(data.isna().sum())


print(data.isnull().sum())
print()

print(data.duplicated().sum())
data=data.drop_duplicates()
print(data)
data.dropna(subset=['previous_device_os'], inplace=True)
data.dropna(subset=['customer_rating'], inplace=True)
print(data.isnull().sum())