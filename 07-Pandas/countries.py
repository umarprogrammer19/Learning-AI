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

# How many total regions are there
regions = df["region"].value_counts().count()

# how many countries lie in Eastern Europe region
eastern_europe_region = df["region"].value_counts()["Eastern Europe"]

# who is the political leader of the 2nd highest populated country
pl = df[df["population"] == df["population"].nlargest(2).iloc[1]]["political_leader"]

# how many countries are there whoes political leaders are unknown
count_unknown = df[df["political_leader"].isna()].value_counts("country").count()

# how many country have Republic in their full name
count = 0


def counting(text):
    global count
    if "republic" in text.lower():
        count += 1
    return text


df["country_long"].apply(counting)

# which country in african region has highest population
africa_df = df[df["continent"] == "Africa"]
total = africa_df[africa_df["population"] == africa_df["population"].max()]["country"]
