import streamlit as st
import pandas as pd
import numpy as np
import talib as ta
import os
from lightweight_charts.widgets import StreamlitChart
from lightweight_charts.abstract import Line 
import datetime

def main():
    st.set_page_config(layout="wide")
    st.title('Stock Price Viewer')

    col1, col2 = st.columns(2)
    with col1:
        # User input for market name
        market_name = st.text_input('Enter the market name (e.g., AAPL):', 'AAPL')

        # User input for timeframe
        timeframe = st.selectbox('Select timeframe:', ['5min', '15min', '30min', '45min', '1hr', '2hr', '4hr', '1d', '1wk'], index=0)
    with col2:
        indicator_name = st.text_input('Enter indicators (e.g., SMA):')

        options = st.text_input('Enter options (e.g., SMA):')
    # Load data from the corresponding CSV file
    df = load_csv_data(market_name, timeframe)
    print(df["Date"].max())
    print(df["Date"].min())
    date_selection = st.checkbox('Toggle Date Selection')
    min_date = pd.to_datetime(df["Date"].min()).date()
    max_date = pd.to_datetime(df["Date"].max()).date()+datetime.timedelta(days=1)
    with col1:
        selected_date_start = st.date_input("Start Date", min_value=min_date, max_value=max_date, value=min_date)
    with col2:
        selected_date_end = st.date_input("End Date", min_value=min_date, max_value=max_date,value=max_date)
    technical_df,mutlival = calc_inidcators(df,indicator_name,options)
    print(technical_df)
    print(mutlival)
    if df is not None:
        batched_data = create_date_batch(df,selected_date_start,selected_date_end,date_selection)
        indicator_batched_data = create_date_batch(technical_df,selected_date_start,selected_date_end,date_selection)
        multi_indicator_batched_data = create_date_batch(mutlival,selected_date_start,selected_date_end,date_selection)
        # Get or create the current page using caching
        current_page = st.experimental_get_query_params().get('page', [0])[0]
        current_page = int(current_page) if current_page else 0
        print("Cuurent Page: ", current_page)
        # Display the chart
        display_chart(batched_data,indicator_batched_data, current_page,indicator_name,options,multi_indicator_batched_data)

def load_csv_data(market_name, timeframe):
    # Define the directory where the CSV files are stored
    data_dir = 'Hist'

    # Construct the CSV file path
    file_path = os.path.join(data_dir, market_name, f"{timeframe}.csv")

    # Load data from the CSV file
    try:
        df = pd.read_csv(file_path).drop_duplicates(subset=['Date'],keep='last')
        df['date'] = df["Date"]
        df = df.set_index('date')
        print(df)
        return df
    except FileNotFoundError:
        st.warning(f"No CSV file found for market '{market_name}' and timeframe '{timeframe}'")
        return None


def calc_inidcators(df,indicator_name,options):
    indicator_names = indicator_name.split("-")
    indicator_values = options.split("-")
    cols = []
    for i in range(len(indicator_name.split("-"))):
        cols.append(indicator_name.split("-")[i]+options.split("-")[i])
    # blacklist = ['MACD','SAR']
    # diff = [item for item in cols if any(substring in item for substring in blacklist)]
    # same = [item for item in cols if not any(substring in item for substring in blacklist)]
    results = {}
    multi_df = pd.DataFrame()
    close = np.array(df["Close"])
    high = np.array(df["High"])
    low = np.array(df["Low"])
    date = np.array(df["Date"])
    print(indicator_names)
    for i in range(len(indicator_names)): 
        if indicator_names[i] == 'MACD':
            multi_val = indicator_values[i].replace("(","").replace(")","").split(",")
            value = getattr(ta, indicator_names[i])(close, int(multi_val[0]),int(multi_val[1]),int(multi_val[2]))
            col_names = ['MACD'+indicator_values[i],'MACD_Signal'+indicator_values[i],'MACD_Hist']
            temmpdf = pd.DataFrame(value).T.rename(columns={0: col_names[0], 1: col_names[1], 2: col_names[2]}).drop(['MACD_Hist'],axis=1)
            multi_df[col_names[0]] = temmpdf[col_names[0]]
            multi_df[col_names[1]] = temmpdf[col_names[1]]
        elif indicator_names[i] == 'SAR':
            multi_val = indicator_values[i].replace("(","").replace(")","").split(",")
            value = getattr(ta, indicator_names[i])(high,low, float(multi_val[0]),float(multi_val[1]))
            results[cols[i]] = value
        else:
            value = getattr(ta, indicator_names[i])(close, int(indicator_values[i]))
            results[cols[i]] = value
    # print(results)
    technical_df = pd.DataFrame(results)
    technical_df['date'] = date
    technical_df = technical_df.set_index('date')
    multi_df['date'] = date
    multi_df = multi_df.set_index('date')
    return technical_df, multi_df
    


