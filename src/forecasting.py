from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
import pandas as pd

def train_arima_model(df, order=(5,1,0), forecast_steps=30):
    model = ARIMA(df['Price'], order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=forecast_steps)
    return forecast

def train_prophet_model(df, forecast_days=30):
    df = df.reset_index().rename(columns={"Date": "ds", "Price": "y"})
    model = Prophet(daily_seasonality=True)
    model.fit(df)
    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']]
