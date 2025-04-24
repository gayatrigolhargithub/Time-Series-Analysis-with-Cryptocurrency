# 🧠 Crypto Time Series Forecasting App

An interactive dashboard that predicts future cryptocurrency prices using ARIMA and Prophet time series models. Built with Python, Streamlit, and yfinance.

---

## 📦 Features

- 📊 **Historical Data Collection** from Yahoo Finance (`yfinance`)
- 🧹 **Data Preprocessing** with Pandas
- 🔮 **Forecasting Models**:
  - ARIMA (Statsmodels)
  - Prophet (Meta)
- 📈 **Interactive Dashboard** with Streamlit
- 💾 Organized code structure with `src/` folder

---

## 📸 Screenshot

*Insert a screenshot of your Streamlit dashboard here (optional)*

---
## 📁 Project Structure

''' time-series-analysis-with-cryptocurrency/ ├── src/ │ ├── main.py │ ├── gui.py │ ├── data_collector.py │ ├── preprocessing.py │ ├── forecasting.py │ └── init.py ├── venv/ (ignored) ├── .gitignore └── README.md '''


## 🛠️ Tech Stack
Python

Pandas, Statsmodels, Prophet

yfinance

Streamlit


## 🚀 Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run src/main.py
