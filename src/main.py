from data_collector import get_crypto_data
from preprocessing import clean_crypto_data
from forecasting import train_arima_model, train_prophet_model

df_raw = get_crypto_data("BTC-USD", "3mo")
df_clean = clean_crypto_data(df_raw)

# ARIMA
forecast = train_arima_model(df_clean)

# Prophet
prophet_forecast = train_prophet_model(df_clean)

import gui

# Display in Streamlit
gui.display_dashboard(df_clean, forecast, prophet_forecast)


