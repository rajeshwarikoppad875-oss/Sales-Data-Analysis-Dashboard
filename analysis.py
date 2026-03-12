import pandas as pd

data = pd.read_csv("sales_data.csv")

print("Dataset:")
print(data)

total_sales = data["Sales"].sum()
print("Total Sales:", total_sales)

product_sales = data.groupby("Product")["Sales"].sum()

print("Sales by Product:")
print(product_sales)