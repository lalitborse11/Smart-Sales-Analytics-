import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# SMART SALES ANALYTICS
# ==============================

# Load Dataset
df = pd.read_csv("sales_data_200.csv")

print("SMART SALES ANALYTICS")
print("---------------------")

# ==============================
# 1. DATASET
# ==============================

print("\nDataset:")
print(df)

print("\nTotal Rows:", len(df))
print("Total Columns:", len(df.columns))

# ==============================
# 2. BASIC ANALYSIS
# ==============================

total_sales = df["Sales"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Sales"].mean()

print("\nBASIC ANALYSIS")
print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Total Quantity:", total_quantity)

# ==============================
# 3. REGION ANALYSIS
# ==============================

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

# ==============================
# 4. CATEGORY ANALYSIS
# ==============================

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# ==============================
# 5. TOP PRODUCT
# ==============================

product_sales = df.groupby("Product")["Sales"].sum()

top_product = product_sales.idxmax()
top_sales = product_sales.max()

print("\nTop Selling Product:")
print("Product:", top_product)
print("Sales:", top_sales)

# ==============================
# 6. PRODUCT-WISE SALES CHART
# ==============================

plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")

plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# 7. REGION-WISE SALES CHART
# ==============================

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Region-wise Total Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# 8. CATEGORY-WISE SALES CHART
# ==============================

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# 9. MONTHLY SALES
# ==============================

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# 10. PRODUCT QUANTITY
# ==============================

product_quantity = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold by Product:")
print(product_quantity)

plt.figure(figsize=(10, 6))
product_quantity.plot(kind="bar")

plt.title("Product-wise Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")

plt.tight_layout()
plt.show()

# ==============================
# 11. TOP 5 PRODUCTS
# ==============================

top_5_products = product_sales.sort_values(
    ascending=False
).head(5)

print("\nTop 5 Products by Sales:")
print(top_5_products)

plt.figure(figsize=(8, 5))
top_5_products.plot(kind="bar")

plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# 12. KPI SUMMARY
# ==============================

highest_region = region_sales.idxmax()
highest_region_sales = region_sales.max()

highest_category = category_sales.idxmax()
highest_category_sales = category_sales.max()

print("\n==============================")
print("     SMART SALES ANALYTICS")
print("==============================")

print("Total Sales     :", total_sales)
print("Total Quantity  :", total_quantity)
print("Average Sale    :", round(average_sales, 2))
print("Top Product     :", top_product)
print("Best Region     :", highest_region)
print("Best Category   :", highest_category)

print("==============================")

# ==============================
# 13. BUSINESS INSIGHTS
# ==============================

print("\n==============================")
print("       BUSINESS INSIGHTS")
print("==============================")

print("1. Laptop is the top-selling product.")
print("2. South region generated the highest sales.")
print("3. Electronics is the highest-performing category.")
print("4. Total sales reached:", total_sales)
print("5. Total quantity sold:", total_quantity)

print("==============================")
print("\nPROJECT COMPLETED SUCCESSFULLY!")