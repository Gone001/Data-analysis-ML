
import matplotlib.pyplot as md
import pandas as pd
data=pd.read_csv("sales_clean.csv")
print(data)
by_month=data.groupby("Month")["Quantity"].sum().reindex( ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
print(by_month)
print(by_month.idxmax(),by_month.max())
md.plot(by_month.index, by_month.values, marker="*", color="#7c3aed")

#this line adds a title to the chart
md.title("Quantity Trend by Month")

#this line adds a label to the x-axis
md.xlabel("Month")

#this line adds a label to the y-axis
md.ylabel("Qunatity")

#this line tightens the layout of the chart
md.tight_layout()

#this line saves the chart as a PNG file
md.savefig("Quantity_by_month.png")

#this line shows the chart
md.show()


