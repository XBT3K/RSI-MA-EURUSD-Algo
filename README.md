# Modified Mean Reversion Trading Strategy

This is a modified mean reversion trading strategy that generates buy and sell signals based on the relative strength index (RSI) and moving average (MA) of the EUR/USD currency pair on a 1-minute timeframe. The strategy uses the OANDA API to enter and exit trades automatically.

## Requirements

To run this code, you will need:

- A valid OANDA account
- An API access token and account ID
- Python 3.x
- The following Python packages: oandapyV20, pandas, numpy, ta

## Usage

1. Clone the repository to your local machine.
2. Install the required packages by running the following command:
3. 
3. Open the `config.py` file and replace the placeholders with your OANDA API access token and account ID.
4. Run the `mean_reversion_trading.py` file to start the trading algorithm.

## Backtesting Results

This strategy was backtested on historical price data from the EUR/USD currency pair on a 1-minute timeframe from May 1, 2021 to May 31, 2021. Over this testing period, the strategy generated a small profit, with a profit factor of 1.11. However, further optimization and testing are necessary to improve its performance over the long term.

![Backtesting results for modified mean reversion strategy on EUR/USD 1-minute timeframe](https://i.imgur.com/0dJfxh1.png)

## Disclaimer

This code is provided for educational purposes only and should not be used for real-world trading without proper testing and validation. Trading involves a high level of risk, and past performance is not indicative of future results.

## License

This code is released under the MIT License. See the `LICENSE` file for more information.
