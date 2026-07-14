
import pandas as pd
df=pd.read_csv("messy_sales.csv")
print(df.isnull().sum())
print(df.duplicated())
df=df.drop_duplicates()
print(df.duplicated())
df.dropna(subset=["Price"],inplace=True)
df["Quantity"]=df["Quantity"].fillna(0)
print(df.isnull().sum())
df["date"]=pd.to_datetime(df["Date"])
df["Month"]=df["date"].dt.month_name()
print(df)
df["Revenue"]=df["Quantity"]*df["Price"]
print(df)
By_cat=df.groupby("Category")["Revenue"].sum()
print(By_cat.sort_values(ascending=False))
print(f"Total revenue is : {df["Revenue"].sum()} ")

df.to_csv("cleaned_datasales.csv")
By_cat.to_csv("Revenue_by_category.csv")

dn=pd.read_csv("cleaned_datasales.csv")
print(dn)