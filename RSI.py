# Import all libraries neseccary for the code
import datetime as dt # 
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def stock_price(ticker, start, end):
    dataset = yf.download(ticker, start, end)
    dataset.reset_index(inplace = True)
    return dataset

def closed_dates(dataset):
    time_line = pd.date_range(start = dataset['Date'].iloc[0], end = dataset['Date'].iloc[-1])
    dates = [day.strftime('%Y-%m-%d') for day in pd.to_datetime(dataset['Date'])]