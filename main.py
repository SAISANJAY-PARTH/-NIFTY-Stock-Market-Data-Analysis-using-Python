import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------- STOCK UNIVERSE --------
TICKERS = ["RELIANCE.NS" ,"TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS","SBIN.NS","AXISBANK.NS","KOTAKBANK.NS","LT.NS","ITC.NS",
"HINDUNILVR.NS","BAJFINANCE.NS","BHARTIARTL.NS","ASIANPAINT.NS","MARUTI.NS","SUNPHARMA.NS","ULTRACEMCO.NS","TITAN.NS","NESTLEIND.NS","POWERGRID.NS",
"NTPC.NS","ONGC.NS","COALINDIA.NS","ADANIENT.NS","ADANIPORTS.NS"]

# -------- DOWNLOAD DATA --------
end = pd.Timestamp.today()
start = end - pd.DateOffset(years=1)

data = yf.download(TICKERS,start=start,end=end,
                   auto_adjust=True,progress=False)["Close"]

returns = data.pct_change().dropna()

# -------- SUMMARY STATISTICS --------
summary = pd.DataFrame({
    "Mean Return": returns.mean()*252,
    "Volatility": returns.std()*np.sqrt(252),
    "Max Price": data.max(),
    "Min Price": data.min()
})

print("\n=== STOCK SUMMARY ===")
print(summary)

# -------- CORRELATION MATRIX --------
corr = returns.corr()

plt.figure(figsize=(10,6))
plt.imshow(corr, cmap="coolwarm", interpolation="none")
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=90)
plt.yticks(range(len(corr)), corr.columns)
plt.title("Stock Correlation Matrix")
plt.show()

# -------- VOLATILITY COMPARISON --------
volatility = returns.std()*np.sqrt(252)

volatility.sort_values().plot(kind="bar", figsize=(10,5))
plt.title("Annualized Volatility")
plt.ylabel("Volatility")
plt.show()

# -------- PRICE TREND --------
data.plot(figsize=(11,6))
plt.title("Stock Price Trends")
plt.ylabel("Price")
plt.show()
