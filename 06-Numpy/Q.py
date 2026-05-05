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

# 5) Get Details Of the student who scored more than 90 in maths.
student = data[data[:, 1] > 90]

# 6) Increase Math Marks Of All Student By 5
data[:, 1] = data[:, 1] + 5

# 7) Find How many students are younger than 19
younger = len(data[data[:, 0] < 19])

# 8) Calculate the average marks in each subject.
subjects = data[:, 1:]
average = np.mean(subjects, axis=0)

# 9) Get the student of the data who score at least 80 in both subjects
student_score = data[(data[:, 1] >= 80) & (data[:, 2] >= 80)]

# 10) Replace all Science Marks < 75 with 0.
data[data[:, 2] < 75, 2] = 0
