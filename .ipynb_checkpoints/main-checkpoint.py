import yfinance as yf
import pandas as pd
import cvxpy as cp
import numpy as np

def fetch_data(tickers, start="2020-01-01", end="2024-12-31"):
    """
    Fetch adjusted close prices using yfinance.
    Returns a DataFrame of daily adjusted returns.
    """
    data = yf.download(tickers, start=start, end=end, group_by='ticker',auto_adjust=True)
    adj_close = data.xs('Close', level=1, axis=1)
    adj_close = adj_close.dropna()
    returns = adj_close.pct_change().dropna()
    return adj_close, returns

def optimize_portfolio(expected_returns, cov_matrix, risk_aversion=1.0):
    """
    Mean-variance optimization using cvxpy.
    """
    n = len(expected_returns)
    w = cp.Variable(n)
    mu = expected_returns.values
    Sigma = cov_matrix.values

    objective = cp.Maximize(mu @ w - risk_aversion * cp.quad_form(w, Sigma))
    constraints = [cp.sum(w) == 1, w >= 0]
    prob = cp.Problem(objective, constraints)
    prob.solve()

    return w.value

from modules.data_loader import fetch_data
from modules.optimizer import optimize_portfolio
import pandas as pd

#Step 1: Input tickers
tickers = input("Enter tickers (comma separated): ").split(",")
tickers = [t.strip().upper() for t in tickers]

#Step 2: Fetch data
adj_close, returns = fetch_data(tickers)

#Step 3: Compute metrics
expected_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

#Step 4: Optimize
optimal_weights = optimize_portfolio(expected_returns, cov_matrix, risk_aversion=1.0)

#Step 5: Display results
result = pd.DataFrame({
    'Ticker': tickers,
    'Optimal Weight': optimal_weights
})
print("\nOptimal Portfolio Allocation:")
print(result)