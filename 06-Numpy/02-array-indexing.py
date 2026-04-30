import numpy as np

# ==========================================
print(" 1) 1D Array Indexing and Slicing ")

# Creating a 1D array (vector) from 11 to 20
vector = np.arange(11, 21)
print("Original 1D array:\n", vector)

# Indexing: Grabbing a single element. Python is 0-indexed.
print("\nElement at index 6 (7th item):", vector[6])

# Slicing syntax: array[start_index : stop_index : step]
# The 'stop_index' is exclusive (it goes up to, but doesn't include it).
print("Elements from index 1 to 4 (1:5):", vector[1:5])
print("Elements from start to index 4 (:5):", vector[:5])
print("All elements ([:]):", vector[:])
print("Elements from index 3 to the end (3:):", vector[3:])

# This returns an empty array because the start index (3) is greater than
# the stop index (2) while stepping forward.
print("Elements from index 3 to 2 (3:2):", vector[3:2])

# Slicing with a step. Start at index 3, stop before 8, take every 2nd element.
print("Elements from index 3 to 7, skipping by 2 (3:8:2):", vector[3:8:2])

# Best Practice: Slicing returns a "view" of the original array.
# If you want to modify a slice without accidentally changing the original array,
# you should save it as a distinct copy using .copy()
saved_slice = vector[1:5].copy()


# 2) NumPy Indexing and Slicing of Matrices (2D Arrays)
print("\n 2) 2D Array (Matrix) Indexing and Slicing ")

# Creating a 6x5 matrix
matrix = np.arange(1, 31).reshape(6, 5)
print("Original 2D Matrix:\n", matrix)

# Grabbing entire rows
print("\nEntire Row 0 (1st row):", matrix[0])
print("Entire Row 1 (2nd row):", matrix[1])
print("Entire Row 5 (6th row):", matrix[5])

# Grabbing specific elements using matrix[row, column]
print("\nElement at Row 0, Column 3:", matrix[0, 3])
print("Element at Row 5, Column 4:", matrix[5, 4])

# 2D Slicing syntax: matrix[row_start : row_stop , col_start : col_stop]
# If you want the specific block:
#  [2, 3]
#  [7, 8]
# These are located in rows 0 and 1 (slice 0:2) and columns 1 and 2 (slice 1:3).
print("\nExtracting a 2x2 sub-matrix (Rows 0-1, Cols 1-2):")
print(matrix[0:2, 1:3])

# Slicing from row 3 to the end, and column 3 to the end
print("\nBottom-right corner (Rows 3 to end, Cols 3 to end):\n", matrix[3:, 3:])

# Grabbing an entire column. ':' means "give me all rows", then '2' means "column 2".
print("\nEntire Column 2 (3rd column):", matrix[:, 2])


# 3) Boolean Indexing (Filtering)
print("\n 3) Boolean Indexing ")

# Re-creating our 1D vector
vector = np.arange(11, 21)
print("Original vector:\n", vector)

# Creating a boolean "mask". This checks every element to see if it is divisible by 2.
# It returns an array of True/False values of the exact same size.
bool_mask = vector % 2 == 0
print("\nBoolean mask (True where element is even):\n", bool_mask)

# Passing the boolean mask into the array brackets filters the array.
# It only keeps the elements where the mask is True.
even_numbers = vector[bool_mask]
print("\nFiltered array (only even numbers):\n", even_numbers)

# Pro-tip: You can do this in one single line without saving.
print(vector[vector % 2 == 0])
