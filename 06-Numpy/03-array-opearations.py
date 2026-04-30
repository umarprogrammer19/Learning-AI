import numpy as np

# Arithematic Opearations
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])
# a2 = np.array([6, 7, 8, 9, 10, 11]) # If this it will throws an error
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
print(a1 // a2)
print(a1**a2)

# Broadcasting
l = [10, 20, 30, 40]
arr = np.array(l)
print(arr + 10)

arr2 = np.arange(1, 26).reshape(5, 5)
print(arr2 + 10)
print(arr2 * 2)

# Deep And Shallow Copy
a = np.arange(1, 21)
slice = a[:5]
print(slice * 10)

# Matrix Opearations

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)
print(np.dot(A, B))

C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
D = np.array([[9, 4, 5], [1, 3, 2], [7, 6, 8]])
print(np.dot(C, D))
