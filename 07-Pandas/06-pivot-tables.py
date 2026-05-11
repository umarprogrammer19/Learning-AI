import numpy as np
import pandas as pd

# Setting a random seed so the "random" numbers are exactly the same every
# time this script is run. This is best practice for reproducible examples!
np.random.seed(42)

# 1) DataFrame Initialization
print("--- 1) Original DataFrame ---")

data = {
    "Date": pd.date_range("2023-01-01", periods=20),
    "Product": ["A", "B", "C", "D"] * 5,
    "Region": ["East", "West", "North", "South"] * 5,
    "Sales": np.random.randint(100, 1000, 20),
    "Units": np.random.randint(10, 100, 20),
    "Rep": ["John", "Mary", "Bob", "Alice"] * 5,
}

df = pd.DataFrame(data)

# Extracting month and quarter from the datetime column
df["Month"] = df["Date"].dt.month_name()
df["Quarter"] = "Q" + df["Date"].dt.quarter.astype(str)

print(df)
# Data Frame:
#          Date Product Region  Sales  Units    Rep    Month Quarter
# 0  2023-01-01       A   East    415     23   John  January      Q1
# 1  2023-01-02       B   West    137     58   Mary  January      Q1
# 2  2023-01-03       C  North    729     45    Bob  January      Q1
# 3  2023-01-04       D  South    817     24  Alice  January      Q1
# 4  2023-01-05       A   East    934     52   John  January      Q1
# 5  2023-01-06       B   West    455     12   Mary  January      Q1
# 6  2023-01-07       C  North    558     29    Bob  January      Q1
# 7  2023-01-08       D  South    748     61  Alice  January      Q1
# 8  2023-01-09       A   East    437     98   John  January      Q1
# 9  2023-01-10       B   West    334     36   Mary  January      Q1
# 10 2023-01-11       C  North    670     56    Bob  January      Q1
# 11 2023-01-12       D  South    375     14  Alice  January      Q1
# 12 2023-01-13       A   East    815     25   John  January      Q1
# 13 2023-01-14       B   West    599     39   Mary  January      Q1
# 14 2023-01-15       C  North    280     12    Bob  January      Q1
# 15 2023-01-16       D  South    417     92  Alice  January      Q1
# 16 2023-01-17       A   East    503     88   John  January      Q1
# 17 2023-01-18       B   West    151     95   Mary  January      Q1
# 18 2023-01-19       C  North    853     29    Bob  January      Q1
# 19 2023-01-20       D  South    500     44  Alice  January      Q1

# 2) Pivot Tables
print("\n--- 2) Pivot Tables ---")
# pd.pivot_table() reshapes your data.
# index   = What goes on the Rows
# columns = What goes on the Columns
# values  = What numbers fill the inside of the table
# aggfunc = How to calculate the overlapping numbers (mean is the default)

# Example A: Median Sales grouped by Region (Rows) and Product (Columns)
pt_median = pd.pivot_table(
    df, values="Sales", index="Region", columns="Product", aggfunc="median"
)
print("Median Sales by Region and Product:\n", pt_median)

# Example B: Multiple Values
# If you pass a list to 'values', Pandas creates a multi-level table.
pt_multi = pd.pivot_table(
    df,
    values=["Sales", "Units"],
    index="Region",
    columns="Product",
    aggfunc="sum",  # Changed to 'sum' as it makes more business sense for this view
)
print("\nTotal Sales AND Total Units by Region and Product:\n", pt_multi)

# Example C: Margins (Grand Totals)
# Adding margins=True automatically calculates the grand totals for rows and columns!
pt_totals = pd.pivot_table(
    df,
    values="Sales",
    index="Rep",
    columns="Product",
    aggfunc="sum",
    margins=True,
    margins_name="Grand Total",
)
print("\nSales by Rep and Product (With Grand Totals):\n", pt_totals)


# 3) Cross Tabulations (Crosstab)
print("\n--- 3) Cross Tabulations ---")
# pd.crosstab() is a specialized version of a pivot table.
# By default, it ignores the 'values' entirely and just COUNTS how many times
# a specific combination occurs in your data (a frequency table).

ct_frequency = pd.crosstab(index=df["Region"], columns=df["Product"])
print(
    "Frequency Count (How many times did each Region sell each Product?):\n",
    ct_frequency,
)

# Note: In this specific dataset, the count is always 5 because of how we
# multiplied the lists during initialization: ["A", "B", "C", "D"] * 5
