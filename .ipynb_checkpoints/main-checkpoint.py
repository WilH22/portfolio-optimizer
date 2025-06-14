import yfinance as yf
import pandas as pd
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

from modules.data_loader import fetch_data
from modules.optimizer import optimize_portfolio
from modules.efficient_frontier_plot import plot_efficient_frontier
from modules.visualizer import plot_portfolio_growth
from modules.visualizer import plot_portfolio_weights

#Step 1: Input tickers
tickers = input("Enter tickers (comma separated): ").split(",")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
tickers = [t.strip().upper() for t in tickers]

# Step 2: Fetch data

adj_close, returns = fetch_data(tickers, start=start_date, end=end_date)

# Step 3: Compute metrics
expected_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252
cov_matrix = (cov_matrix + cov_matrix.T) / 2  # Force symmetry

#Step 4: Optimize
optimal_weights = optimize_portfolio(expected_returns, cov_matrix, risk_aversion=1.0)

#Step 5: Display results
result = pd.DataFrame({
    'Ticker': tickers,
    'Optimal Weight': optimal_weights
})
print("\nOptimal Portfolio Allocation:")
print(result)
print("\nSum of weights:", round(optimal_weights.sum(), 4))
print("Are any weights negative?", (optimal_weights < 0).any())

#Expected Portfolio Return
port_return = np.dot(optimal_weights, expected_returns) 

#Portfolio Risk (Volatility)
port_volatility = np.sqrt(optimal_weights.T @ cov_matrix.values @ optimal_weights) 

#Sharpe Ratio (assume risk-free=0%)
sharpe_ratio = port_return / port_volatility 

print(f"\nExpected Return: {port_return:.2%}")
print(f"Volatility (Risk): {port_volatility:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# 🔥 Plot portfolio weight distribution
plot_portfolio_weights(optimal_weights, result['Ticker'])

# 📈 Plot portfolio growth over time
portfolio_returns = (returns @ optimal_weights).dropna()
plot_portfolio_growth(portfolio_returns)

# 📈 Plot Efficient Frontier
plot_efficient_frontier(expected_returns.values, cov_matrix.values)

# Save adjusted close prices to data/close_prices_sample.csv
adj_close.to_csv("data/close_prices_sample.csv")
print("Adjusted close prices saved.")
# Save optimized weights to data/portfolio.csv
result.to_csv("data/portfolio.csv", index=False)
print("Optimized portfolio weights saved.")
