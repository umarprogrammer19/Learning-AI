import numpy as np

# Columns: [Age, Math Marks, Science Marks]
data = np.array(
    [
        [18, 85, 78],  # Student 1
        [19, 92, 88],  # Student 2
        [17, 76, 95],  # Student 3
        [18, 65, 70],  # Student 4
        [20, 90, 85],  # Student 5
    ]
)

# 1) Get the shape of the matrix.
shape_of_matrix = data.shape

# 2) Find the average age of students.
average = np.mean(data[:, 0])

# 3) Extract Math Marks of all students
maths_marks = data[:, 1]

# 4) Find The Highest Science Marks
max_science = np.max(data[:, 2])

