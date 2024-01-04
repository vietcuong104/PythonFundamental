import csv
import pandas as pd

data = {"Name" : ["Duong", "Lam", "Nguyet", "Tung"],
        "Age" : [28, 26, 27, 30]}
data = pd.DataFrame(data)
data.to_csv("actors.csv", index=False)
print(data.head())