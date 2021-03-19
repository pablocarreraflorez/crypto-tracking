# Imports
import config
import pandas as pd
from datetime import datetime, timedelta
from binance.client import Client


def download_1week(symbol: str) -> pd.DataFrame:
    """
    Use Binance API to download 1 week of OHLCV data from one pair. Since process is going to
    run on mondays, it has to retrieve data from past week's monday to sunday.

    :param str symbol: symbol to track in Binance.
    :return: pd.DataFrame, OHLCV data from symbol.
    """
    # Log
    print('{} Downloading {} from Binance'.format(datetime.today(), symbol))

    # Create client
    client = Client(config.API_KEY, config.SECRET_KEY)

    # Obtain dates
    date_monday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    date_sunday = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

    # Get data
    data = client.get_historical_klines(symbol=symbol,
                                        interval=Client.KLINE_INTERVAL_1DAY,
                                        start_str=date_sunday,
                                        end_str=date_monday
                                        )

    # Convert to dataframe
    df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', '', '', '', '', '', ''])

    # Keep only relevant columns
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    # Clean types
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')
    df['Open'] = pd.to_numeric(df['Open'])
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = pd.to_numeric(df['Low'])
    df['Close'] = pd.to_numeric(df['Close'])
    df['Volume'] = pd.to_numeric(df['Volume'])

    return df
