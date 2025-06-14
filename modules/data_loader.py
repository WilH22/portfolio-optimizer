import yfinance as yf
import pandas as pd
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

def fetch_data(tickers, start=None, end=None):
    import datetime

    # Use default dates if user does not provide them
    if not start:
        start = "2020-01-01"
    if not end:
        end = datetime.datetime.today().strftime("%Y-%m-%d")

    data = yf.download(tickers, start=start, end=end, group_by='ticker', auto_adjust=True)

    # Handle both single and multi-level column format
    if isinstance(data.columns, pd.MultiIndex):
        try:
            adj_close = data.xs('Close', level=1, axis=1)
        except KeyError:
            raise ValueError("❌ 'Adj Close' prices not found — possibly all tickers failed.")
    else:
        if 'Close' in data.columns:
            adj_close = data['Close'].to_frame()
        else:
            raise ValueError("❌ No 'Adj Close' in single-column format.")

    # Drop tickers with no data
    adj_close = adj_close.dropna(axis=1, how='all')

    # ✅ Detect failed tickers
    successful = list(adj_close.columns)
    failed = [t for t in tickers if t not in successful]

    if not successful:
        raise ValueError("❌ Tickers failed to download.")
    
    if failed:
        print(f"\n⚠️ The following tickers failed to download (check for typos or delisting): {failed}")

    returns = adj_close.pct_change().dropna()
    return adj_close, returns
