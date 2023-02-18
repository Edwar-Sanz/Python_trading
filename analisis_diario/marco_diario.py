import yfinance as yf
import pandas as pd
import numpy as np


asset = yf.Ticker("^GSPC")
df = asset.history(period="max")
df.reset_index(inplace=True)

df = df[["Date", "Open", "High", "Low", "Close"]]
df[["Open", "High", "Low", "Close"]] = df[["Open", "High", "Low", "Close"]].round(1)
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.date
df["Date"] = pd.to_datetime(df["Date"])
df["Mes"] = df["Date"].dt.strftime('%B')
df["Day"] = df["Date"].dt.strftime('%A')
df["Clande_type"] = np.where(df["Close"] - df["Open"] > 0, "Green", "Red")
df["next_low"] = df['Low'].shift(-1)
df["next_High"] = df['Low'].shift(-1)

df["Correction"] = np.where(df["Clande_type"] == "Green",
                            df["Close"] - df["next_low"], 
                            df["next_High"] - df["Close"])



print(df.iloc[20000:20050])

