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
print(merge_right)