def create_date_batch(df, start_date, end_date,date_selection):
    start_date = str(pd.to_datetime(start_date).date())
    end_date = str(pd.to_datetime(end_date).date())
    if not date_selection:
        return [df]
    else:    
        return [df.loc[start_date:end_date]]

def display_chart(batched_data, indicator_batched_data, current_page,indicator_name,options,multi_indicator_batched_data):
    colors = ["white","red","blue","green","purple","orange"]
    OffCharts = ['RSI','MACD']
    cols = []
    for i in range(len(indicator_name.split("-"))):
        cols.append(indicator_name.split("-")[i]+options.split("-")[i])
    Seperate = [item for item in cols if any(substring in item for substring in OffCharts)]
    print(Seperate)
    Onchart = [item for item in cols if not any(substring in item for substring in OffCharts)]
    print(Onchart)
    if Seperate:
        numofsub = len(Seperate)
        if numofsub == 1:
            inn_height = 0.8
            sub_height = 0.2
            total_height = 600
        else:
            factor = (1-0.1)-numofsub/10
            total_height = 600/factor
            inn_height = factor
            sub_height = ((numofsub/10)+0.1)/numofsub
        chart = StreamlitChart(height=total_height,inner_width=1, inner_height=inn_height,toolbox=True)
        chart.legend(True)
        for i in range(len(Seperate)):
            locals()["chart" + str(i+1)] = chart.create_subchart(width=1, height=sub_height, sync=True, volume_enabled=False)
            locals()["chart" + str(i+1)].legend(True)
    else:
        chart = StreamlitChart(height=600,toolbox=True)
        chart.legend(True)
    # Create a chart with the current batched data
    chart.set(batched_data[current_page])
    if Onchart:
        data_df = indicator_batched_data[current_page]
        for i in range(len(Onchart)):
            if 'SAR' in Onchart[i]:
                locals()["line" + str(i+1)] = chart.create_line(color=colors[i])
            else:
                locals()["line" + str(i+1)] = chart.create_line(color=colors[i])
            locals()["series" + str(i+1)] = data_df[Onchart[i]]
            locals()["df" + str(i+1)] = pd.DataFrame(locals()["series" + str(i+1)], columns=[Onchart[i]]).dropna()
            locals()["line" + str(i+1)].set(locals()["df" + str(i+1)],name=Onchart[i])
    if Seperate:
        data_df = indicator_batched_data[current_page]
        multi_df = multi_indicator_batched_data[current_page]
        for i in range(len(Seperate)):
            if 'MACD' in Seperate[i]:
                names = 'MACD_Signal'+Seperate[i].split("D")[-1]
                locals()["line" + str(i+1)] = locals()["chart" + str(i+1)].create_line(color="red")
                locals()["line" + str(i+2)] = locals()["chart" + str(i+1)].create_line()
                locals()["series" + str(i+1)] = multi_df[Seperate[i]]
                locals()["series" + str(i+2)] = multi_df[names]
                locals()["df" + str(i+1)] = pd.DataFrame(locals()["series" + str(i+1)], columns=[Seperate[i]]).dropna()
                locals()["df" + str(i+2)] = pd.DataFrame(locals()["series" + str(i+2)], columns=[names]).dropna()
                locals()["line" + str(i+1)].set(locals()["df" + str(i+1)],name=Seperate[i])
                locals()["line" + str(i+2)].set(locals()["df" + str(i+2)],name=names)
            else:
                locals()["line" + str(i+1)] = locals()["chart" + str(i+1)].create_line()
                locals()["series" + str(i+1)] = data_df[Seperate[i]]
                print(locals()["series" + str(i+1)])
                locals()["df" + str(i+1)] = pd.DataFrame(locals()["series" + str(i+1)], columns=[Seperate[i]]).dropna()
                locals()["line" + str(i+1)].set(locals()["df" + str(i+1)],name=Seperate[i])
        
    # Display the chart
    chart.load()

    # Create a container for the buttons
    col1, col2 = st.columns(2)

    # Create buttons for navigating forward and backward
    with col1:
        if current_page > 0:
            if st.button('Backward'):
                current_page -= 1
    with col2:
        if current_page < len(batched_data) - 1:
            if st.button('Forward'):
                current_page += 1

    # Update the current page using caching
    st.experimental_set_query_params(page=current_page)

    # Re-render the chart with the updated data when buttons are clicked
    chart.set(batched_data[current_page])
    chart.load()


if __name__ == '__main__':
    main()
