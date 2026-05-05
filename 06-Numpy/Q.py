import numpy as np

# Student Dataset Initialization
# Columns represent: [Age, Math Marks, Science Marks]
data = np.array(
    [
        [18, 85, 78],  # Student 1
        [19, 92, 88],  # Student 2
        [17, 76, 95],  # Student 3
        [18, 65, 70],  # Student 4
        [20, 90, 85],  # Student 5
    ]
)

print("--- Original Student Data ---")
print("Columns: [Age, Math, Science]")
print(data)


# 1) Get the shape of the matrix
print("\n--- 1) Matrix Shape ---")
shape_of_matrix = data.shape
print(f"Shape: {shape_of_matrix} -> (5 students/rows, 3 attributes/columns)")


# 2) Find the average age of students
print("\n--- 2) Average Age ---")
# data[:, 0] grabs ALL rows (:), but ONLY the first column (index 0 - Age)
average_age = np.mean(data[:, 0])
print(f"Average Age: {average_age}")


# 3) Extract Math Marks of all students
print("\n--- 3) All Math Marks ---")
# Grabbing ALL rows (:), but ONLY the second column (index 1 - Math)
maths_marks = data[:, 1]
print(f"Math Marks: {maths_marks}")


# 4) Find The Highest Science Marks
print("\n--- 4) Highest Science Score ---")
# Grabbing ALL rows (:), but ONLY the third column (index 2 - Science)
max_science = np.max(data[:, 2])
print(f"Highest Science Mark: {max_science}")


# 5) Get Details of the student who scored > 90 in Math
print("\n--- 5) Students with Math > 90 ---")
# data[:, 1] > 90 creates a boolean mask [False, True, False, False, False]
# Passing that mask back into the array filters it to only the 'True' rows
student_math_genius = data[data[:, 1] > 90]
print(student_math_genius)


# 6) Increase Math Marks Of All Students By 5
print("\n--- 6) Bumping Math Marks by 5 ---")
# This modifies the original array in-place!
# The new math scores will be used for all following steps.
data[:, 1] = data[:, 1] + 5
print("Updated Data (Math scores increased):")
print(data)


# 7) Find How many students are younger than 19
print("\n--- 7) Count of Students Younger Than 19 ---")
# Your method: Filter the array and check its length
younger_count = len(data[data[:, 0] < 19])

# Pro-Tip Method: A boolean mask evaluates to 1s (True) and 0s (False).
# You can just sum the mask directly to get the count!
# younger_count = np.sum(data[:, 0] < 19)

print(f"Number of students under 19: {younger_count}")


# 8) Calculate the average marks in each subject
print("\n--- 8) Average Marks per Subject ---")
# data[:, 1:] grabs ALL rows, and columns from index 1 to the end (Math & Science)
subjects_data = data[:, 1:]

# axis=0 means "calculate down the columns" (giving one average per subject)
subject_averages = np.mean(subjects_data, axis=0)
print(f"Average Math Mark: {subject_averages[0]}")
print(f"Average Science Mark: {subject_averages[1]}")


# 9) Get the students who scored at least 80 in BOTH subjects
print("\n--- 9) Top Performers (>= 80 in Math AND Science) ---")
# When combining boolean conditions in NumPy arrays, you must wrap each
# condition in parentheses () and use the bitwise '&' operator instead of 'and'.
top_students = data[(data[:, 1] >= 80) & (data[:, 2] >= 80)]
print(top_students)


# 10) Replace all Science Marks < 75 with 0
print("\n--- 10) Penalty: Science Marks < 75 set to 0 ---")
# data[:, 2] < 75 finds the rows where Science is less than 75.
# The ', 2' targets the exact column (Science) where the replacement should happen.
data[data[:, 2] < 75, 2] = 0
print("Final Updated Data:")
print(data)
