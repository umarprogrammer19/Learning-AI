import pandas as pd

# 1) Creating a DataFrame
print("--- 1) Creating DataFrames ---")

# Method A: From a Dictionary
# Keys become Column Headers, Values become the rows.
data_dict = {
    "Name": ["Umar", "Raza", "Asad", "Saad"],
    "Age": [28, 34, 29, 42],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [65000, 70000, 62000, 85000],
}

df = pd.DataFrame(data_dict)
print("DataFrame from Dictionary:\n", df)

# Method B: From a List of Lists
data_list = [
    ["Umar", 28, "New York", 65000],
    ["Raza", 34, "Paris", 70000],
    ["Asad", 29, "Berlin", 62000],
    ["Saad", 42, "London", 85000],
]

# Without column names, Pandas uses 0, 1, 2, 3
df_list_no_cols = pd.DataFrame(data_list)
print("\nDataFrame from List (No Columns):\n", df_list_no_cols)

# If you just pass the list, Pandas assumes you are setting the row 'index'.
col_names = ["Name", "Age", "City", "Salary"]
df_list_with_cols = pd.DataFrame(data_list, columns=col_names)
print("\nDataFrame from List (With Columns):\n", df_list_with_cols)


# 2) Modifying Columns (Selecting, Adding, Dropping)
print("\n--- 2) Column Operations ---")

# Selecting specific columns (pass a list of column names inside the brackets)
selected_cols = df[["Name", "City"]]
print("Just Name and City:\n", selected_cols)

# Creating a new column. Just declare it like a new dictionary key!
# Note: The list you provide must match the number of rows in the DataFrame.
df["Designation"] = ["Doctor", "Engineer", "Finance", "Artist"]
print("\nAdded 'Designation' column:\n", df)

# Removing columns using drop()
# axis=1 means "look at columns". axis=0 (default) means "look at rows".
# This returns a COPY of the DataFrame with the column removed.
df_dropped_copy = df.drop("Age", axis=1)
print("\nReturned a copy without 'Age':\n", df_dropped_copy)
print("Original df still has 'Age':\n", df)

# Using inplace=True modifies the original DataFrame permanently in memory.
df.drop("Age", axis=1, inplace=True)
print("\nOriginal df after inplace drop of 'Age':\n", df)

# Dropping a Row (axis=0 is the default)
# This drops the row at index 2 (Asad).
print("\nDropping Row index 2 (returns a copy):\n", df.drop(2))


# 3) Selecting Rows (loc vs iloc)
print("\n--- 3) Selecting Rows ---")

# .loc[] locates rows based on their LABEL / NAME.
# Here, our labels just happen to be numbers (0, 1, 2, 3).
rows_loc = df.loc[[0, 1]]
print("Selecting Rows 0 and 1 using .loc:\n", rows_loc)

# .iloc[] locates rows based on their INTEGER POSITION (like a standard Python list).
# Even if your row labels were letters ["A", "B", "C"], .iloc[0] would grab the first row.
row_iloc = df.iloc[0]
print("\nGrabbing the very first row using .iloc:\n", row_iloc)

# Selecting subsets of both rows AND columns
# First .loc[] grabs the rows, the second [][] grabs the columns from that result.
subset_1 = df.loc[[0, 1]][["City", "Salary"]]
print("\nSubset: Rows 0,1 & City,Salary:\n", subset_1)

subset_2 = df.loc[[2, 3]][["Name", "Designation"]]
print("\nSubset: Rows 2,3 & Name,Designation:\n", subset_2)


# 4) Conditional Selection (Filtering)
print("\n--- 4) Conditional Filtering ---")

# Exactly like NumPy, this creates a boolean mask [False, True, False, True]
# and filters the rows where the condition is True.
high_salary = df[df["Salary"] >= 70000]
print("People earning 70,000 or more:\n", high_salary)

# Multiple conditions MUST be wrapped in parentheses ()
# and use bitwise operators: & (AND), | (OR), ~ (NOT).
specific_target = df[(df["Salary"] >= 70000) & (df["City"] == "Paris")]
print("\nPeople earning 70,000+ AND living in Paris:\n", specific_target)
