import numpy as np
import pandas as pd

data = {
    "Date": pd.date_range("2023-01-01", periods=20),
    "Product": ["A", "B", "C", "D"] * 5,
    "Region": [
        "East",
        "West",
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
    ],
    "Sales": np.random.randint(100, 1000, 20),
    "Units": np.random.randint(10, 100, 20),
    "Rep": [
        "John",
        "Mary",
        "Bob",
        "Alice",
        "John",
        "Mary",
        "Bob",
        "Alice",
        "John",
        "Mary",
        "Bob",
        "Alice",
        "John",
        "Mary",
        "Bob",
        "Alice",
        "John",
        "Mary",
        "Bob",
        "Alice",
    ],
}

df = pd.DataFrame(data)
df["Month"] = df["Date"].dt.month_name()
df["Quarter"] = "Q" + df["Date"].dt.quarter.astype(str)

# Data Frame:
#          Date Product Region  Sales  Units    Rep    Month Quarter
# 0  2023-01-01       A   East    415     23   John  January      Q1
# 1  2023-01-02       B   West    137     58   Mary  January      Q1
# 2  2023-01-03       C  North    729     45    Bob  January      Q1
# 3  2023-01-04       D  South    817     24  Alice  January      Q1
# 4  2023-01-05       A   East    934     52   John  January      Q1
# 5  2023-01-06       B   West    455     12   Mary  January      Q1
# 6  2023-01-07       C  North    558     29    Bob  January      Q1
# 7  2023-01-08       D  South    748     61  Alice  January      Q1
# 8  2023-01-09       A   East    437     98   John  January      Q1
# 9  2023-01-10       B   West    334     36   Mary  January      Q1
# 10 2023-01-11       C  North    670     56    Bob  January      Q1
# 11 2023-01-12       D  South    375     14  Alice  January      Q1
# 12 2023-01-13       A   East    815     25   John  January      Q1
# 13 2023-01-14       B   West    599     39   Mary  January      Q1
# 14 2023-01-15       C  North    280     12    Bob  January      Q1
# 15 2023-01-16       D  South    417     92  Alice  January      Q1
# 16 2023-01-17       A   East    503     88   John  January      Q1
# 17 2023-01-18       B   West    151     95   Mary  January      Q1
# 18 2023-01-19       C  North    853     29    Bob  January      Q1
# 19 2023-01-20       D  South    500     44  Alice  January      Q1

pt = pd.pivot_table(
    df, values="Sales", index="Region", columns="Product", aggfunc="median"
)
print(pt)
pt2 = pd.pivot_table(df, values=["Sales", "Units"], index="Region", columns="Product")
print(pt2)
