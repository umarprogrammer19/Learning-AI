import numpy as np

# 1) Arithmetic Operations (Element-wise)
print(" 1) Arithmetic Operations ")

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])
print("Array 1:", a1)
print("Array 2:", a2)

# For direct arithmetic, arrays usually need to be the exact same shape.
# Operations are performed "element-wise" (index 0 with index 0, index 1 with index 1, etc.)
print("\nAddition (+):      ", a1 + a2)
print("Subtraction (-):   ", a1 - a2)
print("Multiplication (*):", a1 * a2)
print("True Division (/): ", a1 / a2)
print(
    "Floor Division (//):", a1 // a2
)  # Divides and rounds down to nearest whole number
print("Exponentiation (**):", a1**a2)


# 2) Broadcasting
print("\n 2) Broadcasting ")
# Broadcasting is NumPy's ability to perform operations between arrays of
# different sizes or between an array and a single scalar number.

arr_1d = np.array([10, 20, 30, 40])
print("Original 1D array:", arr_1d)

# NumPy "broadcasts" the 10 to every single element in the array
print("Adding 10 to all elements:", arr_1d + 10)

arr_2d = np.arange(1, 26).reshape(5, 5)
print("\nOriginal 2D Matrix:\n", arr_2d)

# Broadcasting works on matrices too!
print("\nAdding 10 to all matrix elements:\n", arr_2d + 10)
print("\nMultiplying all matrix elements by 2:\n", arr_2d * 2)


# 3) Views (Shallow Copy) vs Deep Copy
print("\n 3) Views vs Copies ")

original_arr = np.arange(1, 11)
print("Original array:", original_arr)

# Slicing creates a "View" (Shallow Copy) of the array, not a new distinct array.
# It shares the same memory as the original array.
arr_view = original_arr[:5]

# If we modify this view in place (e.g., changing all its values to 99)...
arr_view[:] = 99
print("Modified view:", arr_view)

# ...it actually changes the original array too!
print("Original array IS changed!:", original_arr)

# To prevent this, you must explicitly create a Deep Copy using .copy()
safe_array = np.arange(1, 11)
safe_copy = safe_array[:5].copy()
safe_copy[:] = 99  # Modifying the copy...
print("\nNew array (safe):", safe_array)  # ...does NOT change the new original!


# 4) Matrix Operations
print("\n 4) Matrix Operations ")

Matrix_A = np.array([[1, 2], [3, 4]])
Matrix_B = np.array([[5, 6], [7, 8]])

# Remember: Matrix_A * Matrix_B would just do element-by-element multiplication.
# To do proper algebraic Matrix Multiplication (Dot Product), use @ or np.dot()
print("Dot Product using @ operator:\n", Matrix_A @ Matrix_B)
print("\nDot Product using np.dot():\n", np.dot(Matrix_A, Matrix_B))

Matrix_C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Matrix_D = np.array([[9, 4, 5], [1, 3, 2], [7, 6, 8]])

CD_product = np.dot(Matrix_C, Matrix_D)
print("\nProduct of 3x3 Matrices C and D:\n", CD_product)

# .T stands for Transpose. It flips the matrix over its diagonal,
# switching its rows into columns and its columns into rows.
print("\nTransposed CD Matrix (CD.T):\n", CD_product.T)


# 5) Advanced Array Manipulation
print("\n 5) Stacking Arrays ")

vec_a = np.array([1, 2, 3, 4])
vec_b = np.array([5, 6, 7, 8])

# vstack() stacks arrays vertically (row wise).
# Note: You must pass the arrays inside a tuple: (vec_a, vec_b)
print("Vertical Stack:\n", np.vstack((vec_a, vec_b)))

# hstack() stacks arrays horizontally (column wise).
print("\nHorizontal Stack:", np.hstack((vec_a, vec_b)))

# column_stack() stacks 1D arrays as columns into a 2D array.
print("\nColumn Stack:\n", np.column_stack((vec_a, vec_b)))


print("\n 6) Splitting Arrays ")
matrix_to_split = np.arange(16).reshape(4, 4)
print("Original 4x4 matrix:\n", matrix_to_split)

# np.hsplit() splits an array into multiple sub-arrays horizontally (column-wise).
# Splitting into 2 means taking 4 columns and making two arrays of 2 columns each.
print("\nHorizontal Split (into 2 parts):")
h_splits = np.hsplit(matrix_to_split, 2)
print("Part 1:\n", h_splits[0])
print("Part 2:\n", h_splits[1])

# If you tried np.hsplit(matrix_to_split, 3), it would throw an error because
# 4 columns cannot be divided evenly into 3 parts.

# np.vsplit() splits an array vertically (row-wise).
print("\nVertical Split (into 2 parts):")
v_splits = np.vsplit(matrix_to_split, 2)
print("Part 1:\n", v_splits[0])
print("Part 2:\n", v_splits[1])


# 7) Iterating over Arrays
print("\n 7) Iterating Over a 2D Array ")

# When you iterate over a 2D array in a standard for-loop,
# it iterates row by row.
for row in matrix_to_split:
    print("Row:", row)
