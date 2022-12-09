import pandas as pd

alles_auf_null = False

url = 'https://raw.githubusercontent.com/bcwodo/lattrain/master/vokabeln.csv'
df = pd.read_csv(url)

if alles_auf_null:
    df["Kartei"] = 1


print(df.head())
df.to_csv("vokabeln.csv", index=False)