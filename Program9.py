import pandas as pd
df = pd.read_csv("temperatures.csv")

df['date'] = pd.to_datetime(df['date'],format='%y-%m-%d')
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = df[(df["date"] >= "2010-01-01") & (df["date"] <= "2011-12-31")]
print(temperatures_bool)

