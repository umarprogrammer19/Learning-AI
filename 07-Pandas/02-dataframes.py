import numpy as np
import pandas as pd

# Creating a dataframe
data = {
    "Name": ["Umar", "Raza", "Asad", "Saad"],
    "Age": [28, 34, 29, 42],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [65000, 70000, 62000, 85000],
}

df = pd.DataFrame(data)
print(df)

data_list = [
    ["Umar", 28, "New York", 65000],
    ["Raza", 34, "Paris", 70000],
    ["Asad", 29, "Berlin", 62000],
    ["Saad", 42, "London", 85000],
]
df2 = pd.DataFrame(data_list)
print(df2)
columns = ["Name", "Age", "City", "Salary"]
df2 = pd.DataFrame(data_list, columns)
print(df2)
