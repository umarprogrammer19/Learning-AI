import numpy as np
import pandas as pd

# 1) Creating Data with Missing Values
print("--- 1) The 'Dirty' DataFrame ---")

# np.nan stands for "Not a Number". It is the standard way to represent
# missing or null data in Pandas and NumPy.
data = {
    "A": [1, 2, np.nan, 4, 5],
    "B": [1, 2, 3, 4, 5],  # Column B has NO missing data
    "C": [1, 2, 3, np.nan, np.nan],
    "D": [1, np.nan, np.nan, np.nan, 5],
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


# 2) Finding Missing Data
print("\n--- 2) Finding Missing Data ---")

# .isna() returns a DataFrame of the exact same size, but filled with
# True (if data is missing) and False (if data exists).
missing_check = df.isna()
print("Boolean Mask of Missing Data:\n", missing_check)

# .sum() counts the 'True' values (which evaluate to 1) down each column.
# This tells you exactly HOW MANY missing values are in each column.
number_of_missing_values = df.isna().sum()
print("\nCount of missing values per column:\n", number_of_missing_values)

# .any() checks if there is AT LEAST ONE missing value in each column.
print("\nDoes the column have ANY missing data? (True/False):\n", df.isna().any())


# 3) Removing Null Values (Dropping)
print("\n--- 3) Removing Missing Data ---")

# By default, .dropna() drops ANY row that contains AT LEAST ONE missing value.
# In our DataFrame, only row 0 and row 4 have zero missing values.
removed = df.dropna()
print("Dropped rows with ANY missing data:\n", removed)
print("\n(Note: Original df is unchanged because we didn't use inplace=True)")

# The 'thresh' (threshold) parameter is incredibly useful.
# thresh=3 means: "Keep this row ONLY IF it has at least 3 REAL (non-NaN) values."
# Row 0: 4 real values (Kept)
# Row 1: 3 real values (Kept)
# Row 2: 2 real values (Dropped)
# Row 3: 2 real values (Dropped)
# Row 4: 3 real values (Kept)
removed_thres = df.dropna(thresh=3)
print(
    "\nDropped using thresh=3 (Requires >= 3 real values to keep row):\n", removed_thres
)


# 4) Filling Missing Data (Imputation)
print("\n--- 4) Filling Missing Data ---")

# Strategy 1: Fill everything with a single scalar value.
# Good for initializing or zeroing out blanks.
filled_zeros = df.fillna(0)
print("Filled all NaN with 0:\n", filled_zeros)

# Strategy 2: Fill specific columns with specific values using a Dictionary.
# Useful if different columns represent different things (e.g., filling missing
# ages with 18, but missing salaries with 50000).
fill_values = {"A": 0, "B": 100, "C": 200, "D": 1}
filled_diff = df.fillna(value=fill_values)
print("\nFilled using a dictionary (Column A gets 0, C gets 200, etc.):\n", filled_diff)

# Strategy 3: Fill with Statistical Measures (The most common approach in Machine Learning!)
# df.mean() calculates the average of each column.
# Pandas is smart enough to fill the NaN values in Column A with the mean of Column A,
# and the NaNs in Column C with the mean of Column C.
filled_mean = df.fillna(df.mean())
print(
    "\nFilled NaNs with the average (mean) of their respective columns:\n", filled_mean
)
