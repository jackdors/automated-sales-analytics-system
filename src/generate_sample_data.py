import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "sample_sales.csv")

np.random.seed(42)

products = [
    (101, "Widget A", 19.99),
    (102, "Widget B", 29.99),
    (103, "Widget C", 9.99),
    (104, "Service X", 49.99)
]
regions = ["Northeast", "Midwest", "South", "West"]
salespeople = ["Alice", "Bob", "Charlie", "Dana"]

rows = []
start = datetime.now() - timedelta(days=120)
for i in range(1000):
    tdate = (start + timedelta(days=np.random.randint(0, 120))).date()
    pid, pname, price = products[np.random.randint(0, len(products))]
    qty = int(np.random.choice([1,1,1,2,3,5,10], p=[0.4,0.15,0.15,0.12,0.08,0.06,0.04]))
    rows.append({
        "TransactionID": str(uuid.uuid4())[:8],
        "Date": tdate.isoformat(),
        "ProductID": pid,
        "ProductName": pname,
        "Quantity": qty,
        "UnitPrice": price,
        "Region": regions[np.random.randint(0, len(regions))],
        "SalesPerson": salespeople[np.random.randint(0, len(salespeople))]
    })

df = pd.DataFrame(rows)
df.to_csv(OUT, index=False)
print(f"Wrote sample data to {OUT}")

