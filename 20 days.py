#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance as yf
import pandas as pd

def calculate_20_day_low(stock):
    # Get historical data
    the_stock = yf.Ticker(stock)
    hist = the_stock.history(period="1mo")

    # Calculate the 20-day low
    twenty_day_low = hist['Low'].rolling(window=20).min().iloc[-1]

    return twenty_day_low

# List all stocks
url = "ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt"
df = pd.read_csv(url, sep="|")
common_stock_df = df.loc[df['Market Category'] == 'S']  # Filter by common stocks

for stock in common_stock_df['Symbol']:
    try:
        # Calculate the 20-day low
        twenty_day_low = calculate_20_day_low(stock)

        # Fetch the current price
        current_price = yf.Ticker(stock).history(period="1d")['Close'].iloc[-1]

        # Compare the current price to the 20-day low
        if current_price <= twenty_day_low * 1.1:  # Check if current price is within 10% of the low
            print(f"Stock: {stock} - Current Price: {current_price} - 20-day Low: {twenty_day_low}")

    except IndexError:
        print(f"Error fetching data for stock: {stock}. Skipping...")

    except Exception as e:
        print(f"Error occurred for stock: {stock}. {str(e)}")


# In[ ]:




