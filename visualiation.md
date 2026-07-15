# ============================
# Import Required Libraries
# ============================

# matplotlib graph banane ke liye use hoti hai.
# pylab module ko "md" naam diya hai taaki baar-baar
# matplotlib.pylab na likhna pade.
# (Industry me pyplot as plt zyada use hota hai.)
import matplotlib.pylab as md

# Pandas Data Analysis aur Data Manipulation ke liye use hoti hai.
# "pd" iska standard alias hai.
import pandas as pd


# ============================
# Load Dataset
# ============================

# CSV file ko read karke DataFrame object me convert karo.
# DataFrame Excel sheet ki tarah rows aur columns me data store karta hai.
data = pd.read_csv("sales_clean.csv")

# Poora DataFrame screen par print karo.
# Isse verify kar sakte hain ki data sahi load hua hai ya nahi.
print(data)


# ============================
# Data Analysis
# ============================

# Category column ke basis par data ko groups me divide karo.
# Fir har category ke Revenue ka total (sum) calculate karo.
#
# Example:
#
# Books
#   200
#   300
#   500
#
# Total = 1000
#
# Electronics
#   500
#   1000
#
# Total = 1500
#
# Output:
# Books          1000
# Electronics    1500
#
by_cat = data.groupby("Category")["Revenue"].sum()

# Grouped revenue ko print karo.
print(by_cat)


# ============================
# Create Bar Chart
# ============================

# Bar Chart Draw karo.
#
# X-axis:
# by_cat.index
# -> Category Names
#
# Y-axis:
# by_cat.values
# -> Revenue Values
#
# color
# -> Bars ka color
#
# width
# -> Bar ki width (motai)
#
# edgecolor
# -> Bar ke border ka color
#
# linewidth
# -> Border ki thickness
#
# alpha
# -> Transparency
#    1 = Fully Visible
#    0 = Invisible
#
# label
# -> Legend me show hone wala naam
md.bar(
    by_cat.index,
    by_cat.values,
    color="blue",
    width=0.6,
    edgecolor="black",
    linewidth=0.5,
    alpha=0.5,
    label="Revenue"
)


# ============================
# Graph Customization
# ============================

# Graph ka title set karo.
md.title("Revenue by Category")

# X-axis ka naam.
md.xlabel("Category")

# Y-axis ka naam.
md.ylabel("Revenue")

# Legend show karo.
# Legend label="Revenue" se aayega.
md.legend()


# ============================
# Display Graph
# ============================

# Ab tak jitni graph commands likhi gayi hain,
# un sabko render (display) karo.
#
# show() ke bina graph kai environments me display nahi hota.
md.show()