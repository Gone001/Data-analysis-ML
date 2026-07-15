import matplotlib.pyplot as md
import pandas as pd
data=pd.read_csv("sales_clean.csv")
eletronics=data[data["Category"]=="Electronics"]
print(eletronics)
by_month=eletronics.groupby("Month")["Revenue"].sum().reindex( ["January", "February", "March", "April", "May"])
print(by_month)
print(by_month.idxmax(),by_month.max())
md.plot(by_month.index, by_month.values, marker="*", color="#7c3aed",label="Electronics")
md.xlabel("Product")
md.ylabel("Revenue")
md.legend()
md.tight_layout()
md.show()
md.savefig("Revenue by Electronics.png")