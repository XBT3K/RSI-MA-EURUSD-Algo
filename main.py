import numpy as np
import pandas as pd
import yfinance as yf
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order

# Set up the trading strategy parameters
symbol = "EUR"
currency = "USD"
short_window = 10
long_window = 30
threshold = 2
quantity = 10000

# Define the Interactive Brokers API wrapper and client
class IBWrapper(EWrapper):
    def __init__(self):
        self.order_id = None
    
    def nextValidId(self, order_id):
        self.order_id = order_id

class IBClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

# Create the Interactive Brokers API contract and order objects
contract = Contract()
contract.symbol = symbol
contract.secType = 'CASH'
contract.currency = currency
contract.exchange = 'IDEALPRO'

order = Order()
order.action = ''
order.totalQuantity = quantity
order.orderType = ''
order.lmtPrice = 0
order.auxPrice = 0

# Connect to the Interactive Brokers API and request market data
wrapper = IBWrapper()
client = IBClient(wrapper)
client.connect('', 7497, 0)

# Get historical data for the symbol at 5-minute intervals
data = yf.download(f"{symbol}{currency}=X", interval="5m", start="2020-01-01", end="2022-02-17")

# Calculate the short and long moving averages
data['short_mavg'] = data['Close'].rolling(window=short_window).mean()
data['long_mavg'] = data['Close'].rolling(window=long_window).mean()

# Define the entry and exit signals
data['signal'] = 0.0
data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] 
                                          > (data['long_mavg'][short_window:] + threshold * np.std(data['Close'][short_window:])), 1.0, 0.0)       
data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] 
                                          < (data['long_mavg'][short_window:] - threshold * np.std(data['Close'][short_window:])), -1.0, data['signal'][short_window:])

# Generate the trade orders
data['position'] = data['signal'].diff()
for i in range(1, len(data)):
    if data['position'].iloc[i] == 1.0:
        order.action = 'BUY'
        order.orderType = 'LMT'
        order.lmtPrice = data['Close'].iloc[i]
        client.placeOrder(wrapper.order_id, contract, order)
    elif data['position'].iloc[i] == -1.0:
        order.action = 'SELL'
        order.orderType = 'LMT'
        order.lmtPrice = data['Close'].iloc[i]
        client.placeOrder(wrapper.order_id, contract, order)

# Disconnect from the Interactive Brokers API
client.disconnect()

# Plot the results
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(111, ylabel=f"{symbol}/{currency}")
data['Close'].plot(ax=ax1, color='black', lw=2.)
data[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
ax1.plot(data.loc[data.position == 1.0].index, data.short_mavg[data.position == 1.0
