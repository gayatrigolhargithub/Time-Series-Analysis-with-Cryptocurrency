import yfinance as yf
import pandas as pd

def get_crypto_data(symbol="BTC-USD", period="1y", interval="1d"):
    df = yf.download(symbol, period=period, interval=interval)
    df.reset_index(inplace=True)
    return df


