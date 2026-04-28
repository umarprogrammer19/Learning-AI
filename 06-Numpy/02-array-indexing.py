import numpy as np

# Numpy Indexing and Slicing Of Vectors
arr = np.arange(11, 21)
# array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(arr)

print(arr[6])
print(arr[1:5])
print(arr[:5])
print(arr[:])
print(arr[3:])
print(arr[3:2])
print(arr[3:8:2])
# If you are slicing something make sure save it

# Numpy Indexing and Slicing Of Matrix
arr = np.arange(1, 31).reshape(6, 5)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]]
print(arr)
print(arr[0])
print(arr[1])
print(arr[5])
print(arr[0, 3])
print(arr[5, 4])
# if i want 2, 3
#           7, 8
print(arr[0:2, 3:6])
print(arr[3:, 3:])
print(arr[:, 2])
