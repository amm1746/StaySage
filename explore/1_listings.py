# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from staysage import config

# readin one city 
listings = pd.read_csv(config.listings_path("austin"), low_memory=False)

print("Rows: ", len(listings))
print("Columns: ", len(listings.columns))


# %%

for column_name in listings.columns:
    print(column_name)

# %%

first_listing = listings.iloc[0]
for column_name in listings.columns:
    value = first_listing[column_name]
    print(column_name, "=", value)
# %%
print("First few prices:")
print(listings["price"].head())
print()
print("Data type:", listings["price"].dtype)
# %%

price_as_text = listings["price"].astype(str)
price_no_dollar = price_as_text.str.replace("$", "", regex=False)
price_no_comma = price_no_dollar.str.replace(",", "", regex=False)
price = pd.to_numeric(price_no_comma, errors="coerce")

print(price.describe())
# %%
reasonable_prices = price[price < 1000]

plt.figure(figsize=(6, 4))
plt.hist(reasonable_prices, bins=60)
plt.title("Price")
plt.xlabel("Price per night")
plt.show()
# %%
#  the logged prices for better model

logged_prices = np.log1p(reasonable_prices)

plt.figure(figsize=(6, 4))
plt.hist(logged_prices, bins=60)
plt.title("The log1p(price)")
plt.xlabel("log of price")
plt.show()
# %%

# printing the emptiest columns
for column_name in listings.columns:
    blanks = listings[column_name].isna()
    percent_blank = blanks.mean() * 100

    if percent_blank > 5:
        print(round(percent_blank, 1), "% blank:", column_name)
# %%
# checking for the cleaning fede
print("Columns with fee in the name:")
for column_name in listings.columns:
    if "fee" in column_name.lower():
        print(" ", column_name)
# %%
# amenities column
first_amenities = listings["amenities"].iloc[0]

print("Type:", type(first_amenities))
print()
print(first_amenities[:300])
# %%
# room type
print(listings["room_type"].value_counts())