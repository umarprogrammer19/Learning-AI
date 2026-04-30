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
CD = np.dot(C, D)
print(CD)
print(CD.T)

# Advance Array Manipulation

# Stacking Arrays (Vectors)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Vertical Stack
print(np.vstack((a, b)))

# Horizontal Stack
print(np.hstack((a, b)))

# Column Stack
print(np.column_stack((a, b)))

# Splitting Arrays
c = np.arange(16).reshape(4, 4)
print(c)

# Horizontal Split
print(np.hsplit(c, 2))
# print(np.hsplit(c, 3)) # Error array split does not result in an equal division
print(np.hsplit(c, 4))

# Vertical Split
print(np.vsplit(c, 2))

for i in c:
    print(c)
