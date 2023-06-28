import requests
import plotly.graph_objects as go
import pandas as pd
import pandas_ta as TA

# 8 runs per minute 
# max 800 requesuts

url = "https://api.twelvedata.com/time_series"
api_key = "0cd77d4c6bb64776a65ff04c56409016"
symbol = "AAPL"
start_date = "2018-06-25"
end_date = "2023-06-25"
interval = "5min"
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
    df["high"] = pd.to_numeric(df["high"], downcast="float")
    df["low"] = pd.to_numeric(df["low"], downcast="float")
    # Calculate Parabolic SAR
    dbf = TA.psar(df['high'], df['low'])
    df['sar'] = dbf['PSARl_0.02_0.2'].fillna(dbf['PSARs_0.02_0.2'])
    print(df['sar'])
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
