# 📈 Stock Price Prediction
An intelligent, ML-powered app built with **Streamlit** that predicts future stock prices using historical data and time-series forecasting models. Designed for learning, experimentation, and demonstrating AI-driven market forecasting techniques.

---

## 🌐 Live Demo
👉 https://predictrade.streamlit.app  

⚠️ *This project is for educational and research purposes only. Not financial advice.*

---

## 🧠 Project Overview
This Stock Price Prediction app uses **Streamlit** for the frontend interface and **Python** for backend logic, combining simplicity and power in one codebase.  

Users can:
- Input stock ticker symbols.  
- View historical data charts.  
- Generate AI-powered short-term predictions.  

Built with **yfinance, Pandas, Scikit-learn**, and optional deep learning tools, it makes real-time stock prediction accessible to anyone.  

**Key Goals:**
- Provide an interactive UI without separate frontend/backend setup.  
- Fetch, visualize, and predict stock data in one streamlined Python app.  
- Demonstrate multiple forecasting models (Linear Regression, Prophet, LSTM).  

---

## ✨ Key Features
- 🔍 Search any stock ticker for real-time & historical data.  
- 🤖 ML-powered price predictions (configurable horizon).  
- 📊 Interactive charts (prices vs predictions).  
- 🌐 Works fully in the browser via Streamlit.  
- ⚡ Minimal setup — run one Python file to start.  

---

## 🛠 Technology Used
**Data & APIs**: yfinance, Alpha Vantage API (optional)  
**ML/Analysis**: Pandas, NumPy, Scikit-learn, Prophet, TensorFlow/Keras (optional for LSTM)  
**Charts**: Matplotlib, Plotly  
**Hosting**: Streamlit Cloud  

---

## 🚀 Quick Start (Local)
**Requirements:** Python 3.9+  

```bash
# Clone the repo
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


## 🔬 Models & How They Work
- **Simple Moving Average (SMA)** → Baseline rolling averages.  
- **Linear Regression** → Uses lag features for predictions.  
- **Prophet** → Captures trends & seasonality.  
- **LSTM** → Deep learning model for time-series forecasting (optional).  

**Workflow:**
1. Fetch historical adjusted close prices.  
2. Preprocess data (cleaning, lag features, scaling).  
3. Train & validate model.  
4. Display predictions alongside historical charts in Streamlit UI.  

---

## 📈 Evaluation Metrics
- **MAE** (Mean Absolute Error)  
- **RMSE** (Root Mean Squared Error)  
- **MAPE** (Mean Absolute Percentage Error)  

---

## ⚠️ Limitations & Disclaimer
- Predictions rely only on historical prices — no external signals.  
- Market events can cause unexpected price movements.  
- Strictly for **educational purposes only**.  



## 👨‍💻 Author
Made with ❤️ by Asim Husain www.asimhusain.dev
