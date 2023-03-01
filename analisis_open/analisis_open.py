import pandas as pd
import numpy as np

# file = "EURUSD_Monthly_2021_2023.csv"
# df = pd.read_csv(file, sep="\t", header=0, usecols= [0,1,2,3,4], 
#             names= ["date",	"open",	"high",	"low", "close"])

# file = "EURUSD_M1_2021_2023.csv"
file = "EURUSD_M5_2021_2023.csv"
# file = "EURUSD_M15_2021_2023.csv"
# file = "EURUSD_M30_2021_2023.csv"

to_point = 100000
time_1 = "10:00:00"
time_2 = "23:00:00"
filtrar_puntos = 10

df = pd.read_csv(file, sep="\t", header=0, usecols= [0,1,2,3,4,5], 
            names= ["date",	"time", "open",	"high",	"low", "close"])

df["high-open"] = ((df["high"] - df["open"]) * to_point)
df["open-low"] = ((df["open"] - df["low"]) * to_point)

df = df[(df["time"] > time_1) & (df["time"] < time_2)]

series_points= pd.concat([df["high-open"], df["open-low"]])
series_points = series_points.sort_values(ascending=True)

zero_points = (series_points >= filtrar_puntos).value_counts()
zero_points_true = (series_points == 0).value_counts()[0]
zero_points_false = (series_points == 0).value_counts()[1]

zero_points =pd.DataFrame(data=zero_points).reset_index(drop=False)
zero_points["1"] = ((zero_points[0]/(zero_points_true + zero_points_false))*100).round()

print(zero_points)

