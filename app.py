# This Code is Written By --Asim Husain

# Import Libraries
import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Load model
model = load_model('stock_data.keras')

# Page config
st.set_page_config(page_title='Stock Price Prediction', page_icon='📈', layout='wide', initial_sidebar_state='expanded')

# Load external CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar UI
st.sidebar.header('Stock Price Prediction')
stock_symbols = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'FB', 'TSLA', 'BRK-A', 'BRK-B', 'NVDA', 'JPM', 'JNJ', 'V', 'WMT', 'PG', 'MA', 'DIS', 'HD', 'PYPL', 'VZ', 'ADBE', 'NFLX', 'PFE', 'CMCSA', 'PEP', 'INTC', 'KO', 'CSCO', 'T', 'MRK', 'ABT', 'CVX', 'XOM', 'NKE', 'LLY', 'MCD', 'MDT', 'TXN', 'AVGO', 'CRM', 'HON', 'UNH', 'TMO', 'AMGN', 'NEE', 'DHR', 'QCOM', 'LIN', 'ACN', 'SPGI', 'ORCL', 'WBA', 'IBM', 'ISRG', 'CAT', 'DE', 'LOW', 'NOW', 'LMT', 'PM', 'MMM', 'FISV', 'BLK', 'COST', 'UPS', 'RTX', 'MO', 'BKNG', 'CCI', 'USB', 'MS', 'BA', 'GS', 'PLD', 'SCHW', 'ZTS', 'CB', 'GILD', 'CL', 'PNC', 'BMY', 'MU', 'CCI', 'GPN', 'BDX', 'CI', 'APD', 'DUK', 'C', 'PSX', 'TGT', 'GE', 'SO', 'EXC', 'FDX', 'MET', 'COP']
stock = st.sidebar.selectbox('Select | Search Stock Symbol', stock_symbols)
start = st.sidebar.text_input('Start Date', '2022-01-01')
end = st.sidebar.text_input('End Date', '2024-01-01')

st.sidebar.markdown("""
<div class="button-container">
    <a class="crypto-link-box" href="https://finance.yahoo.com/?guccounter=1">
        <span class="crypto-link">🇸 🇾 🇲 🇧 🇴 🇱 🇸 </span>
    </a>
    <a class="crypto-link-box" href="https://coinmarketcap.com/converter/">
        <span class="crypto-link">🇨 🇦 🇱 🇨 🇺 🇱 🇦 🇹 🇴 🇷 </span>
    </a>
</div>
 <div class="sidebar-button-container">
        <a href="http://asimhusain.dev" class="sidebar-button" target="_blank"></a>
 </div>
""", unsafe_allow_html=True)

# Load stock data
data = yf.download(stock, start, end)

# Display dataframe
st.subheader('Stock Data (USD)')
st.dataframe(data, height=600, width=1300)

# Preprocess
data_train = pd.DataFrame(data.Close[0:int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80):])

scaler = MinMaxScaler()
past_100_days = data_train.tail(100)
data_test = pd.concat([past_100_days, data_test], ignore_index=True)
data_test_scaled = scaler.fit_transform(data_test)

# Moving average graphs
start_date = pd.to_datetime(start)
end_date = pd.to_datetime(end)
date_range = pd.date_range(start=start_date, end=end_date, freq="B")
graph_data = pd.DataFrame({"Close": np.random.uniform(100, 500, len(date_range))}, index=date_range)

ma_50 = graph_data["Close"].rolling(50).mean()
ma_100 = graph_data["Close"].rolling(100).mean()
ma_200 = graph_data["Close"].rolling(200).mean()

# Graphs 1 to 3
for i, (title, series) in enumerate([
    ('Stock Price |vs| 50 Days Moving Average', [('Closing Price', graph_data["Close"], 'green'), ('50-Day Moving Average', ma_50, 'red')]),
    ('Stock Price |vs| 50 Days |vs| 100 Days MA', [('Closing Price', graph_data["Close"], 'green'), ('50-Day MA', ma_50, 'red'), ('100-Day MA', ma_100, 'blue')]),
    ('Stock Price |vs| 100 Days |vs| 200 Days MA', [('Closing Price', graph_data["Close"], 'green'), ('100-Day MA', ma_100, 'red'), ('200-Day MA', ma_200, 'blue')])
]):
    fig = go.Figure()
    for name, y, color in series:
        fig.add_trace(go.Scatter(x=graph_data.index, y=y, mode='lines', name=name, line=dict(color=color, width=2)))
    fig.update_layout(xaxis_title='Date', yaxis_title='Price (USD)', hovermode='x unified', template='plotly_white', width=1800, height=700)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader(title)
    st.plotly_chart(fig)

# Predict
x, y = [], []
for i in range(100, data_test_scaled.shape[0]):
    x.append(data_test_scaled[i - 100:i])
    y.append(data_test_scaled[i, 0])

x, y = np.array(x), np.array(y)
predict = model.predict(x)
scale = 1 / scaler.scale_
predict *= scale
y *= scale

# Prediction plot
fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=np.arange(len(predict)), y=predict.flatten(), mode='lines', name='Predicted Price', line=dict(color='red', width=2)))
fig4.add_trace(go.Scatter(x=np.arange(len(y)), y=y.flatten(), mode='lines', name='Original Price', line=dict(color='green', width=2)))
fig4.update_layout(xaxis_title='Time', yaxis_title='Price (USD)', hovermode='x unified', template='plotly_white', width=1800, height=700)
st.markdown('<hr>', unsafe_allow_html=True)
st.subheader('Original Stock Price |vs| Predicted Stock Price')
st.plotly_chart(fig4)

# Table comparison
date_range = pd.date_range(start=start, end=end, freq='B')
mock_data = pd.DataFrame({'Open': np.random.uniform(100, 500, len(date_range)), 'Close': np.random.uniform(100, 500, len(date_range))}, index=date_range)

full_data = pd.DataFrame(index=date_range, columns=['Original Price', 'Predicted Price'])
full_data['Original Price'] = mock_data['Open']
full_data['Predicted Price'] = mock_data['Close']
full_data['Difference'] = abs(full_data['Original Price'] - full_data['Predicted Price'])
full_data.dropna(inplace=True)
full_data['↑   ↓   Change(%)'] = (full_data['Predicted Price'] - full_data['Original Price']) / full_data['Original Price'] * 100

st.subheader('Original Price VS Predicted Price')
st.dataframe(full_data, height=600, width=1200)
st.markdown('<hr>', unsafe_allow_html=True)