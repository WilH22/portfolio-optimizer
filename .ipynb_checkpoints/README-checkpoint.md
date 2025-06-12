# 📊 Portfolio Optimization Tool

An interactive Python-based application to construct optimal investment portfolios using Modern Portfolio Theory. This tool uses Modern Portfolio Theory (MPT) to maximize return for a given level of risk, or minimize risk for a given level of return. It solves a convex optimization problem with constraints on weights (e.g., fully invested and no shorting).
## 📘 Overview

This project implements a portfolio optimization tool that uses real historical stock data to:
- Calculate expected returns and risks
- Optimize portfolio weights using Mean-Variance Optimization (Markowitz Model)
- Visualize the results (coming soon!)
- Provide an interactive interface (via Streamlit, optional)

It’s built to showcase core concepts in financial engineering and serves as part of my preparation for the NUS MFE program.

## 🚀 Features

- 📈 Fetch live stock data using `yfinance`
- 📊 Calculate annualized returns and covariance
- 🧠 Optimize portfolio weights using `cvxpy`
- 💡 Simple command-line interface (CLI)
- 🔄 Streamlit web app (coming soon)

## 🛠️ Tech Stack

- Python 3
- yfinance
- numpy, pandas
- cvxpy
- Streamlit (optional)

## ⚙️ How to Use

### Clone the Repo
```bash
git clone https://github.com/wiellyhalim/portfolio-optimizer.git
cd portfolio-optimizer

pip install -r requirements.txt

## 📌 Sample Output

