import numpy as np
import pandas as pd

# Merging Two Dataframes

# Dataframe 1: Personal Information
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

merge_inner = pd.merge(employees, salaries, on="employee_id", how="inner")
# print(merge_inner)

merge_outer = pd.merge(employees, salaries, on="employee_id", how="outer")
# print(merge_outer)

merge_left = pd.merge(
    employees, salaries, on="employee_id", how="left"
)  # Merge Basis Of Employes
# print(merge_left)

merge_right = pd.merge(
    employees, salaries, on="employee_id", how="right"
)  # Merge Basis Of Salaries
# print(merge_right)

# Concatination of Two dataframes

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

concat = pd.concat([df1, df2])
print(concat)

concat_rows = pd.concat([df1, df2], axis=1)
print(concat_rows)
