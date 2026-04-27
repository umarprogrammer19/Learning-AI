import numpy as np

### 1) Basic Array Creation
arr = np.array([1, 2, 3, 4])

a = [1, 2, 3.5, False]

np.array(a)
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(l)
### 2) Array Generation function
arr = np.arange(1, 11)
arr = np.zeros(6)

arr = np.zeros((4, 8))  # 4 Rows and 8 Columns
arr = np.linspace(1, 10, 100)
np.random.rand(100)
np.random.randn(10)
np.random.randint(10)
np.random.randint(10, 20, 8)
