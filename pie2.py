import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv("sales_clean.csv")

# Order of months
order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Group revenue by category
by_category = df.groupby("Category")["Revenue"].sum()

# Group revenue by month
by_month = df.groupby("Month")["Revenue"].sum().reindex(order)

# Print the top category
print(f"Top Category: {by_category.idxmax()} ({by_category.max()})")

# Print the best month
print(f"Best Month: {by_month.idxmax()} ({by_month.max()})")

# Create two charts in one figure
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# -----------------------------
# Bar Chart (Left)
# -----------------------------
axes[0].bar(
    by_category.index,
    by_category.values,
    color="#FBC02D",
    edgecolor="black"
)

axes[0].set_title("Revenue by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Revenue (Rs)")

# -----------------------------
# Line Chart (Right)
# -----------------------------
axes[1].plot(
    by_month.index,
    by_month.values,
    marker="o",
    color="#7c3aed"
)

axes[1].set_title("Revenue by Month")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Revenue (Rs)")

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("two_charts.png")

print("Saved -> two_charts.png")

# Display the figure
plt.show()