import numpy as np
import pandas as pd

# 1) Introduction to Pandas Series
print("--- 1) Introduction to Pandas Series ---")
# A Series is a one-dimensional labeled array.
# It can hold any data type (integers, strings, floats, Python objects, etc.).
# The key difference from a NumPy array is the "index" (the axis labels).
# If you don't provide an index, Pandas creates a default numeric one (0, 1, 2...).

# Setting up our basic data sources
labels = ["a", "b", "c"]
my_list = [10, 20, 30]
my_arr = np.array([10, 20, 30])
my_dict = {"a": 10, "b": 20, "c": 30}


# 2) Creating Series from Different Data Types
print("\n--- 2) Creating Series ---")

# Method A: From a standard Python List
# Because we didn't specify an index, Pandas automatically assigns 0, 1, 2.
series_from_list = pd.Series(data=my_list)
print("From a Python List (Default Index):\n", series_from_list)

# Method B: From a Python List WITH a Custom Index
# We explicitly tell Pandas to use our 'labels' array as the index.
# Note: The data list and index list must be the exact same length!
series_with_labels = pd.Series(data=my_list, index=labels)
print("\nFrom a Python List (Custom Index):\n", series_with_labels)

# Method C: From a NumPy Array
# This works exactly like passing a Python list. Pandas is built on top of NumPy,
# so they integrate perfectly.
series_from_array = pd.Series(data=my_arr, index=labels)
print("\nFrom a NumPy Array (Custom Index):\n", series_from_array)

# Method D: From a Python Dictionary
# This is incredibly fast and intuitive. Pandas automatically uses the
# dictionary 'keys' as the index and the 'values' as the data points.
series_from_dict = pd.Series(my_dict)
print("\nFrom a Python Dictionary:\n", series_from_dict)


# 3) Accessing Data in a Series (Bonus)
print("\n--- 3) Accessing Series Data ---")

# Once you have a labeled Series, you can grab data using those labels
# just like you would with a dictionary.
print("Grabbing the value at index 'b':", series_with_labels["b"])

# You can also perform basic operations on them. If you add two Series together,
# Pandas will automatically align the data by matching their index labels!
series_two = pd.Series(data=[1, 2, 3], index=["a", "b", "c"])

print(
    "\nAdding two series together (Matches based on index 'a', 'b', 'c'):\n",
    series_with_labels + series_two,
)
