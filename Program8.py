import pandas as pd
temperatures = pd.read_csv("temperatures.csv")



# Make a list of cities to subset on
cities = ["Cape Town", "Casablanca"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])