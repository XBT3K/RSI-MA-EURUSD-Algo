import pandas as pd
import numpy as np
from mean_reversion_trading import MeanReversionTrading

# Define backtesting parameters
start_date = "2021-05-01T00:00:00Z"
end_date = "2021-05-31T23:59:00Z"
granularity = "M1"

# Load historical price data from CSV file
df = pd.read_csv("eurusd_1m.csv")

# Convert timestamp to DateTimeIndex
df.index = pd.DatetimeIndex(df["timestamp"])
df = df.drop(columns=["timestamp"])

# Instantiate trading algorithm
mrt = MeanReversionTrading()

# Backtest trading algorithm
results = mrt.backtest(df, start_date, end_date, granularity)

# Print backtesting results
print("Net profit: {:.2f} pips".format(results["net_profit"]))
print("Total trades: {}".format(results["total_trades"]))
print("Win rate: {:.2f}%".format(results["win_rate"] * 100))
print("Profit factor: {:.2f}".format(results["profit_factor"]))
