# src/gui.py

import streamlit as st
import matplotlib.pyplot as plt

def display_dashboard(data, arima_forecast, prophet_forecast):
    st.set_page_config(page_title="Crypto Forecast Dashboard", layout="centered")

    st.title("📈 Crypto Price Forecasting")
    
    st.subheader("📊 Recent Price Data")
    st.line_chart(data['Price'])

    st.subheader("🔮 ARIMA Forecast (Next 30 Days)")
    st.line_chart(arima_forecast)

    st.subheader("📅 Prophet Forecast (Next 30 Days)")
    fig, ax = plt.subplots()
    ax.plot(prophet_forecast['ds'], prophet_forecast['yhat'], label='Prophet Forecast', color='green')
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)
