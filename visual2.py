import matplotlib.pyplot as md
import pandas as pd
data=pd.read_csv("sales_clean.csv")
print(data)
by_product=data.groupby("Product")["Revenue"].sum().sort_values(ascending=True)
print(by_product)
print(by_product.idxmax,by_product.max())

md.barh(by_product.index,by_product.values,color="blue",edgecolor='black',linewidth=0.5,alpha=0.5,label="Order")

md.title("Revenue by product")
md.xlabel("Product")
md.ylabel("Revenue")
md.legend()
md.show()
md.tight_layout()
md.savefig("Revenue by product.svg",dpi=300)