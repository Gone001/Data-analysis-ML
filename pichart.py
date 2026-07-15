'''
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv("sales_clean.csv")

#this line groups the data by category and sums the revenue
by_category = df.groupby("Category")["Revenue"].sum()

#this line creates a pie chart
plt.pie(by_category.values,
labels=by_category.index,
autopct="%1.1f%%")

#this line adds a title to the chart
plt.title("Share of Revenue by Category")

#this line tightens the layout of the chart
plt.tight_layout()

#this line saves the chart as a PNG file
plt.savefig("pie_chart.png")

#this line shows the chart
plt.show()
'''

import matplotlib.pyplot as md
import pandas as pd
data=pd.read_csv("sales_clean.csv")
print(data)

category=data.groupby("Category")["Quantity"].size()
print(category)
md.pie(category.values,labels=category.index,autopct="%1.1f%%")
md.title("Orders by category")
md.tight_layout()
md.savefig("order_by_category.png")
md.show()