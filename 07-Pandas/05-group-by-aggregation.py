import pandas as pd

# 1) DataFrame Initialization
print("--- Original Sales Data ---")

data = {
    "Category": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "Store": ["S1", "S1", "S2", "S2", "S1", "S2", "S2", "S1"],
    "Sales": [100, 200, 150, 250, 120, 180, 200, 300],
    "Quantity": [10, 15, 12, 18, 8, 20, 15, 25],
    "Date": pd.date_range("2023-01-01", periods=8),
}

df = pd.DataFrame(data)
print(df)


# 2) Single Column Grouping
print("\n--- 2) Single Column Grouping ---")

# Step 1: df.groupby("Category") -> SPLITS data into Group A and Group B
# Step 2: ["Sales"] -> SELECTS only the Sales column to look at
# Step 3: .sum() -> APPLIES the sum function and COMBINES the result
category_sales_sum = df.groupby("Category")["Sales"].sum()
print("Total Sales per Category:\n", category_sales_sum)

# Doing the same thing, but grouping by Store instead.
store_sales_sum = df.groupby("Store")["Sales"].sum()
print("\nTotal Sales per Store:\n", store_sales_sum)


# 3) Multiple Column Grouping
print("\n--- 3) Multiple Column Grouping ---")

# By passing a list of columns ["Category", "Store"], Pandas creates a
# "MultiIndex". It groups by Category first, and then by Store within each Category.
cat_store_sums = df.groupby(["Category", "Store"])["Sales"].sum()
print("Sales grouped by Category, then by Store:\n", cat_store_sums)


# 4) Basic Aggregation (.agg)
print("\n--- 4) Basic Aggregation ---")

# You can run a single mathematical method directly on a column
overall_mean = df["Sales"].mean()
print(f"Overall Average Sales (All Stores): {overall_mean}")

# The .agg() function allows you to run MULTIPLE mathematical calculations
# at the exact same time. You just pass a list of the function names as strings.
all_sales_metrics = df["Sales"].agg(
    ["sum", "mean", "min", "max", "count", "std", "median"]
)
print("\nComprehensive Sales Metrics:\n", all_sales_metrics)


# 5) Advanced Aggregation (Bonus)
print("\n--- 5) Advanced GroupBy with Aggregation ---")

# You can combine .groupby() and .agg() to generate complex reports in one line!
# Here, we group by 'Store', and calculate BOTH the sum and the average of 'Sales'.
store_performance = df.groupby("Store")["Sales"].agg(["sum", "mean"])
print("Store Performance Report (Total vs Average Sales):\n", store_performance)
