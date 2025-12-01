# Automated Sales Analytics System

An end-to-end Python system for processing sales data, generating analytics charts, and exporting formatted Excel reports to streamline sales reporting workflows.

## Features

### Automated Data Processing
- Reads and cleans raw CSV sales data.
- Aggregates daily revenue, regional performance, and top product metrics.
- Exports a formatted Excel report using a template file.

### Data Visualization
- Generates charts for:
  - Daily sales trend
  - Sales by region
  - Top five products
- All charts are saved to the `outputs/charts` directory.

### Email Report (Optional)
- Includes a script (`send_report.py`) that can email the report file using SMTP settings.

### Included Demo Data
- Sample CSV data and an Excel template are included so the project can be executed immediately.

## Sample Charts

- Daily Sales Trend (Daily_Sales_Chart.png)
- Sales by Region (Sales_by_Region_Chart.png)
- Top 5 Products (Top_5_Products_Chart.png)


## Project Structure

automated_sales/
├── README.md
├── src/
├── data/
├── excel/
├── images/
│ ├── daily_sales.png
│ ├── sales_by_region.png
│ └── top5_products.png
├── .gitignore
└── requirements.txt

## How to Run

1. Set up a virtual environment: python3 -m venv .venv, then source .venv/bin/activate
2. Install dependencies: pip install -r requirements.txt
3. Process the sales data: python src/process_sales.py
4. Generate charts: python src/create_charts.py

Skills Demonstrated
- Python (Pandas, Matplotlib, OpenPyXL)
- Data cleaning and transformation
- Automated reporting and workflow design
- Data visualization
- Structured project organization
- Git and version control
- Virtual environments and requirements management

Purpose
This project demonstrates the ability to combine software development, data analysis, and process automation.