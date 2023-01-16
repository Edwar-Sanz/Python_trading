import yfinance as yf
import pandas as pd

asset = yf.Ticker("^GSPC")
df = asset.history(period="max")
df.reset_index(inplace=True)

df.iloc[1, 1] = df.iloc[1, 4]
for i in range(1, len(df)):
	df.iloc[i, 1] = df.iloc[i-1, 4]

print(df)

