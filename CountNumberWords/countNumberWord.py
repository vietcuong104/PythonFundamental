import pandas as pd

data = pd.read_csv("articles.csv")
print(data.head())

data["Number of words"] = data["Article"].apply(lambda n: len(n.split()))

print(data.head())
