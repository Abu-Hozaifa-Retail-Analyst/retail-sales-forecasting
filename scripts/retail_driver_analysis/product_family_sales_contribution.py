"""Analyze product-family sales contribution for complete months."""

from pathlib import Path
import pandas as pd

# Define project input and output paths.
INPUT_FILE = Path("data/processed/train_standardized.csv")
OUTPUT_DIR = Path("reports/retail_driver_analysis")
OUTPUT_FILE = OUTPUT_DIR / "product_family_sales_contribution.csv"

# Load only the columns needed for this analysis.
sales = pd.read_csv(
    INPUT_FILE,
    usecols=["date", "family", "sales"],
    parse_dates=["date"]
)

# Keep the 55 complete months used in forecasting.
sales = sales.loc[
    (sales["date"] >= "2013-01-01")
    & (sales["date"] < "2017-08-01")
]

# Aggregate sales by product family.
family_sales = (
    sales.groupby("family", as_index=False)
    .agg(total_sales=("sales", "sum"))
)

# Calculate sales contribution.
overall_sales = family_sales["total_sales"].sum()

family_sales["sales_share_pct"] = (
    family_sales["total_sales"] / overall_sales * 100
)

# Rank families from highest to lowest sales.
family_sales = family_sales.sort_values(
    ["total_sales", "family"],
    ascending=[False, True]
).reset_index(drop=True)

# Calculate cumulative contribution in ranked order.
family_sales["cumulative_share_pct"] = (
    family_sales["sales_share_pct"].cumsum()
)

# Validate the analysis.
assert len(family_sales) == 33, "Unexpected number of product families"
assert abs(family_sales["sales_share_pct"].sum() - 100) < 0.000001

# Create the output folder and save results.
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
family_sales.to_csv(OUTPUT_FILE, index=False)

print("Product families:", len(family_sales))
print("Total sales:", round(overall_sales, 2))
print()
print(family_sales.head(10).round(2).to_string(index=False))
print()
print("Saved report:", OUTPUT_FILE)
