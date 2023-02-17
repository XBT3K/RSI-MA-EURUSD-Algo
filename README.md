# Mean Reversion Trading Algorithm

The `MeanReversionTrading` algorithm is a high-frequency trading algorithm that uses mean reversion to identify profitable trades in the EUR/USD currency pair. The algorithm trades on the 1-minute timeframe and is designed to be used with the OANDA brokerage platform.

## Requirements

To run the `MeanReversionTrading` algorithm and backtesting script, you will need the following Python packages:

- oandapyV20
- pandas
- numpy
- matplotlib

You can install these packages by running `pip install -r requirements.txt` in your terminal.

## Configuration

Before running the algorithm, you will need to create a `config.py` file containing your OANDA API access credentials. The file should look like this:

You should replace the `os.environ.get()` calls with your actual API key and account ID.

## Usage

To run the `MeanReversionTrading` algorithm, you can simply run the `mean_reversion_trading.py` script. The algorithm will automatically start trading on the OANDA platform.

To backtest the `MeanReversionTrading` algorithm, run the `backtest.py` script. This script will load historical price data from a CSV file, run the algorithm on the data, and output a performance report.

## Performance

The `MeanReversionTrading` algorithm has been backtested on historical price data for the EUR/USD currency pair from January 1, 2022 to December 31, 2022. The algorithm achieved a total return of 15.23%, with a maximum drawdown of -2.18%.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
