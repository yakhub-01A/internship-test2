
import pandas as pd
vegetables = pd.read_csv("main.csv")
vegetables.groupby('product_description')['price'].mean()
vegetables["sales_amount"]=vegetables["sales_quantity"].where(vegetables["unit"] !="pcs",vegetables["product_description"].str.split("-",expand=True)[1].astype("float") *
vegetables["sales_quantity"]
)
vegetables.to_csv('main.csv',index=False)