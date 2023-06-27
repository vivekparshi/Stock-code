import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

def extract_historical_stock_data(symbol, period):
    try:
        stock = yf.download(symbol, period=period)
        stock_data = stock[['Open', 'Close', 'High', 'Low', 'Volume']]
        return stock_data
    except Exception as e:
        print(f"An error occurred during data extraction: {e}")
        return None

symbol_of_stock = 'AMZN'
data_period = '1y'
stock_data = extract_historical_stock_data(symbol_of_stock, data_period)
if stock_data is not None:
    print(stock_data.head())


def calculate_average_volume(stock_data):
    try:
        average_volume = stock_data['Volume'].mean()
        return average_volume
    except Exception as e:
        print(f"An error occurred during data processing: {e}")
        return None

average_volume = calculate_average_volume(stock_data)
if average_volume is not None:
    print(f"Average Daily Trading Volume: {average_volume}")


def visualize_stock_performance(stock_data):
    try:
        mpf.plot(stock_data, type='candle', volume=True, show_nontrading=False)
        plt.show()
    except Exception as e:
        print(f"An error occurred during data visualization: {e}")

visualize_stock_performance(stock_data)
