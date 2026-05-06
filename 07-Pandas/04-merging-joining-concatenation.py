import numpy as np
import pandas as pd

# 1) Merging Two DataFrames (Like SQL Joins)
print("--- 1) Merging (Joining on a Column) ---")
# .merge() combines DataFrames based on the values of a shared "key" column.

# DataFrame 1: Personal Information
employees = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 5],
        "name": ["Asad", "Umar", "Saad", "Bilal", "Sameed"],
        "department": ["HR", "IT", "Finance", "IT", "HR"],
    }
)

# DataFrame 2: Salary information
salaries = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 6, 7],
        "salary": [60000, 80000, 65000, 70000, 90000],
        "bonus": [5000, 10000, 7000, 8000, 12000],
    }
)

# INNER MERGE: Only keeps rows where the employee_id exists in BOTH DataFrames.
# (IDs 1, 2, and 3 are the only ones present in both).
merge_inner = pd.merge(employees, salaries, on="employee_id", how="inner")
print("Inner Merge (Intersection):\n", merge_inner)

# OUTER MERGE: Keeps ALL rows from BOTH DataFrames.
# If a DataFrame is missing a matching ID, Pandas fills the gaps with NaN.
merge_outer = pd.merge(employees, salaries, on="employee_id", how="outer")
print("\nOuter Merge (Union - Notice the NaNs):\n", merge_outer)

# LEFT MERGE: Keeps ALL rows from the "Left" DataFrame (employees).
# It only brings in salary data if the employee_id matches an existing employee.
merge_left = pd.merge(employees, salaries, on="employee_id", how="left")
print("\nLeft Merge (All Employees, regardless of salary info):\n", merge_left)

# RIGHT MERGE: Keeps ALL rows from the "Right" DataFrame (salaries).
# It only brings in employee info if the ID matches an existing salary record.
merge_right = pd.merge(employees, salaries, on="employee_id", how="right")
print("\nRight Merge (All Salaries, regardless of employee info):\n", merge_right)


# 2) Concatenation (Stacking DataFrames)
print("\n--- 2) Concatenation (Stacking) ---")
# .concat() literally glues DataFrames together. It does not look for matching
# keys; it just stacks them either vertically or horizontally.

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2"],
        "B": ["B0", "B1", "B2"],
        "C": ["C0", "C1", "C2"],
    }
)

df2 = pd.DataFrame(
    {
        "A": ["A3", "A4", "A5"],
        "B": ["B3", "B4", "B5"],
        "C": ["C3", "C4", "C5"],
    }
)

# axis=0 (Default): Stacks rows vertically (on top of each other).
# Notice how the index resets or continues depending on your original data.
concat_rows = pd.concat([df1, df2], axis=0)
print("Concatenated Vertically (axis=0):\n", concat_rows)

# axis=1: Stacks columns horizontally (side-by-side).
concat_cols = pd.concat([df1, df2], axis=1)
print("\nConcatenated Horizontally (axis=1):\n", concat_cols)


# 3) Joining (Merging on the Index)
print("\n--- 3) Joining (Index-based Merge) ---")
# .join() is basically a convenient shortcut for .merge(), but instead of
# looking at a specific column, it automatically merges based on the row INDEX.

df3 = pd.DataFrame(
    {"name": ["Saad", "Umar", "Subhan"]},
    index=[1, 2, 3],  # Custom index!
)

df4 = pd.DataFrame(
    {"score": [85, 90, 75]},
    index=[2, 3, 4],  # Custom index!
)

# Inner Join: Only keeps rows where the INDEX (2 and 3) exists in both.
joining_inner = df3.join(df4, how="inner")
print("Inner Join on Index:\n", joining_inner)

# Outer Join: Keeps all indices (1, 2, 3, 4) and fills missing values with NaN.
joining_outer = df3.join(df4, how="outer")
print("\nOuter Join on Index:\n", joining_outer)
