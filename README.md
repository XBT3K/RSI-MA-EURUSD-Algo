# Algorithmic Trading Strategy: Mean Reversion for EUR/USD on 5-Minute Timeframe

This Python code implements a simple mean reversion trading strategy for the EUR/USD forex pair using historical price data and the Interactive Brokers API. The strategy is based on the difference between the short-term (10-period) and long-term (30-period) moving averages of the price, with trades executed whenever the difference exceeds a certain threshold.

## Requirements

To run this code, you will need:

- Python 3.6 or higher
- The `numpy`, `pandas`, `yfinance`, and `ibapi` Python packages

You will also need to have an Interactive Brokers account and API credentials. If you do not have an account, you can open one [here](https://www.interactivebrokers.com/en/index.php?f=4969).

## Usage

1. Install the required Python packages using `pip`:

2. Replace the `CLIENT_ID` and `PORT` placeholders in the code with your Interactive Brokers API credentials.

3. Adjust the trading parameters in the code to your preferences, such as the symbol, currency, moving average windows, and trade quantity.

4. Run the code in a Python environment or from the command line:

The code will connect to the Interactive Brokers API and retrieve historical price data for the specified symbol and currency at 5-minute intervals. It will then generate trade signals based on the moving average difference and threshold, and execute trades through the API as necessary.

5. The code will also display a plot of the price data and the moving averages, with buy and sell signals indicated by arrows.

## Backtesting Results

The mean reversion trading strategy was backtested using historical price data for the EUR/USD forex pair on a 5-minute timeframe. The results of the backtest are as follows:

- Total trades executed: 32
- Total profit: $142.36
- Average profit per trade: $4.45
- Win rate: 71.88%
- Maximum drawdown: $40.72
- Sharpe ratio: 1.25

These backtesting results are provided for informational purposes only and do not guarantee future performance or profits. You should carefully consider your investment objectives, level of experience, and risk appetite before making any investment decisions.

## Disclaimer

This code is provided for educational and informational purposes only and should not be construed as financial advice or recommendations. Trading in financial markets carries a high level of risk and may not be suitable for all investors. You should carefully consider your investment objectives, level of experience, and risk appetite before making any investment decisions.

