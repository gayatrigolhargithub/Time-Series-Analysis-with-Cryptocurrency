# src/preprocessing.py

import pandas as pd

def clean_crypto_data(df):
    """
    Cleans the raw data by handling missing values and selecting required columns.
    :param df: raw crypto DataFrame
    :return: cleaned DataFrame with Date and Close Price
    """
    df = df[['Date', 'Close']].dropna()
    df.columns = ['Date', 'Price']
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df
