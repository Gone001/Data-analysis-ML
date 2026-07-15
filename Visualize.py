import matplotlib.pyplot as md
import pandas as pd
data=pd.read_csv("sales_clean.csv")
print(data)
'''
by_cat=data.groupby("Category")["Revenue"].sum()
print(by_cat)
md.bar(by_cat.index,by_cat.values,color="blue",width=0.6,edgecolor='black',linewidth=0.5,alpha=0.5,label="Revenue")

md.title("Revenue by category")
md.xlabel("Category")
md.ylabel("Revenue")
md.legend()
md.show()


'''
order=data.groupby("Category").size().sort_values(ascending=True)
print(order)
print(order.idxmax(),order.max())
md.bar(order.index,order.values,color="blue",width=0.2,edgecolor='black',linewidth=0.5,alpha=0.5,label="Order")

md.title("Orders by category")
md.xlabel("Category")
md.ylabel("Order")
md.legend()
md.show()
md.tight_layout()
md.savefig("Order by Category.png")