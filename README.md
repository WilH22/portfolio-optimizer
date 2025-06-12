# 📊 Optimal Portfolio Allocation Tool

This Python-based financial engineering tool allows users to construct an **optimized investment portfolio** using real-time market data and quantitative methods. It applies **Modern Portfolio Theory (MPT)** and convex optimization (via `cvxpy`) to generate **long-only portfolios** that maximize return for a given level of risk.

Whether you're an aspiring quant, finance student, or curious investor, this tool helps you **analyze asset performance, visualize optimal allocation, and simulate portfolio growth** with clean, professional outputs.

---

## 🔧 Features

✅ Fetches historical **adjusted close prices** from Yahoo Finance using `yfinance`  
✅ Computes annualized **expected returns** and **covariance matrix**  
✅ Solves the **mean-variance optimization** problem using `cvxpy`  
✅ Enforces realistic constraints: **long-only**, fully invested (weights sum to 1)  
✅ Automatically **cleans tiny or invalid weights**, preventing noise  
✅ Visualizes allocation with a beautiful, labeled **pie chart**  
✅ Simulates **portfolio growth** with backtested cumulative returns  
✅ Detects and logs **invalid tickers** or **zero-weighted assets**  

---

## 📈 Example Output

- 💼 Optimal Portfolio Allocation:



(excluded 0% weight from chart)

- 📉 Portfolio Metrics:  


- 📊 Visualization:
  - 🥧 Clean pie chart with `[TICKER]` labels  
  - 📈 Portfolio value curve over time  
  - (Optional) Efficient frontier plot

---

## 🧪 Technologies Used

- Python 3.x  
- `yfinance` – market data  
- `cvxpy` – optimization modeling  
- `numpy`, `pandas` – data analysis  
- `matplotlib` – charting  