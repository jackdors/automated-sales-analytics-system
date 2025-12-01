import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project root
DATA_CSV = os.path.join(BASE_DIR, "data", "sample_sales.csv")
OUTPUT_XLSX = os.path.join(BASE_DIR, "outputs", "reports", "sales_report.xlsx")

# Make sure output folder exists
os.makedirs(os.path.dirname(OUTPUT_XLSX), exist_ok=True)

# Read CSV
df = pd.read_csv(DATA_CSV, parse_dates=["Date"])

# Compute SalesAmount
df["SalesAmount"] = df["Quantity"] * df["UnitPrice"]

# Aggregate by Product
product_summary = df.groupby("ProductName").agg(
    TotalUnits=("Quantity", "sum"),
    TotalSales=("SalesAmount", "sum")
).reset_index().sort_values("TotalSales", ascending=False)

# Aggregate by Region
region_summary = df.groupby("Region").agg(
    TotalUnits=("Quantity", "sum"),
    TotalSales=("SalesAmount", "sum")
).reset_index().sort_values("TotalSales", ascending=False)

# Aggregate by Day
daily_summary = df.groupby(df["Date"].dt.date).agg(
    TotalUnits=("Quantity", "sum"),
    TotalSales=("SalesAmount", "sum")
).reset_index().rename(columns={"Date": "Date"})

# Write to Excel with multiple sheets
with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="raw_data", index=False)
    daily_summary.to_excel(writer, sheet_name="daily", index=False)
    product_summary.to_excel(writer, sheet_name="by_product", index=False)
    region_summary.to_excel(writer, sheet_name="by_region", index=False)

print(f"Wrote aggregated report to {OUTPUT_XLSX}")
