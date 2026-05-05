import numpy as np
import pandas as pd

# Creating a dataframe
data = {
    "Name": ["Umar", "Raza", "Asad", "Saad"],
    "Age": [28, 34, 29, 42],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [65000, 70000, 62000, 85000],
}

df = pd.DataFrame(data)
print(df)

data_list = [
    ["Umar", 28, "New York", 65000],
    ["Raza", 34, "Paris", 70000],
    ["Asad", 29, "Berlin", 62000],
    ["Saad", 42, "London", 85000],
]
df2 = pd.DataFrame(data_list)
print(df2)
columns = ["Name", "Age", "City", "Salary"]
df2 = pd.DataFrame(data_list, columns)
print(df2)

# Selection And Indexing Of Columns
cols = df[["Name", "City"]]

# Creating a new columns
df["Designation"] = ["Doctor", "Engineer", "Finance", "Artist"]
print(df)

# Removing columns
drop = df.drop("Age", axis=1)
print(drop)  # Main Data frame should be same this is a copy of data frame
df.drop("Age", axis=1, inplace=True)
print(df)
print(df.drop(2))  # Row Because By default Axis is 0

# Selecting Rows
row = df.loc[[0, 1]]
print(row)

row2 = df.iloc[0]
print(row2)

# Selecting Subsets of rows and columns
d = df.loc[[0, 1]][["City", "Salary"]]
print(d)
d = df.loc[[2, 3]][["Name", "Designation"]]
print(d)


