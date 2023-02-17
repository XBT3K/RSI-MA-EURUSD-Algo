Mean Reversion Trading Algorithm
This is a simple mean reversion trading algorithm that trades the EUR/USD forex pair based on a rolling window of the previous close prices.

Installation
Clone the repository
Install the required packages by running pip install -r requirements.txt
Fill in the necessary credentials for your OANDA account and API in the mean_reversion.py file
Usage
To run the algorithm, simply run the mean_reversion.py file. The algorithm will run continuously and execute trades based on the mean reversion strategy.

By default, the algorithm uses a 20-period window size, an overbought threshold of 1.5, and an oversold threshold of -1.5. These values can be modified in the MeanReversion class in the mean_reversion.py file.

Disclaimer
This trading algorithm is provided for educational and informational purposes only and should not be considered as investment advice. The performance of the algorithm may vary depending on market conditions and past performance does not guarantee future results. You should thoroughly backtest and evaluate the performance of the algorithm before using it with real money.

License
This algorithm is licensed under the MIT License. See LICENSE for more information.

You can also add any other information that you feel is relevant, such as performance metrics, how to interpret the algorithm's output, or troubleshooting tips.
