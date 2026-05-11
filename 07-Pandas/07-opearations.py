import numpy as np
import pandas as pd

# 1) DataFrame Initialization
print("--- 1) Original DataFrame ---")

df1 = pd.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "B": [10, 20, 30, 40, 50],
        "C": [100, 200, 300, 400, 500],
    }
)
print(df1)
#    A   B    C
# 0  1  10  100
# 1  2  20  200
# 2  3  30  300
# 3  4  40  400
# 4  5  50  500

# 2) DataFrame Metadata & Summary Operations
print("\n--- 2) Basic Information & Metadata ---")

# .shape returns a tuple representing (rows, columns).
print(f"Shape of DataFrame: {df1.shape}")

# .columns returns an Index object containing the names of all columns.
print(f"\nColumn Names: {df1.columns.tolist()}")

# .info() is the ultimate diagnostic tool. It tells you the total rows,
# column names, count of non-null values, data types, and memory usage.
# Note: info() prints directly to the console by default.
print("\nDataFrame Info:")
df1.info()

# .describe() automatically calculates summary statistics (mean, standard
# deviation, min, max, and percentiles) for all NUMERIC columns.
print("\nStatistical Summary (.describe):")
print(df1.describe())


# 3) Broadcasting
print("\n--- 3) Broadcasting Operations ---")

# Just like NumPy, Pandas allows you to broadcast operations.
# Here, we add 10 to every single element in Column A simultaneously,
# without needing a slow 'for' loop!
df1["A"] = df1["A"] + 10
print("Column A after adding 10:\n", df1)


# 4) Applying Custom Functions
print("\n--- 4) Applying Functions ---")


# Sometimes you need a complex calculation that broadcasting can't handle.
# You can define a standard Python function...
def square(x):
    return x**2


# ...and use .apply() to execute that function on every row in the column.
df1["D"] = df1["B"].apply(square)
print("Added Column D (Square of Column B):\n", df1)

# Pro-Tip: Anonymous 'Lambda' Functions
# For simple one-line calculations, Data Scientists rarely write out a full
# 'def' function. Instead, they use inline 'lambda' functions to keep code clean.
# Let's cube Column A and store it in Column E in one single line:
df1["E"] = df1["A"].apply(lambda x: x**3)
print("\nAdded Column E (Cube of Column A using lambda):\n", df1)
