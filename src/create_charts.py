import pandas as pd
import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORT_XLSX = os.path.join(BASE_DIR, "outputs", "reports", "sales_report.xlsx")
CHARTS_DIR = os.path.join(BASE_DIR, "outputs", "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

# Read sheets
df_product = pd.read_excel(REPORT_XLSX, sheet_name="by_product")
df_region = pd.read_excel(REPORT_XLSX, sheet_name="by_region")
df_daily = pd.read_excel(REPORT_XLSX, sheet_name="daily", parse_dates=["Date"])

# Top 5 products by sales (bar chart)
top5 = df_product.head(5)
plt.figure(figsize=(8,5))
plt.bar(top5["ProductName"], top5["TotalSales"], color='skyblue')
plt.title("Top 5 Products by Sales")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "top5_products.png"))
plt.close()

# Sales by region (pie chart)
plt.figure(figsize=(6,6))
plt.pie(df_region["TotalSales"], labels=df_region["Region"], autopct="%1.1f%%", startangle=140)
plt.title("Sales by Region")
plt.savefig(os.path.join(CHARTS_DIR, "sales_by_region.png"))
plt.close()

# Daily sales (line chart)
plt.figure(figsize=(10,5))
plt.plot(df_daily["Date"], df_daily["TotalSales"], marker='o', linestyle='-')
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "daily_sales.png"))
plt.close()

print(f"Saved charts to {CHARTS_DIR}")
