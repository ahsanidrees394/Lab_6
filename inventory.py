
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Bread", "Yogurt", "Chocolate", "Water", "Cheese"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks",
        "BEVERAGES", "bakery ", "DAIRY", " snacks ",
        "Beverages", "Dairy "
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
        "Rs. 1,800", "Rs. 150", "Rs. 200", "Rs. 250",
        "Rs. 80", "Rs. 550"
    ],
    "Stock": [40, 120, 60, 100, 35, 80, 50, 75, 150, 30]
}

df = pd.DataFrame(data)

df["Category"] = df["Category"].str.strip().str.title()

df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["Category_Code"] = df["Category"].astype("category").cat.codes

print("Cleaned Product Inventory:")
print(df.to_string(index=False))

print("\nCategory Codes:")
print(
    df[["Category", "Category_Code"]]
    .drop_duplicates()
    .sort_values("Category_Code")
    .to_string(index=False)
)

average_price = df.groupby("Category")["Price"].mean()
category_stock = df.groupby("Category")["Stock"].sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(average_price.index, average_price.values)
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=20)

axes[1].pie(
    category_stock.values,
    labels=category_stock.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Share of Total Stock")

fig.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()

print("\nSaved inventory_plots.png")
