from src.data_collector import get_crypto_data
from src.preprocessing import clean_crypto_data
from src.forecasting import train_arima_model, train_prophet_model

df_raw = get_crypto_data("BTC-USD", "3mo")
df_clean = clean_crypto_data(df_raw)

# ARIMA Forecast
arima_forecast = train_arima_model(df_clean)
print("\nARIMA Forecast:\n", arima_forecast.head())

# Prophet Forecast
prophet_forecast = train_prophet_model(df_clean)
print("\nProphet Forecast:\n", prophet_forecast.tail())
