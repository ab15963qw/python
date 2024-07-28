import twstock
import pandas as pd

# Define the target stock and fetch data
target_stock = '0050'
stock = twstock.Stock(target_stock)
target_price = stock.fetch_from(2024, 5)

# Define column names
name_attribute = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change', 'Transaction']

# Correctly create a DataFrame
df = pd.DataFrame(data=target_price, columns=name_attribute)

# Print the DataFrame to verify
print(df)
