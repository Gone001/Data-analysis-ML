
import pandas as pd
'''
df=pd.read_csv("apple_global_sales_dataset.csv")

together=df[["storage","previous_device_os"]]
print(together)
# Jo '18–24' mein nahi hain, unhe select karo (Yani baaki sab 20+ hain)
age_filter = df[df["customer_age_group"] != "18–24"]
print(age_filter)

print(df.isnull().sum())
print(df.duplicated().sum())
data=df.drop_duplicates()
print(data)
# 1. 'storage' ko 'Unknown' se fill karein
df['storage'] = df['storage'].fillna('Unknown')

# 2. 'customer_rating' ko median rating se fill karein
df['customer_rating'] = df['customer_rating'].fillna(df['customer_rating'].median())

# 3. 'previous_device_os' ko 'Not Disclosed' se fill karein
df['previous_device_os'] = df['previous_device_os'].fillna('Not Disclosed')
print(df.isnull().sum())
print(df)
print((df["storage"].unique()))


'''
df=pd.read_csv("messy_sales.csv")
print(df)
df["Revenue"]=df["Quantity"]*df["Price"]
print(df)
by_cat=df.groupby("Category")["Revenue"].count()
print(by_cat)
#revenue by month
df["date"]=pd.to_datetime(df["Date"])
df["Month"]=df["date"].dt.month_name()
by_month=df.groupby("Month")["Revenue"].sum()
print(by_month.sort_values(ascending=False))
by_cat.to_csv("Revenue_by_category.csv") # save the result