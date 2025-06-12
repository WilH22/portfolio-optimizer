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
✅ The input is not case-sensitive and automatically trims spaces, so these are all valid:

![image](https://github.com/user-attachments/assets/efb233ae-af90-40a8-b049-4b9164504f8d)


## 📈 Example Output
- 💼 Optimal Portfolio Allocation:

![image](https://github.com/user-attachments/assets/8fc0c81a-f6d6-495b-9f4b-75bd4d524b34)



(excluded 0% weight from chart)

- 📉 Portfolio Metrics:  

![image](https://github.com/user-attachments/assets/ab66f31b-4bc1-40b4-a890-ad735621d10a)


- 📊 Visualization:
  - 🥧 Clean pie chart with `[TICKER]` labels

![image](https://github.com/user-attachments/assets/bc27cb54-e7d1-4107-8271-d388d56b8763)
  
  - 📈 Portfolio value curve over time

![image](https://github.com/user-attachments/assets/41555c1c-5054-4ca1-9126-e1f169f36d8b)

  - 📈 Efficient frontier plot

![image](https://github.com/user-attachments/assets/facff4ce-71e7-4bbd-885c-5af9c4aefac8)

---

## 🧪 Technologies Used

- Python 3.x  
- `yfinance` – market data  
- `cvxpy` – optimization modeling  
- `numpy`, `pandas` – data analysis  
- `matplotlib` – charting  
