import pandas as pd

df = pd.read_csv("Countries.csv")

# which country has highest population
highest_population = df[df["population"] == df["population"].max()]

# what is the capital of country with highest population
highest_population_country_capital = df[df["population"] == df["population"].max()][
    "capital_city"
]

# which country is the least population
lowest_population = df[df["population"] == df["population"].min()]["country"]

# what is the capital of the country with least population
lowest_population_country_capital = df[df["population"] == df["population"].min()][
    "capital_city"
]

# top 5 countries with highest democratic score
df.sort_values(by="democracy_score", ascending=False, inplace=True)
highest_democretic_score = df["country"].head()
