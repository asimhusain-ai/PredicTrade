**📈 Stock Price Prediction**
Stock Price Prediction — An intelligent, ML-powered app built with Streamlit that predicts future stock prices using historical data and time-series forecasting models. Designed for learning, experimentation, and demonstrating AI-driven market forecasting techniques.


**🌐 Live Demo**

Try the app here: https://predictrade.streamlit.app

⚠️ This project is for educational and research purposes only. Not financial advice.


**🧠 Project Overview**
This Stock Price Prediction app uses Streamlit for the frontend interface and Python for all backend logic, combining simplicity and power in one codebase. Users can input stock ticker symbols, view historical data charts, and generate AI-powered short-term predictions. 

Built with libraries like yfinance, Pandas, and Scikit-learn, it makes real-time stock prediction accessible to anyone.
Key goals:

Provide an interactive UI without needing separate frontend/backend setup.

Fetch, visualize, and predict stock data in one streamlined Python app.

Demonstrate multiple forecasting models (e.g., Linear Regression, Prophet, LSTM).


**✨ Key Features**

Search any stock ticker to fetch real-time and historical data

ML-powered price predictions (configurable time horizon)

Interactive charts for prices vs predictions

Works entirely in the browser via Streamlit

Minimal setup — just run the Python file to start


**🛠 Technology Used**

yfinance, Alpha Vantage API (optional)

ML/Analysis

Pandas, NumPy, Scikit-learn, Prophet, TensorFlow/Keras (optional for LSTM)

Charts

Matplotlib, Plotly

Hosting

Streamlit Cloud 


**🚀 Quick Start (Local)**

Requires Python 3.9+

Clone the repo:

git clone https://github.com/your-username/stock-price-prediction.git

cd stock-price-prediction

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

Open the local URL shown in the terminal (default: http://localhost:8501).


**🔬 Models & How They Work**

Simple Moving Average (SMA) — Baseline using rolling averages

Linear Regression — Prediction based on lag features

Prophet — Captures trends and seasonality

LSTM — Deep learning model for time-series data (optional)

Workflow:

Fetch historical adjusted close prices

Preprocess data (cleaning, lag features, scaling)

Train and validate model

Display prediction alongside historical chart in Streamlit UI


**📈 Evaluation Metrics**

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

MAPE (Mean Absolute Percentage Error)


**⚠️ Limitations & Disclaimer**

Predictions are based only on historical prices — no external market signals.

Market events can cause unexpected price movements.

For educational purposes only.


**👨‍💻 Author**

Made with ❤️ by Asim Husain — https://asimhusain.vercel.app
