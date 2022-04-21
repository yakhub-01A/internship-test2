
import pandas as pd
data = pd.read_csv("main.csv")
data = data.sort_values(by = ["Red Cards","Yellow Cards"],ascending = False)
data.to_csv("main.csv", index = False)

