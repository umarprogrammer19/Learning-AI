import pandas as pd

data = {
    "Category": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "Store": ["S1", "S1", "S2", "S2", "S1", "S2", "S2", "S1"],
    "Sales": [100, 200, 150, 250, 120, 180, 200, 300],
    "Quantity": [10, 15, 12, 18, 8, 20, 15, 25],
    "Date": pd.date_range("2023-01-01", periods=8),
}

df = pd.DataFrame(data)

#   Category Store  Sales  Quantity        Date
# 0        A    S1    100        10     2023-01-01
# 1        B    S1    200        15     2023-01-02
# 2        A    S2    150        12     2023-01-03
# 3        B    S2    250        18     2023-01-04
# 4        A    S1    120         8     2023-01-05
# 5        B    S2    180        20     2023-01-06
# 6        A    S2    200        15     2023-01-07
# 7        B    S1    300        25     2023-01-08

# 1) Group by Category and calculate the sum of Sales
sum_of_cat = df.groupby("Category")["Sales"].sum()
print(sum_of_cat)

# 2) Group by Store and calculate the sum of Sales
sum_of_store = df.groupby("Store")["Sales"].sum()
print(sum_of_store)

# Group by multiple columns
# Group by Category and Store

sums = df.groupby(["Category", "Store"])["Sales"].sum()
print(sums)

# Aggregation
# mean_of_sales = df["Sales"].mean()
# print(mean_of_sales)

# all = df["Sales"].agg(["sum", "mean", "min", "max", "count", "std", "median"])
# print(all)
