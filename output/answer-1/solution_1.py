
import pandas as pd
q1_data = pd.read_csv("main.csv")
q1_data.head()
q1_data.groupby("product_description")['price'].mean()
q1_data["price_new"] = q1_data['price'].fillna(q1_data.groupby("product_description")['price'].transform("mean"))
q1_data[q1_data["price"].isna()].head()
q1_data.to_csv('main.csv',index=False)