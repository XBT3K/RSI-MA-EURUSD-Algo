import time
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders

# define your own parameters here
access_token = "YOUR_ACCESS_TOKEN"
accountID = "YOUR_ACCOUNT_ID"
instrument = "EUR_USD"
units = 1000
stop_loss = 0.0020
take_profit = 0.0050

# establish connection to OANDA API
api = oandapyV20.API(access_token=access_token)

# define function to get current price data
def get_price():
    params = {
        "instruments": instrument,
        "granularity": "M1"
    }
    r = instruments.InstrumentsCandles(instrument=instrument, params=params)
    response = api.request(r)
    price_data = response["candles"][0]["mid"]
    return float(price_data["c"])

# define function to enter a trade
def enter_trade(units, stop_loss, take_profit):
    data = {
        "order": {
            "instrument": instrument,
            "units": units,
            "type": "MARKET",
            "stopLossOnFill": {
                "price": str(get_price() - stop_loss),
                "timeInForce": "GTC"
            },
            "takeProfitOnFill": {
                "price": str(get_price() + take_profit),
                "timeInForce": "GTC"
            }
        }
    }
    r = orders.OrderCreate(accountID, data=data)
    api.request(r)

# define function to exit a trade
def exit_trade(tradeID):
    data = {
        "order": {
            "type": "MARKET",
            "tradeID": tradeID
        }
    }
    r = orders.OrderCreate(accountID, data=data)
    api.request(r)

# define main trading loop
while True:
    current_price = get_price()
    last_price = current_price
    time.sleep(60) # wait 1 minute before checking price again
    current_price = get_price()
    if current_price < last_price:
        enter_trade(units, stop_loss, take_profit)
        time.sleep(60) # wait 1 minute before checking price again
        trade_details = api.trade.get(accountID=accountID, tradeID=response["orderFillTransaction"]["tradeID"])
        tradeID = trade_details["trade"]["id"]
        exit_trade(tradeID)
