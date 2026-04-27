import numpy as np

# 1) Basic Array Creation
print("\n--- 1) Basic Array Creation ---")

# Creating a basic 1-Dimensional array from a Python list
arr_1d = np.array([1, 2, 3, 4])
print("Basic 1D array:\n", arr_1d)

# NumPy arrays must contain a single data type.
# If you mix types, NumPy automatically "upcasts" them to the most complex type.
# Here, integer (1, 2), float (3.5), and boolean (False) all become floats.
mixed_list = [1, 2, 3.5, False]
arr_mixed = np.array(mixed_list)
print("\nMixed types upcasted to floats (False becomes 0.):\n", arr_mixed)

# Creating a 2-Dimensional array (a matrix) from a list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_2d = np.array(list_of_lists)
print("\n2D array (Matrix):\n", arr_2d)

# 2) Array Generation Functions
print("\n--- 2) Array Generation Functions ---")

# np.arange(start, stop) works like Python's built-in range().
# It generates values from 'start' up to (but not including) 'stop'.
arr_range = np.arange(1, 11)
print("Arange (1 to 10):\n", arr_range)

# np.zeros() creates an array filled with exact zeros. Great for initializing placeholders.
arr_zeros_1d = np.zeros(6)
print("\n1D array of zeros:\n", arr_zeros_1d)

# Pass a tuple (rows, columns) to create a 2D array of zeros.
arr_zeros_2d = np.zeros((4, 8))
print("\n2D array of zeros (4 Rows, 8 Columns):\n", arr_zeros_2d)

# np.linspace(start, stop, num) generates exactly 'num' evenly spaced values
# between 'start' and 'stop'. (Inclusive of the stop value by default).
arr_linspace = np.linspace(1, 10, 5)  # Changed to 5 values for easier viewing
print("\nLinspace (5 evenly spaced points between 1 and 10):\n", arr_linspace)

# 3) Random Generation Functions
print("\n--- 3) Random Generation Functions ---")

# np.random.rand() creates an array of the given shape filled with random
# numbers from a uniform distribution over [0, 1).
rand_uniform = np.random.rand(3)  # Changed to 3 for easier viewing
print("Random uniform values [0, 1):\n", rand_uniform)

# np.random.randn() returns samples from the "standard normal" distribution
# (mean of 0, variance of 1). It includes negative numbers.
rand_normal = np.random.randn(3)
print("\nRandom standard normal values:\n", rand_normal)

# np.random.randint(low, high, size) returns random integers.
rand_int_single = np.random.randint(10)  # One random int from 0 to 9
print("\nSingle random integer (0-9):", rand_int_single)

rand_int_array = np.random.randint(10, 20, 8)  # 8 random ints from 10 to 19
print("Array of 8 random integers (10-19):\n", rand_int_array)


# 4) Array Attributes
print("\n--- 4) Array Attributes ---")
# Attributes are properties of the array object (no parentheses needed).

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Inspecting this matrix:\n", matrix)

# .shape returns a tuple representing the dimensions (rows, columns)
print("Shape (rows, cols):", matrix.shape)

# .size returns the total number of elements in the array
print("Total size (number of elements):", matrix.size)

# .dtype returns the data type of the elements inside the array (e.g., int32, float64)
print("Data type:", matrix.dtype)


# 5) Array Methods
print("\n--- 5) Array Methods ---")
# Methods are functions that belong to the array object (parentheses needed).

print("Matrix min value:", matrix.min())
print("Matrix max value:", matrix.max())
print("Sum of all elements:", matrix.sum())

# The 'axis' parameter is crucial in NumPy:
# axis=0 means "perform operation down the columns"
print("Sum down the columns (axis=0):", np.sum(matrix, axis=0))

# axis=1 means "perform operation across the rows"
print("Sum across the rows (axis=1):", np.sum(matrix, axis=1))

# Statistical methods
print("Mean (average) of all elements:", matrix.mean())
print("Standard deviation of all elements:", matrix.std())

# argmax() and argmin() return the *index* (position) of the max/min value,
# not the value itself. It flattens the array first to find the index.
print("Index of maximum value:", matrix.argmax())
print("Index of minimum value:", matrix.argmin())


# 6) Reshaping and Resizing
print("\n--- 6) Reshaping ---")

# Create a 1D array with 30 elements
arr_30 = np.arange(1, 31)
print("Original 1D array (30 elements):\n", arr_30)

# .reshape() changes the dimensions of the array without changing its data.
# Note: The new shape must perfectly fit the number of elements (6 rows * 5 cols = 30).
reshaped_arr = arr_30.reshape(6, 5)
print("\nReshaped into 6 rows and 5 columns:\n", reshaped_arr)
