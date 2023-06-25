# Figure out a way to get the indicators working properly on a local machine, (twelve data), use my api key 
# Use plotly to plot the data
# Find a broker that has low fees, and uses python to execute market orders 24hrs
# Build a strategy price has to be over 200 ema, macd has to crossover signal line, and psar has to be under the candle
# Stop loss is at the psar risk to ratio atleast 1 optimal 1.5 great 2
# Look at other indicators that improve the entry and exit conditions 

# ord and chr functions, math library, objects and methods, reading and processing string characters, includes concationations, reading user inputs ~1-2hr
# Qs ~ 2hrs max


import requests
import plotly.graph_objects as go
import pandas as pd
import talib as TA

# 8 runs per minute 
# max 800 requesuts

url = "https://api.twelvedata.com/time_series"
api_key = "0cd77d4c6bb64776a65ff04c56409016"
symbol = "AAPL"
start_date = "2000-06-25"
end_date = "2023-06-25"
interval = "1day"
data_type = "Common Stock"

params = {
    "apikey": api_key,
    "symbol": symbol,
    "start_date": start_date,
    "end_date": end_date,
    "interval": interval,
    "type": data_type
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Extract candlestick data
    dates = []
    open_prices = []
    high_prices = []
    low_prices = []
    close_prices = []
    for item in data['values']:
        dates.append(item['datetime'])
        open_prices.append(item['open'])
        high_prices.append(item['high'])
        low_prices.append(item['low'])
        close_prices.append(item['close'])
    df = pd.DataFrame({
        'date': dates,
        'open': open_prices,
        'high': high_prices,
        'low': low_prices,
        'close': close_prices
    })

    # Calculate Parabolic SAR
    df['sar'] = TA.SAR(df['high'], df['low'], acceleration=0.02, maximum=0.2)

    # Create figure
    fig = go.Figure()

    # Add candlestick trace
    fig.add_trace(go.Candlestick(x=df['date'],
                                 open=df['open'],
                                 high=df['high'],
                                 low=df['low'],
                                 close=df['close'],
                                 name='Candlesticks'))

    # Add Parabolic SAR trace
    fig.add_trace(go.Scatter(x=df['date'],
                             y=df['sar'],
                             mode='markers',
                             name='Parabolic SAR',
                             marker=dict(color='red')))

    # Update layout
    fig.update_layout(title="Candlestick chart with Parabolic SAR for AAPL",
                      xaxis_title="Date",
                      yaxis_title="Price ($USD)")

    fig.show()
else:
    print("Error occurred:", response.status_code)
