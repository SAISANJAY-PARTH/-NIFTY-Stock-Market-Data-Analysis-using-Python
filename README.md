# 📈 NIFTY Stock Market Data Analysis using Python

## Overview
This project performs exploratory data analysis (EDA) on a large universe of Indian stock market equities using Python.  
The goal is to understand price trends, volatility, correlations, and return characteristics across major stocks listed on the NSE.

Using financial time series data, the project analyzes market behavior over the past year and extracts insights about stock performance and risk dynamics.

---

## Objectives
- Analyze stock price trends across multiple NSE-listed companies
- Measure and compare annualized returns and volatility
- Study correlations between stocks to understand diversification
- Visualize financial market behavior using Python

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- yFinance

---

## Data Source
Stock market data is retrieved using the **Yahoo Finance API** via the `yfinance` Python library.

Data includes:
- Historical closing prices
- Daily returns
- Volatility estimates

---

## Analysis Performed

### 1. Stock Price Trend Analysis
Visualizes historical price movements across multiple companies to understand market behavior.

### 2. Annualized Volatility
Measures risk levels of stocks by calculating annualized standard deviation of returns.

### 3. Correlation Matrix
Examines relationships between stock returns to identify diversification opportunities.

### 4. Summary Statistics
Key metrics computed for each stock:
- Annualized Return
- Volatility
- Maximum Price
- Minimum Price

---

## Visualizations
The project generates:

- 📈 Stock Price Trend Charts
- 📊 Annualized Volatility Comparison
- 🔥 Correlation Heatmap
- 📉 Return Distribution Insights

---

## Example Insights
- Certain sectors show significantly higher volatility compared to others.
- Metals and energy stocks exhibited stronger returns during the analysis period.
- Some IT stocks showed negative annual performance during the same timeframe.

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/stock-market-analysis.git
