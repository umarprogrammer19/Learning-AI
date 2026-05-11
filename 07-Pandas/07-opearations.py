import numpy as np
import pandas as pd

# DataFrames Basic Operations
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

# Shape
print(df1.shape)  # (5, 3)

# Colums
print(df1.columns)  # Index(['A', 'B', 'C'], dtype='str')

# Information
print(df1.info())

# Describe
print(df1.describe())

# Broadcasting
df1["A"] = df1["A"] + 10


# DataFrames Applying Functions
def square(x):
    return x**2


df1["D"] = df1["B"].apply(square)
print(df1)
