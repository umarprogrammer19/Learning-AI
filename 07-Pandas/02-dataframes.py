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

