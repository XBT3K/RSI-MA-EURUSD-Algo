import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import pandas as pd

# Define API credentials
api_key = 'YOUR_API_KEY'
account_id = 'YOUR_ACCOUNT_ID'

# Define the instrument to get data for
instrument = 'EUR_USD'

# Define the time range to get data for
params = {
    'from': '2022-01-01T00:00:00Z',
    'to': '2022-12-31T23:59:59Z',
    'granularity': 'M1'
}

# Create an API client
client = oandapyV20.API(access_token=api_key)

# Request the historical price data
r = instruments.InstrumentsCandles(instrument=instrument, params=params)
data = client.request(r)

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data['candles'])

# Extract the relevant columns and rename them
df = df[['time', 'mid']]
df.columns = ['time', 'price']

# Convert the time column to a datetime object and set it as the index
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)

# Save the data to a CSV file
df.to_csv('eur_usd_price_data.csv')
