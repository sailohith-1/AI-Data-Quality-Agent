import pandas as pd

df = pd.read_csv("data/games.csv")

print(df)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate records:")
print(df[df.duplicated()])

print("\nNegative purchase amounts:")
print(df[df["purchase_amount"] < 0])

print("\nNegative session minutes:")
print(df[df["session_minutes"] < 0])