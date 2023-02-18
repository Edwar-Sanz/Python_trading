import yfinance as yf
import pandas as pd


asset = yf.Ticker("^GSPC")
df = asset.history(period="max")
df.reset_index(inplace=True)

df = df[["Date", "Open", "High", "Low", "Close"]]
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.date
print(df)

